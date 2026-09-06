# 14 · THE WORLD IN THE ROOM — what a matter is, how the world gets in, and what a person brings

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Written in answer to a Jordan question that exposed a real thinness: the design said *"the matter is
## a Proposition"* and stopped, which is not enough to run a treaty negotiation, a title dispute, a
## question of fact and a debate about an invasion through one structure.

> **Jordan, 2026-09-06:** *"How will the system be able to bring in epistemics and events tracked
> season over season, character by character? How will one negotiate over a contested item like 'who
> owns this settlement' or argue over 'what are the terms of this treaty' or debate whether 'is it
> true that this occurred' or discuss 'what should we do about the possibility of invasion'? How do
> events/facts/pressures/clocks/issues/concerns/demands/impositions make their way into this system,
> and how do characters' biases (allegiance, ethical convictions, influences, ambitions, etc) and
> knowledge (how much they know, from what perspective, etc) affect their behaviour and choices?"*

---

> ## THE SHORT ANSWER, AND THE HALF OF IT THAT IS BAD NEWS
>
> **Every carrier this question asks for already exists and already runs.** Epistemics are `Claim`
> rows in each person's own ledger, deposited per witness per channel, fading on the one licensed
> clock. Allegiance is a `commit` edge. Convictions are a field a scoring function already reads.
> Ambition is one of four question sources. **This subsystem adds none of it and consumes all of it.**
>
> ⚠ **AND THE CHANNEL FROM ALL OF IT TO A DECISION IS MEASURED-SEVERED TODAY.** The degree sweep
> flipped every mechanical decision in 143 cases — 2,403 forks — and **not one changed any of the
> next three decisions.** The cause is exact: `Query.opening_set` has four clauses and **none consults
> world state**; the single channel from consequence to decision is a claim in the actor's own ledger,
> and that channel is closed by a **type mismatch** — over 4,800 measured claims, the predicate
> vocabularies are **disjoint** and **zero** claims are falsy.
>
> **So the honest answer is: the shape below is right, the carriers are right, and none of it reaches
> a choice until `H-72` / `H-116` / `F.24` are closed. This subsystem does not fix that and is
> blocked by it exactly as everything else is.**

---

# PART A · WHAT A MATTER IS — the mood selects the genre, and that is the missing piece

A published draft said *"the matter is a `Proposition`"* and stopped. **Four of Jordan's examples are
four different kinds of matter, and the ontology already distinguishes them.**

`§D.5`: *"A **HOLDS** Proposition is a claim about the world; an **OUGHT** Proposition **is an uttered
Belief**."* And Fig. 23: **the species of a speech is fixed by what the hearer's office requires him
to decide** — the past, the future, or the present.

> ### **SO THE MATTER'S MOOD SELECTS THE GENRE, AND THE GENRE SELECTS THE LADDER.**

| the matter's mood | what is in dispute | genre | ladder | what a disposal writes |
|---|---|---|---|---|
| **HOLDS** — an assertion about how the world is | **whether it is so** | **forensic** | ⭐ **the issue ladder runs** | a `Tenure` opened or closed |
| **OUGHT** — an uttered belief about what should be | **whether to** | **deliberative** | **none.** The fact is not in dispute | an `issue`, a `levy`, a `commit` |
| **neither — no bench** | **who is worth what** | **epideictic** | none | standing only |

⚠ **This is a derivation this directory owed and had not made**, and it is banked with a note: **an
independent Fable synthesis under the same brief reached the same mapping from the other end** —
*"the genre triangle maps species → carrier."* **Two derivations converging on a mapping neither took
from the other is corroboration** (`§G.4.3`), and it is the only place in this exercise where that
happened cleanly.

## A.1 · Jordan's four, worked

### **"Who owns this settlement"** — a HOLDS matter, forensic, and it is a Tenure dispute
```
matter    : Proposition(HOLDS, "hold(Aldric, Vellenmark)")   -- uttered by somebody, immutable, authored
parties   : Aldric commits to it · Rulf commits to a rival HOLDS naming himself
bench     : the seats whose remit covers a holding at that rung  -- judging_set, a containment WALK
ladder    : issue.  procedural ("this bench cannot hear a duchy matter") →
            conjecture ("the grant was never made") → definition ("it was a wardship, not a grant")
            → quality ("it was made, and it was void")
disposal  : `determine` writes `Tenure.degree` on the hold; a losing hold is closed by `T-o`
```
⭐ **The dispute is never over "the settlement". It is over a Proposition somebody uttered about it**
— which is why it has an author, a date, and a document that can be forged or burned.

### **"What are the terms of this treaty"** — an OUGHT matter, `disposal: mutual`, and the mechanism is elegant
**A `Proposition` is immutable** (`§D.5`: *"adding a mutable field to a Proposition is a category
error"*). **So terms are never edited.** A negotiation is:

```
A utters  OUGHT("A yields the ford; B pays 40 in grain")        -- a complete set of terms
B refuses to commit; utters OUGHT("A yields the ford; B pays 25")
A utters  OUGHT("A yields the ford; B pays 32; B garrisons it")
BOTH commit to that one                                          -- the treaty EXISTS
```

> **The treaty is the Proposition both parties hold a live `commit` to.** Breaking it is `repudiate`,
> which is `T-m` and needs no verb of its own. **Every rejected offer stays in the log, authored and
> dated** — so *what he offered in the spring* is a fact somebody can produce later, and a party who
> improved his terms after a defeat did so where witnesses could see.
>
> ⚠ **And a multilateral treaty does not work.** `disposal: mutual` is defined over **two** parties.
> A peace conference among five is `P-15`'s counted-threshold problem, and calling that *"a ruling on
> whether majorities are wanted"* understated it — **it is a coverage bound on conclaves, votes,
> majority verdicts and multilateral peace at once.** Regraded.

### **"Is it true that this occurred"** — a HOLDS matter at the conjecture rung
The purest forensic case. **It moves by `tell`** — a party transmits a claim they hold, and by the
fifth obstacle term (`06_RESOLUTION.md` §C.1) **what has been told so far in this run lowers the
obstacle for a speech resting on it.** The mirror test bites here and nowhere else: a probable sign
the other party can run back leaves the obstacle where it was.

⭐ **And this is the rung where `AX-2` is worth the whole design.** Nobody in the room knows whether it
occurred. **The engine does not adjudicate it either** — what the bench ends up holding is what the
claims deposited in *their* ledgers say, and those came from people who may be lying, misremembering,
or repeating a `chronicle` at third hand.

### **"What should we do about the possibility of invasion"** — an OUGHT matter, deliberative, no ladder
`proofs: []` is not an oversight: *the future admits no witnesses.* **There is no fact to descend
from.** What moves is what the bench holds **right**, which is `convictions × alignment`, and the
speeches are amplification and the weighing of advantage.

⚠ **AND *"THE POSSIBILITY OF"* IS DOING REAL WORK THAT THIS DESIGN CANNOT YET CARRY.** A matter about
a *possibility* needs somebody to hold a claim that the possibility is live — and **a claim about a
future state has no producer**: WITNESS deposits from Events, and the invasion has not happened.
**The lawful shape is that somebody `utter`s a HOLDS Proposition asserting the threat and others
commit to it or do not** — belief as commitment, exactly as `§D.1.1` rules — **but nothing in this
design or the chain writes the `commit` that would make a person's fear legible to a bench.**
Registered `P-24`, and it is the sharpest thing this question surfaced.

---

# PART B · HOW THE WORLD GETS IN — eight nouns, eight carriers, none of them new

| Jordan's word | its carrier | how it reaches a proceeding |
|---|---|---|
| **events** | `Event`, in the one log, carrying no actor and no target | → WITNESS → claims in ledgers → a **question** → a Candidate |
| **facts** | `Claim(holder, subject, predicate, value, when, source, confidence, visibility)` | **the only currency there is.** Produced at a hearing by `tell`, and out of it by the `FI` lane's investigation acts. ⚠ **`visibility` IS INERT** — one occurrence in `shape.py`, the declaration, with no writer and no reader (`18_FINDINGS.md` correction, `19_PLAN.md` step 21) |
| **pressures** | `Sensation(subsistence, standing)` — the two scalars a person feels | a question source: a **need** raises a candidate |
| **clocks** | `Date`, wound by an act (`T-c`), matured by MATTER citing the act that wound it | ⭐ **this is how a proceeding CONVENES.** A date fires; CALENDAR appends a `DocketItem`; nothing is decided |
| **issues** | the matter — a `Proposition`, uttered by somebody | `open_case`, which declares the stages and their terms |
| **concerns** | a `Question`, from one of four ordered sources — **including a standing ambition** | what makes a person form a Candidate at all |
| **demands** | `petition` (a live verb) · `oblige` · a summons, which is `issue` | a petition filed is a matter somebody must docket |
| **impositions** | `issue` a dispensation · `levy` · `oblige` · a `Tenure` a determination opened | **what a proceeding produces**, and `AX-6` makes every one of them closable |

> ### **THE SUBSYSTEM ADDS NO CHANNEL. IT IS A CONSUMER OF ALL EIGHT, AND A HEAVY PRODUCER OF THE
> ### SECOND.**
> One occasion, many witnesses, many deposits — **a proceeding feeds the epistemic layer harder than
> anything else in the game.** That is `L-3` in `10_LOOPS_AND_GAPS.md`, signed `+`, bounded by claim
> decay and ledger eviction, **and this design adds no bound of its own and should not.**

## B.1 · The one thing that has no carrier, said plainly

**A proceeding cannot be raised by a fact.** Facts raise *questions*, questions raise *candidates*,
and a person must then act. **There is no path from "the granary is empty" to "a hearing happens"
that does not go through somebody deciding to convene one** — which is `AX-1` working, and it means
**a world where nobody convenes anything has no proceedings**, however bad things get. Whether that
is right is a play question; it is not an oversight.

---

# PART C · WHAT A PERSON BRINGS — four kinds of bias, and only two are fields

Answered in full at `06_RESOLUTION.md` PART A; the mapping to Jordan's four words:

| Jordan's word | carrier | how it changes behaviour |
|---|---|---|
| **allegiance** | ⭐ **`commit` edges to a faction's Proposition** — a Query, never a field | who counts as a party; who a person will not speak against; and it is **visible to others only through what they were witnessed doing** |
| **ethical convictions** | **`Person.convictions`** — weights over the closed axes, four of thirteen named (`H-46`, ruled open) | `score()` sums `convictions × alignment` inside `choose`. **This is the NPC's whole decision, and it already runs** |
| **influences** | **`Claim.source`** — who told you, and how long ago — plus `Person.stance` toward particular subjects | a person who believes a thing *because Aldric said so* holds a different row from one who saw it |
| **ambitions** | ⭐ **a question source.** *"An NPC with a standing ambition and a quiet season forms no candidates at all"* without it | it is what makes somebody turn up to a hearing that does not concern them |

| **knowledge** | carrier |
|---|---|
| **how much** | the size of the ledger, **capped**, with eviction ranking on `(confidence, recency)` — so **a person forgets what they have not used** |
| **from what perspective** | ⭐ **the channel that minted it.** `co_located` → firsthand **with attribution** · `document_key` → *that it changed, and not who changed it* · `chronicle` → `told_by`, at the teller's confidence · `post_remit` → `inferred` |
| **whether it is true** | **nothing marks it.** `AX-2` — *a false conclusion is indistinguishable from a true one to the person holding it* |

> ### **SO A BIASED ADJUDICATOR NEEDS NO FIELD, AND THAT IS THE DESIGN'S BEST SINGLE RESULT.**
> They are a person **whose claims came through a channel that could not carry attribution**, or from
> somebody with a stance, **and whose convictions weight the axes differently from their
> neighbour's.** The bias is real, it changes the finding, **nobody can read it off them, and nothing
> stores it.**

---

# PART D · THE HONEST HALF — why none of this reaches a choice today

**Everything in Parts A–C is a carrier that exists. The question Jordan asked is whether it
*affects behaviour*, and the measured answer at this commit is no.**

| the edge | state | the measurement |
|---|---|---|
| world → belief | **present, wrong payload** | 339,804 claims deposited, carrying **event-kind predicates** |
| ⭐ **belief → decision** | ⚠ **RETRACTED 2026-09-06 — SEE BELOW. The reader is LIVE; the WRITE into its namespace is not** | ~~`belief_contradicts` fires only on `predicate ∈ PERSON_PREDICATES ∧ value is False`. Over **4,800** claims the vocabularies are **disjoint** and **zero** are falsy~~ — **that describes DELETED CODE** |
| outcome → magnitude | **absent** | **0 acts** have ever resolved at a degree; 12 of 12 interpersonal verbs are degreeless |

> ### ⛔ **RETRACTION, 2026-09-06 — THE SEVERANCE MEASUREMENT ABOVE WAS STALE WHEN THIS FILE QUOTED IT.**
> Found by the antagonist stage of the playability relay, which refused to take the row on trust and
> read the code; **verified by hand afterwards, because a retraction of a measured claim is not
> something to delegate.** Full account at `17_PLAYABILITY.md` §C.2.
>
> `shape.py:3834-3843`, the docstring of `belief_contradicts`, **naming its own previous version**:
> *"⚠ `W-A`: IT ASKS THE VERB'S OWN TYPED CELL, NOT A ROSTER. **The previous version filtered on
> `predicate in PERSON_PREDICATES and value is False`** … `H-116` then measured the consequence: over
> 4,800 deposited claims the two vocabularies were DISJOINT … **The predicate is DERIVED from the
> form now** … so there is one namespace and **the write side has a name to aim at.**"*
>
> **The row above reproduced the `H-116` measurement of the implementation `W-A` replaced, and
> presented it as the current state.** That is `06_RESOLUTION.md:185-189`'s own named defect — *a fact
> about the tree stated as timeless* — committed in the directory that names it. **`shape.py:1265-1274`
> records a firing:** seed 0, NPC-088, mode `actor`, 2026-09-04 — a ledger claim made a person
> **decline `tell` for a season** on a belief the fold would have admitted.
>
> ### **THE CORRECTED STATE, WHICH IS NARROWER THAN "THE LOOP IS LIVE" AND BETTER THAN "SEVERED".**
> **The reader is live and aimed at a named namespace.** The **write** into that namespace is unbuilt,
> and the same docstring declares it a separate item — *"`H-116`'s other half — WITNESS depositing
> claims in that namespace — is not this item."* And the one recorded firing is on `claim.held`, a
> self-referential predicate the surrounding comment is **in the act of excluding**.
>
> ⭐ **So provocation is still not runnable today — but it is blocked on a WRITE that a rostered arm
> can supply (`observation_deposit_modes` : `none / actor / total`), not on a vocabulary mismatch that
> no arm could fix.** That moves the ceiling this directory placed on itself: **every "measured-severed"
> statement about `H-72` in this directory and in `relay/B_AGONIST_CONVERSIONS.md` is withdrawn**, and
> the paragraphs below — written under the old reading — overstate the block accordingly.


⚠ **AND THE DESIGN'S OWN WORKED EXAMPLE IS ONE TYPE MISMATCH FROM RUNNING.** `opening_set`'s docstring
describes the loop as working — *"a person who wrongly believes the granary full still forms the
Candidate, acts, and gets `transfer.refused` from the fold"* — and **the fold does deposit that
refusal. Nothing can read it.**

> ### **WHAT THIS SUBSYSTEM CONTRIBUTES TO THAT, AND IT IS NOT A FIX.**
> It is **the first producer of a margin**, so it closes *outcome → magnitude* for one verb. It
> **deposits more claims than anything else in the game**, so it makes *world → belief* matter more.
> **It does nothing for the severed edge**, which is `H-72` / `F.24` — typing `requires` so a belief
> can reach a decision — and which the chain's own measurement puts **ahead of all five** of its
> registered root causes.
>
> **So the correct reading of this whole directory is: a consumer built against a channel that is
> currently closed.** That is worth building — the corpus wants belief/knowledge in **58** cases and
> social/speech in **31** — but a reader who takes it as *"proceedings will make characters act on
> what they believe"* has the causation backwards. **`H-72` makes that true. This makes it visible.**

---

# PART E · THE GOVERNING TEST — **about the world, enacted by characters of the world**

> ### **JORDAN, 2026-09-06:** *"This subsystem and its games must be ABOUT the world and enacted by
> ### characters OF the world."*

**This is a ruling and it binds every row.** It is also the sharpest thing said about this design,
because the failure mode it names is the one a formal derivation drifts into on its own: **a
structurally impeccable shell in which persons-with-edges contest propositions-with-moods and nothing
in the world moves.** Stated as two questions every game must answer:

> **1 · WHAT IN THE WORLD DOES THIS GAME CHANGE?** A disposal must write a thing somebody can lose —
> a holding, a seat, a duty, a life, a document, a bond. **If the answer is "how people feel about
> each other", it is not a game in this structure.**
>
> **2 · WHY IS EACH PERSON IN THE ROOM?** Because of what they **hold** — a seat whose remit reaches
> the matter, a stake in the thing disputed, a kin bond, a standing ambition, a duty that brought
> them. **If a participant could be swapped for any other person without changing anything, they are
> not a character of the world; they are a slot.**

## E.1 · The test run over all twelve — and it fails two of them

| game | **1 · what changes in the world** | **2 · why these people** | |
|---|---|---|---|
| **negotiation** | an `oblige` opened — a duty one of them now owes | **they hold the things being traded** | ✅ |
| **arbitration** | an `oblige`, and the arbiter was **named in the opening act's terms** | the parties chose the arbiter; that choice is a prior game | ✅ |
| **legal trial** | a `hold` closed, an `oblige` imposed, a life | the bench by **remit and purview walk**; the parties by stake | ✅ |
| **tribunal** | as above | the bench sits by **office**, so it is there whether or not it cares | ✅ |
| **inquisition hearing** | a `commit` severed, an `oblige` imposed | the accuser **sits**, which is why it is what it is | ✅ |
| **excommunication** | ⭐ **a `commit` severed** — and with it the person's eligibility for every seat that body confers | the bench by remit; **the subject is absent because they did not travel** | ✅ |
| **parliamentary debate** | ⚠ **a dispensation issued or a levy raised** — see E.2, the row was mistyped | members by seat; petitioners by stake | ✅ *(once typed)* |
| **council of state** | as above | as above | ✅ |
| **audience / embassy** | a dispensation, a grant, a refusal — **and a relation settled by the ceremony** | one hearer by rank; the envoy by whose message he carries | ✅ |
| **appeal to authority** | ⭐ **a prior Tenure closed** — the finding below is undone | a bench whose remit **reaches** the first bench | ✅ |
| **interrogation** | ⚠ **`disposes: standing` — WHICH IS NOTHING.** See E.2 | the questioner by custody or office; the subject by being held | ⚠ **FAILS 1** |
| **public debate** | ⚠ **`disposal: none`. Nothing changes.** See E.3 | anyone who came | ⚠ **FAILS 1** |

## E.1a · ⭐ THE TEST HAD A THIRD QUESTION AND NOBODY ASKED IT (Jordan, 2026-09-06)

**The two questions above are the right two and they were answered honestly. A third belongs beside
them, and its absence was an accident rather than a decision.**

> **3 · WHO LEARNS THAT IT HAPPENED?** A disposal that changes the world and that **nobody outside
> the room is told about** compels the people it binds and lets none of them react. **If the answer
> is "whoever happens to carry the document", the game has no public.**

> **Jordan:** *"the outcome of a closed parliament may have epistemic impacts on those who
> participated, but the decisions made therein still get announced to the world as the parliament's
> decision, which means state change and propagation."*

**The state half of §E was already right and is not in question.** A parliament writes a `Record`
somebody carries, burns or defies; a negotiation writes an `oblige`; an excommunication severs a
`commit`. None of it runs through belief — **the reeve collects the levy because the document exists
and he holds a duty, not because he heard the debate.**

⚠ **What was missing is the knowing, and `grep -rn "announce"` over this whole directory returned one
phrase — *"a concession that was not announced"* — which is about the ARGUING.** There was no
announcement of anything, ever. So a ruling that bound a duchy was known to whoever sat in the room,
and **the people it compelled could be compelled by it and could not react to it**: nobody petitions
against a levy they never heard was raised.

**Closed by `disposal_reach`** — `03_PARAMETERS.md` §B.7, mechanism at `08_SEAM.md` §D.3. It is not an
act (so `AX-1` is untouched) and adds no Event kind: **the reach is a property of the disposal**, and
the disposal's existing emission scopes by it instead of by who was present.

## E.2 · `disposes: standing` is not a disposal, and two rows used it

**Standing is *"the gap between what everyone reads off you and what you hold"* — a Query, season-local,
owned by nobody, stored nowhere. A finding cannot write it.** A published draft nonetheless gave
`disposes: standing` to the interrogation and the public-debate rows, and `disposes: issue` — **a verb
name** — to the parliament and audience rows. **Both are outside the key's declared domain, and the
loader would refuse all four.**

| row | was | is |
|---|---|---|
| **interrogation** | `disposes: standing` | ⭐ **`disposes: <tenure>`** — what an interrogation is *for* is a confession or a charge, and both are things: a claim `tell`-ed into every ledger present, and an `oblige` or a case that follows. **The standing loss was never the disposal; it was the by-product** |
| **parliament · council · audience** | `disposes: issue` | **`disposes: Record`** — a dispensation is a **document**, carried, forgeable, burnable, obeyed by `comply` or defied by `evade / defy`. *A parliament that resolves and produces no document has changed nothing* |
| **public debate** | `disposes: standing` | **removed — see E.3** |

⭐ **AND THE PARLIAMENT CORRECTION IS THE ONE THAT MOST REPAYS THE RULING.** *"Deliberative bodies
decide the future"* is abstract; **a parliament producing a Record that a person must carry to a
place, that another person may burn, and that a third may defy, is about the world.** Nothing new is
needed for any of it — `create_record`, `carry`, `destroy_record`, `forge`, `comply` and
`evade / defy` are all live rows.

## E.3 · The public debate is not a twelfth game — it is what a proceeding degenerates to

**Under the ruling, `disposal: none` cannot stand.** A game whose only output is how people regard one
another is **not about the world**, and dressing that up as *"standing is an input to every other
game"* does not save it — an independent pass established that the eligibility half of that claim is
**false by this design's own verb rows**, since every relevant verb is `eligibility: ["own"]` and
`04_VERBS.md` forbids gating speech on standing by name.

> ### **SO THE CATALOGUE IS ELEVEN GAMES AND ONE DEGENERATE CASE, AND SAYING SO IS BETTER THAN
> ### KEEPING TWELVE.**
> **A public debate is what happens when a `speak` finds no bench**: an occasion, witnessed, at which
> claims are deposited into every ledger present and **nothing is disposed of.** That is a real and
> valuable thing in the world — *it is how what people believe gets changed at scale* — but it is the
> **absence** of a disposal rather than a kind of one, and it needs no row.
>
> ⚠ **What this costs is real and is charged here:** the design loses its answer to *"why would anyone
> attend a debate?"* The honest replacement is narrower — **you attend to put claims into ledgers**,
> which is the same reason anyone `tell`s anything, and it is worth a scene only when the people in
> the room are people whose beliefs matter. **That is a better answer than the one it replaces,
> because it names who those people are.**

## E.4 · What the ruling forbids, stated so a later session cannot drift back

| forbidden | because |
|---|---|
| a disposal that writes only a Query | a Query is stored nowhere; nothing was lost and nothing can be recovered |
| a proceeding whose stakes are internal to it | **the game must be about the world.** Points, momentum, a debate score — each is a stake nobody outside the room can feel |
| a participant who is in the room by the arrangement's say-so | **the arrangement never declares a cast** (`03_PARAMETERS.md` §C.1.1). Who is there is who travelled, and they travelled because of what they hold |
| a matter with no referent | *"who owns this settlement"* names a settlement. **A matter that names nothing cannot be disposed of** |
| an outcome nobody can be told about | if no channel mints a claim from it, **it did not happen to anybody** |

> ### **AND THE RULING IS ALSO THE ANSWER TO THE NERS `N` ATTACK THIS DESIGN COULD NOT BEAT.**
> `11_NERS.md` grades **N narrowed** because the top-down attack — *"delete proceedings and the
> strategic layer still runs"* — partly lands. **Under this ruling the answer sharpens: proceedings
> are the only route by which a holding, a seat, a duty or a bond changes hands WITHOUT FORCE.**
> Delete them and every disposal in the game is a `kill / wound` or a `revoke` by somebody who already
> had the power. **That is not a game with a political layer; it is a game with a military one.**
