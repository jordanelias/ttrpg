# 00 · THE DERIVATION — what a proceeding is, derived with the tree closed

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Method: `04_CODE_ARCHITECTURE.md` PART G. Derived from the six axioms and the study; the executable
## chain was opened only to check that each shape is expressible in it (`§G.4.6`).
## ⚠ **This file is one of TWO independent derivations.** The second was produced by a read-only
## Fable 5.1 synthesis under the same brief and with the same scope ban. `11_ADVERSARIAL.md` records
## where they converged, where they disagreed, and which won.

---

# THE FRAMING, RULED BY JORDAN 2026-09-05, AND THE VOCABULARY IS HIS

> **"The subsystem is a game structure, which means that it hosts the parameters, logic, processes,
> mechanics, actions, roles, venues, etc and then the games within it are the negotiation,
> parliamentary debate, tribunal, etc which are just defined parameters."**

**So there are two things in this directory and they must never be confused.**

| | | owns |
|---|---|---|
| **THE GAME STRUCTURE** | the host. Parameters · logic · processes · mechanics · actions · roles · venues | **nothing** — it is a seam provider, and `§A.2` gives it no token |
| **A GAME** | an instance: a negotiation, a tribunal, an inquisition hearing | **nothing** — it is a row of parameter values |

**This raises the bar rather than lowering it.** If a game is *just defined parameters*, then **every
difference between two games must be locatable in the row**, and a difference that will not fit is a
defect in the parameter set, not a licence to write a branch. The twelve rows in
`03_ARRANGEMENT.md` are the proof obligation, and §5 there discharges it twice — once by authoring a
thirteenth game the study never describes, and once by naming a game this structure **cannot** host,
because a parameter space with no inexpressible neighbour has not been bounded (`G.1.4`).

**The vocabulary is Jordan's and is used unchanged** — *game structure* for the host, *game* or
*proceeding* for the instance. No synonym is coined (`CLAUDE.md` §4; the `evacuate` corpse).

---

# THE ONE SENTENCE

> ## **A PROCEEDING IS AN OCCASION AT WHICH PERSONS ADDRESS PERSONS WHO MAY DISPOSE OF A MATTER.**
>
> **The matter is a `Proposition`. The persons who may dispose of it are the holders of seats whose
> remit covers it at that venue — a Query, not a body. Everything that distinguishes a trial from a
> negotiation from an inquisition is the RELATION BETWEEN THOSE TWO SETS AND THE SET OF PERSONS
> PRESENT.**

Three sets, all of which already exist:

```
parties  = persons who have committed to a disposition of the matter   -- `commit` edges. Owned.
bench    = holders of seats whose remit covers the matter at the venue -- Query.judging_set. Ownerless.
floor    = persons present at the venue                                -- the presence cache.
```

**And the twelve proceeding kinds are twelve configurations of those three sets**, plus what stands
between them. Not twelve mechanisms. **Nothing in the list below is a new object.**

| | `bench ∩ parties` | `\|bench\|` | subject present? | what it is |
|---|---|---|---|---|
| **negotiation** | **= bench** — the deciders *are* the parties | 0 seats; the parties decide by agreeing | yes | the pure case: nobody outside the exchange disposes of anything |
| **interrogation** | **≠ ∅, asymmetric** — one party is also the only decider | 1 | yes, and is the subject | the asymmetry *is* the proceeding |
| **legal trial** | **∅** | > 1 | yes | parties address deciders who are not parties |
| **tribunal** | **∅** | > 1 | yes | as above; the arrangement differs, not the shape |
| **arbitration** | **∅** | 1 | yes | one decider, chosen by the parties — which is a term of the opening act |
| **appeal to authority** | **∅** | 1 | usually | a decider with few constraints; and the appeal is a *nested* proceeding |
| **audience / embassy** | **∅ or = bench** | 1 | yes | one hearer, heavy staging, low candour |
| **council of state** | **⊇ parties** — the deciders argue among themselves | > 1 | yes | the parties and the bench are the same body |
| **parliamentary debate** | **⊇ parties**, and the floor is large | ≫ 1 | yes | many who must be persuaded |
| **public debate** | **∅ — the bench is EMPTY** | 0 | yes | nobody can dispose of anything; the prize is standing |
| **inquisition hearing** | **≠ ∅** — the accuser sits on the bench | ≥ 1 | yes, as subject | interrogation with a bench; the subject cannot win, only survive |
| **excommunication deliberation** | **∅** | > 1 | **NO — the subject is absent** | a body disposing of a person who cannot address it |

> ### **THAT TABLE IS THE WHOLE OF THE COVERAGE ARGUMENT, AND IT IS A TABLE OF QUERIES.**
> Every column is answered by set membership over `commit` edges, `hold` Tenures and the presence
> cache. **There is no `ProceedingKind` enum and no branch on one.** Adding a thirteenth kind — a
> guild hearing, a synod, a formal challenge — is adding a row of arrangement data, and §5 of
> `03_ARRANGEMENT.md` demonstrates it on a kind the study does not describe.

---

# PART A · THE DERIVATION, AXIOM BY AXIOM

Each axiom forces something, and taken together they leave very little freedom. That is the test:
**a derivation with many free choices has not been forced by anything.**

## A.1 · `AX-1` — only a person acts. **So there is no tribunal.**

A court does not convict; a bishop does. A parliament does not resolve; the members who commit do.
**This is not a restatement of the axiom — it is what fixes the object model**, because the tempting
design here is a `Proceeding` carrier that holds a phase, a docket, a vote tally and a verdict, and
every one of those four is a value with no single owner.

Run `00_THE_METHOD.md`'s question 1 over them:

| candidate value | who owns it? | verdict |
|---|---|---|
| the proceeding's **phase** | **nobody** — it is a fact about a set of persons' acts | ⚠ a defect if stored. It is **the ladder rung the matter has reached**, which is a property of the *matter* and is written by the act that descends |
| the **docket** — what is to be heard | the **occasion**. A `Date` fires and CALENDAR appends a `DocketItem` — `shape.py:5363-5381` | **already exists.** Not ours |
| the **vote tally** | **nobody.** A tally across holders is `T-a`'s worked case: *"a per-person tally summed across holders has no single owner, so `AX-4` refuses it directly"* | **a Query over the bench's `commit` edges.** Never stored |
| the **verdict** | the **seat-holder who determined it**, through `Act.via` | a `Tenure` the determiner opened, closable by `T-o`. **`AX-6` satisfied: every verdict has an author and is therefore contestable** |
| the **record** of the proceeding | whoever **carries** it | a `Record` — forgeable, burnable, held. **Already a kind** |
| who may speak, and in what order | the **arrangement**, which is data read at load | a row, not state |

> **Nothing survives as a carrier.** The proceeding has a phase nobody owns, a tally nobody owns, a
> docket that already exists, a verdict owned by its author, and a record that is already a `Record`
> kind. **A `Proceeding` object would be five values with five different owners wearing one type's
> clothes** — `G.2.1`'s *"you can name two"* firing five times.

## A.2 · `AX-2` — no privileged access. **So there is no view of the room.**

The tempting design gives each participant a "read of the room" — the bench's current leaning, the
opponent's reservation point, the odds. **Every one of those is world truth inside a decision, and
`T-f` makes it unspellable: `choose` receives a `PersonInterior` and no `World`.**

**What the study says about this is the strongest possible endorsement, and it arrives from the other
direction.** `S5`: *the read is made, not taken.* Instructed perspective-**taking** raised confidence
without raising accuracy across twenty-five experiments; what improved accuracy was perspective-
**getting** — being allowed to ask. **The one capacity with positive evidence behind it is the one
that requires an ACT.**

> ### **SO `AX-2` DOES NOT COST THIS SUBSYSTEM A MECHANISM. IT SUPPLIES ITS BEST ONE.**
> A participant who wants to know the room must **act on it and observe what returns** — which is an
> act, at a venue, that other people can see, that costs part of the occasion, and that can be
> misread. **Elicitation is a verb because the axiom refuses the alternative.** A design with a
> room-reading stat would have made the corpus's one evidenced capacity into a passive number.

## A.3 · `AX-3` — true ≠ right. **So a proceeding has two tracks, and the ladder is what keeps them apart.**

This is the derivation the design turns on.

`AX-3` says **evidence moves what is held true; argument and consequence move what is held right**,
and that letting either move the other is *"the single most dangerous collision in the design."*

**A proceeding is the one place in the game where both are moved in the same room, at the same
occasion, by the same people.** So it is the place where the collision will actually be attempted —
and a subsystem that does not separate them will produce exactly the failure `AX-3` names: finding a
document would change what a person believes is *right*, and the moral layer would collapse into a
second epistemic layer.

**The study already contains the separator, and did not know it was one.** The issue ladder (Fig. 5)
is Quintilian's doctrine of *status*, and read against `AX-3` it is a **procedural declaration of
which track is live**:

```
  PROCEDURAL OBJECTION   is this bench competent to hear it?
                         → NEITHER track. A Query over remit. Cheapest win; signals evasion
  ─────────────────────────────────────────────────────────────────────────────
  CONJECTURE             did it happen?
                         → THE EVIDENTIARY TRACK. Moves by claims. `tell` is the act
  ─────────────────────────────────────────────────────────────────────────────
  DEFINITION             what is it called — theft or sacrilege, gift or bribe?
                         → THE HINGE. An uttered Proposition naming the act, which
                           people then commit to or refuse. Both tracks touch here
  ─────────────────────────────────────────────────────────────────────────────
  QUALITY                justified · excused · transferred · mitigated?
                         → THE NORMATIVE TRACK. Moves by argument against convictions.
                           Evidence is spent; what remains is what the bench holds right
```

> ### **THE LADDER IS `AX-3` MADE PROCEDURAL, AND THE DESCENT IS THE MECHANISM.**
> Descending from conjecture to quality is descending **from what is true to what is right.** And the
> corpus's own rule about the descent — *"it is descended only when forced, because every descent is
> visible and is read as a concession not announced"* — is not flavour. **It is the cost of moving
> the contest from a track you are losing to a track you might win.**
>
> **And the cost needs no rule to enforce it.** A descent is an act at a venue; WITNESS fans it out;
> every person present deposits a claim that the descent happened. **The concession is visible
> because it was witnessed** — `AX-2` supplying the enforcement `AX-3` needs. No `concession_penalty`
> field exists anywhere in this design, and none is wanted.

⚠ **AND `AX-3` FORBIDS THE OBVIOUS SHORTCUT, WHICH MUST BE NAMED SO IT IS NOT TAKEN LATER.** It is
very tempting to give the bench a single scalar — *conviction that the accused is guilty* — that
evidence and argument both push on. **That is one quantity that both measures and decides, which is
`G.1.5`'s exact signature**, and it is the collision `AX-3` calls the most dangerous in the design.
The two tracks are two different stores: claims in a ledger (INTERIOR, written at WITNESS) and
commits to `OUGHT` Propositions (ACTS, written at RESOLVE). **A step holding one token cannot reach
the other**, which is `§A.1`'s module split doing the work.

## A.4 · `AX-4` — one owner, one writer. **So the bench is a Query and the record is a Record.**

Covered at A.1. The one addition: **`Query.judging_set` already exists and already raises**
(`shape.py:3161-3163`, law text *"NOTHING IS DECIDED AT A SITTING"*). `04_CODE_ARCHITECTURE.md` §B.7
says what it should be: *"the seats whose remit covers the matter at that venue — a Query over seats,
which are arrangements of the political layer, not a rule stored on a place."* And §A.3 row 7 records
that `Rung.judging_set_rule` was **deleted** for being decision-shaped state on a container.

> **So the bench is not something this design invents. It is a Query the architecture already
> specified, that the executable chain registers as `absent` (`H-32`), that sits on the chain's own
> critical path (`W26`), and that nothing has yet written.** This subsystem's first deliverable is
> that function.

## A.5 · `AX-5` — three motions. **So a proceeding never advances by itself.**

No phase timer. No "the debate moves to the second reading after N turns." **Every step of a
proceeding is somebody's act**, and a proceeding that nobody advances simply does not advance —
which is `T-c`'s dividend: *"a wound clock can be bribed, delayed, burned, or killed."*

**What ends a proceeding that nobody is advancing?** `T-n`: **the opening act declares its terms.**
`open_case`'s `requires` is already *"the act DECLARES the stages and their terms"* — which §F.24a
correctly classifies not as a predicate at all but as **a constraint on the well-formedness of the
Act**, refused at construction. So a summons has a return day; a term of service on a commission has
an end; a stay of proceedings has a length. **MATTER matures what an act wound, citing the act that
wound it.** Bribe the clerk who set the return day, burn the record that carries it, or reach the
person who must renew it.

⚠ **AND THE TRACER CANNOT SPELL THIS TODAY.** `Tenure` has no `term` field (`shape.py:2066-2091`
carries `degree` and `payload`, no `term`). `T-n` is specified in Stage 1 and unbuilt in the chain.
**Registered, not assumed** — see `08_LOOPS_AND_GAPS.md` row `P-04`.

## A.6 · `AX-6` — nothing permanent without an author. **So every verdict is appealable, and the appeal is the nesting.**

A verdict that no act can undo is a state nobody chose to make final. So:

| what a proceeding can produce | how it is closed | by whom |
|---|---|---|
| a **finding** — the matter's disposition | a later `determine` at a bench whose remit reaches it | **the appeal** |
| a **censure** or **excommunication** — a Tenure the determiner opened | `T-o`, the seat's revocation basis, through `Act.via` | a seat that may revoke |
| an **obligation** imposed — an `oblige` edge | `release`, eligibility `own` | **the person who swore it** |
| a **treaty** — mutual `commit`s to a Proposition | `repudiate`, `T-m` | **each committer, separately** |

> ### **AND THIS IS WHERE THE APPEAL FALLS OUT WITH NO MECHANISM.**
> `02_HIERARCHIES.md` §B.2: *a contest is the season loop nested — the same steps over a smaller
> person set on a shorter clock*, bounded by **nothing intrinsic**, therefore requiring a
> **caller-supplied depth cap with no default**, returning a **typed refusal** at the cap.
>
> **An appeal is a proceeding whose matter is the disposition of a prior proceeding, before a bench
> whose remit reaches the first bench.** That is process-nesting, exactly as specified, and the depth
> cap is what stops an infinite appeal chain. **`seam.contest` already takes `depth` and `max_depth`
> and already returns `Refusal(depth_cap)`.** The mechanism is built; nothing has fed it.
>
> ⚠ **The cap is the CALLER'S, always, and a default is a fabricated constant** (`H-87`). Who is the
> caller? Per `02_HIERARCHIES.md` §E.1, *"what a contest's depth cap should BE at a given venue is a
> property of the act that opens one, and `T-n` says the opener declares its terms."* **So the number
> of appeals a matter admits is declared by the act that opened the case** — which is a term a
> constitution sets, a jurisdiction varies, and a party can litigate. **The exhaustion of appeals is
> a game mechanic, not an engine limit.**

---

# PART B · WHAT THIS ADDS, AND WHAT IT MAKES UNNECESSARY

`03_VERBS_AND_LOOPS.md` §F.1: *"None of them added a primitive… A meta-architecture that answers
questions by growing the vocabulary has not found the shape — it has renamed the problem."* The bar
is therefore not *did we cover the twelve kinds* but *what did we add to cover them.*

## B.1 · The count

| | what | why it is not a new primitive |
|---|---|---|
| **carriers** | **0** | `Proposition` (the matter) · `Record` (the record, the summons, the writ) · `Seat` (the bench) · `Tenure` (`commit`, `oblige`, `hold`) · `Person` · `Rung` (the venue) · `Date` (the occasion) · `Act` · `Event` · `Claim`. **Every one already rostered** |
| **fields on existing carriers** | **1, and it is contested** | `Proposition.rung` — the ladder rung a matter has reached. See B.2, where it is argued *against* and then admitted with its price |
| **Queries** | **3** | `judging_set` (**already specified, already registered as `H-32`, already on `W26`**) · `latitude` (derived from the interposition set) · `standing` (**already defined in the design as *the gap between what everyone reads off you and what you hold***) |
| **verbs** | **4 new, 6 reused, 1 filled** | `05_PARAMETERS_AND_VERBS.md` §3 |
| **edge kinds** | **0** | `commit` and `oblige` carry everything |
| **Event kinds** | 9 | all declared as columns; none minted in a body (`F.20b`'s defect not repeated) |
| **rosters** | 5 closed sets, in data | ladder rungs · interposition kinds · genre · register · standing route |

## B.2 · The one field, argued against before it is admitted

**`Proposition.rung` — the issue-ladder rung the matter has reached.**

**What was tried first, and why each failed:**

| candidate | failure |
|---|---|
| a **Query** over the acts so far | it is not derivable. Two people can descend to *quality* by different routes and the log does not say which rung is live now — it says which descents occurred. **A Query that must pick among histories is a resolver making a decision, which is `T-b`** |
| a field on the **venue** (`Rung`) | `§D.2`'s NEVER — decision-shaped state on a container. This is exactly `judging_set_rule`, deleted for this reason |
| a field on the **`Act`** that descended | an Act is not a carrier of ongoing state; the next actor would have to search the log for the most recent descent, which is the Query above |
| a field on the **case `Record`** | ⚠ **this is the live alternative and it is close.** A `Record` is carried, forgeable and burnable — and *burning the record of what has been conceded* is a superb mechanic. **It is rejected only because a matter can be proceeded on with no record at all** (an audience, a public debate), and a field that exists only when a document does is a field whose absence has no meaning |

**Admitted, with its price stated:** `Proposition` is declared **immutable** (`§D.5`: *"OWNS nothing.
It is unowned because nothing may change it"*), so **a mutable rung on it is a category error by the
schema's own admission test.** The resolution is that the rung is **not on the Proposition** but is a
`Tenure` of kind `commit` from **the case's opener to the matter**, carrying the rung in `degree` —
the field that Stage 4 `F.4` calls *"a field with a writer and no reader"* and that `ID-13` is about
to delete.

> ### **SO THE ONE FIELD THIS DESIGN NEEDS IS A FIELD THE DESIGN ALREADY HAS AND IS ABOUT TO THROW
> ### AWAY FOR WANT OF A READER — AND THAT IS THE STRONGEST RESULT IN THIS DOCUMENT.**
> `Tenure.degree` is written by `determine` (`verb_table.yaml:174`) and read by nothing. `F.4` names
> it as `G.1`'s standing falsifier: *"a field the admission tests admit that the game needs refused,
> or refuse that it needs admitted."* **This subsystem is its reader.** Either the field stays and
> proceedings work, or the field goes and this design must find another home — and **that is a
> falsifiable claim, testable today, by deleting the field and seeing what breaks.**

## B.3 · What it makes unnecessary — the deletions this earns

`00_THE_METHOD.md`: *"A primitive earns its place by what it makes UNNECESSARY."*

| no longer needed | why |
|---|---|
| **an `obstruct`-shaped rule for the floor** | two people reaching to speak at one occasion is `T-g` at a venue. The second is refused by the fold and **the refusal emits** — which is the interruption, witnessed, with nobody having a verb for it |
| **a reputation or influence meter** | standing is the gap between what is read off you and what you hold — a Query, season-local, owned by nobody. `T-a` |
| **an "interposition" mechanism** | an advocate absorbs defeat because **consequences attach to the actor, not to a side** (`AX-1`). Fig. 24's headline property costs zero lines |
| **a per-genre resolver** | the genre is a property of the *bench's remit*, not of the speech. A verb that mismatches it is **refused**, and the refusal emits |
| **a vote-counting subsystem** | a tally over holders has no owner (`T-a`). What the bench "decided" is the `determine` acts its members took |
| **a separate `Verdict` type** | a verdict is a `Tenure` its determiner opened. `AX-6` then gives the appeal for free |
| **a "the room is hostile" scalar** | hostility is what the bench holds — claims and commits — and it is unreadable from inside a decision by `AX-2`. **What replaces it is elicitation, which is an act** |

---

# PART C · THE THREE QUESTIONS, ANSWERED FOR THE SUBSYSTEM AS A WHOLE

`00_THE_METHOD.md` requires all three to be answered cleanly, and says that failing one **locates the
problem** rather than merely being a gap.

### 1 · Who owns this?

**Nothing. The subsystem owns no state whatsoever, and that is the contract.** `§A.2`'s module table:
`seam/wrappers/*` owns *"nothing, ever"*, reads *"the projection"*, emits *"a `Margin`"*, holds **no
token**. A proceeding therefore cannot write; it **reports**, and the fold applies the writes through
the gate at the degree the ladder read.

⚠ **The one exception in the tree is `(Person, coherence)`, the single matrix row whose write the gate
licenses to a `driver="Seam"`** (`shape.py:2829-2836`). `02_THE_SOCKET.md` §3 sets out why that
socket exists and why it is currently a deletion candidate. **This design does not take it.** A seam
that writes is a seam that has begun to own, and `§C.5`'s first leak — *a state write from inside a
contest bypasses the write rules, the witness layer and the log at once* — is graded **STRUCTURAL by
absence of a token**, which is the strongest guarantee in the seam contract. **Taking the exception
would trade a structural guarantee for a mechanical one to save a table row. It is not worth it, and
the refusal is recorded with its cost: `coherence` gets no reader from us, and `ID-13` may therefore
delete it.**

### 2 · What can check this?

| the claim | its form | grade |
|---|---|---|
| the twelve kinds differ only in data | **a loader + a falsifier** — twelve rows, and a test asserting no resolver branches on a kind name | **MECHANICAL** — the same `kind ==` scan `02_HIERARCHIES.md` §C.2 specifies |
| the subsystem writes nothing | **a type** — no token in the wrapper's parameter list | **STRUCTURAL (Python) / MECHANICAL (GDScript)** — see `07_IMPOSSIBILITIES.md` on the reference-copy divergence |
| the two tracks never touch | **a loader check** — no verb writing a conviction may phrase its `requires` over the actor's ledger (`§B.2`, `F.23`) | **MECHANICAL at load; CONVENTION until `requires` is typed (`F.24`)** |
| a bench member's decision reads their own convictions | **a falsifier** — permute the bench's convictions and the finding must move | **MECHANICAL**, and it is the sharpest test in the design |
| an appeal terminates | **a falsifier** — a chain at the cap returns `Refusal`, typed, in both languages | **MECHANICAL** |

### 3 · Whose act makes this happen?

Every one, and this is the section a proceedings design most easily fails.

| the thing | whose act |
|---|---|
| the occasion exists | the act that **set the date** — `T-n`, and CALENDAR merely fires it |
| the matter is before the bench | the act that **opened the case** and declared its stages and terms |
| the bench is what it is | the acts that **conferred those seats**, and the acts that established their remit |
| the accused is present | their own act of **moving** to the venue — or their absence, which is also theirs |
| the ladder is at *quality* | the act of the party who **descended**, witnessed by everyone present |
| the finding is what it is | the acts of the bench members who **determined**, each `via` their seat |
| the world believes it | what each witness **deposited**, per channel |

> **There is no step in this list that the engine takes on its own, and no place a narrator could
> stand.** ⚠ **One candidate is worth naming because it is where a narrator would return:** *the
> proceeding decides that debate is over.* It does not. **The occasion ends when its declared term
> matures** (`T-n`, MATTER, citing the act that wound it) **or when nobody spends another
> interaction on it.** A proceeding that everyone abandons lapses — and *a hearing nobody attended*
> is a legitimate and interesting outcome, exactly as *an undecided fight* is (Jordan, 2026-06-02).

---

# PART D · THE FALSIFIERS FOR THIS DERIVATION

`ID-11` — ship the falsifier with the claim. Each is runnable against the tracer today or names what
must exist first.

| # | claim | what would show it wrong |
|---|---|---|
| **D-1** | the twelve kinds are twelve rows | any kind requiring a resolver branch. **Test: the `kind ==` scan, plus authoring a thirteenth kind and running it** |
| **D-2** | no new carrier is needed | a value in a running proceeding with exactly one writer and no home among the rostered carriers |
| **D-3** | `Tenure.degree` is the ladder's home | delete the field and find the design unaffected — which would mean the rung belongs elsewhere and `F.4` should be closed by deletion after all |
| **D-4** | the two `AX-3` tracks stay apart | a proceeding in which producing a document moves what a bench member holds **right** rather than what they hold **true** |
| **D-5** | the advocate needs no mechanism | a case where a defeat suffered by an advocate visibly costs the principal standing **through some path other than the principal's own acts** |
| **D-6** | the descent's cost needs no rule | a witness set for which the descent is invisible and therefore free, where the corpus says it should be costly. ⚠ **This one is expected to FIRE**: a descent at a proceeding with an empty floor costs nothing. **That may be correct — a concession nobody saw is not a concession — but it is a prediction and it should be checked** |
| **D-7** | the appeal is the nesting, with no appeal mechanism | an appeal that cannot be expressed as a proceeding whose matter is a prior finding |
| **D-8** | latitude is derived, not declared | two arrangements with identical interposition sets that must nevertheless differ in latitude |

⚠ **`D-6` IS RECORDED AS A LIVE PREDICTION RATHER THAN A CLOSED ARGUMENT**, per `§G.4.1`'s added
clause: *a stage can close on representations and still be behaviourally wrong.* It is the kind of
defect that no amount of pointing at a type would find, and only a trace would.
