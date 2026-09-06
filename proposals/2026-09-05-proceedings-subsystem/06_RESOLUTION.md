# 06 · RESOLUTION — the person, the pool, the margin, and where a title enters

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

> **Jordan's two directions, which this file answers together:**
> *"They will have attributes that influence their efficacy, and convictions, ethos, stances, biases."*
> *"Characters can have titles that impact their standing and influence."*

---

# PART A · FOUR WORDS, FOUR DIFFERENT THINGS — AND ONLY TWO ARE FIELDS

**The design's first job here is to refuse to make all four into stats.** `§D.0`'s admission clause —
*what kind of assertion is this field making: DECLARED, THE CASE, or READ OFF?* — separates them
cleanly, and the separation is the mechanism.

| the word | what it is | where it lives | assertion kind |
|---|---|---|---|
| **convictions** | what a person holds **RIGHT** — weights over the closed moral axes | ⭐ **`Person.convictions`, a field that already exists** | **declared** — a person's own, moved by argument and consequence, never by evidence (`AX-3`) |
| **stances** | a person's posture toward a particular subject | ⭐ **`Person.stance`, a field that already exists**, read by `stance_toward` | **declared** |
| **ethos** | what **others** take a person to be — practical wisdom, virtue, goodwill toward the hearer | ⚠ **NOT A FIELD. It is claims in OTHER PEOPLE'S ledgers**, one per hearer, each of which may be wrong | **read off**, and read off differently by each hearer |
| **biases** | ⚠ **NOT A FIELD, AND MUST NEVER BECOME ONE** | the **divergence** between what a person holds and what is the case, plus the weights their convictions put on the axes | **neither — it is a gap**, and `§D.0` says a gap between kinds is the signature of a **Query**, not a field |

> ### **THAT `bias` HAS NO REPRESENTATION IS THE STRONGEST RESULT IN THIS FILE.**
> A biased adjudicator is not a person with a `bias: 0.4` field. **They are a person who holds claims
> that are false, and whose convictions weight the axes differently from their neighbour's** — and
> `AX-2` guarantees that *"a false conclusion is indistinguishable from a true one to the person
> holding it."* **The bias is real, it changes the finding, nobody can read it off them, and nothing
> stores it.**
>
> **What it costs to add the field instead:** a bias meter is a value with two owners — the person
> who has it and the observer who reads it — which is `G.2.1`'s *"you can name two"*, and it would
> make prejudice legible in a game whose whole epistemic layer exists to make it illegible.

⚠ **AND `convictions` IS FOUR OF THIRTEEN, WHICH THIS DESIGN DOES NOT FIX.** `rosters.yaml:145-157`:
*"#353 says 'the closed 13' and NEVER ENUMERATES THEM. `H-46` is graded `absent` for exactly that
reason and Jordan's 2026-09-02 ruling says it must STAY open."* **This design does not name the other
nine and must not.** A proceedings subsystem is precisely where a session would be tempted to invent
moral axes to make its adjudicators interesting. **`H-46` stays open; the mechanism works at four and
works at thirteen, because nothing branches on a member.**

---

# PART B · EFFICACY — the pool, and why a seat is not in it

> **`§A.2`: eligibility is never capability. Skill decides how WELL a thing goes, never whether it may
> be attempted.** And `§D.1.1`: `capability` *"supplies dice at RESOLVE and gates nothing."*

**Jordan's word is *efficacy*, and it maps exactly onto the one thing `capability` is licensed to
do.** No new attribute carrier is proposed: `Person.capability` is already a dict on the class
(`shape.py:2368`), and **which keys it carries is content by `ID-12`.**

```
pool(actor, act)  :=  capability[<the key this act draws on>]   +  the draw
```

⚠ **THIS DESIGN NAMES NO CAPABILITY KEYS AND SUPPLIES NO WEIGHTS.** The study is explicit that it
records failure *types* exhaustively and *frequencies* not at all, and that no located work supplies
numbers for these steps. **Inventing a rhetoric stat here would be the fabrication `§0.1` point 4
exists to catch.** Registered `10_LOOPS_AND_GAPS.md` `P-06`, `assumption`-grade, with an injection
site and a three-point sweep (`ID-6`).

## B.1 · Where a title enters — and it is NOT the pool

**`§A.3` is categorical: *a seat adds no verb and no modifier*, because *"the moment a seat carries a
modifier, the seat is a stat, and taking the seat becomes an optimisation rather than a political
act."*** And `§D.7`: **there is no `Title` type** — a title *is* a rank, which is the ordinal of a
seat's domain in the containment roster.

**So a title cannot make a person speak better. Jordan's direction is that it affects *standing and
influence*, and both of those are the HEARER'S side of the exchange, not the speaker's.**

| the study says | the mechanism |
|---|---|
| Fig. 1: standing determines **whether either of the other layers gets a hearing** | rank enters the **obstacle**, never the pool |
| Fig. 3: an ascribed position is **contested procedurally, before any content** — seating, order of speaking, forms of address | `arrangement.order: rank` sorts the nested run **by the ordinal**. *"Precedence is a public ruling delivered without a word"* |
| ▣ bounded by elaboration: **position dominates an inattentive room and merely tilts an attentive one** | the weight rank carries in the obstacle is scaled by how much the room is **attending**, which is a property of the arrangement |
| ▣ bounded in time: **low standing suppresses reception NOW and not reliably later** | ⭐ §D below — and it needs no mechanism at all |

> ### **SO A TITLE BUYS TWO THINGS AND NEITHER IS A BONUS.**
> **It buys ORDER** — where you are called, which at a rank-ordered proceeding is a public ruling on
> your standing before you say anything. **And it buys RECEPTION** — the obstacle your speech faces
> before hearers who read that rank off you. **Neither touches your pool, and a fool with a duchy is
> still a fool who is heard first.**

---

# PART C · THE MARGIN AND THE ONE LADDER

> **`T-k`: one resolver, one degree ladder.** `§C.5`: *the subsystem returns a **Margin**. A subsystem
> returning a winner has not met the contract.* `§E.3`: *a subsystem varies the ladder by passing a
> declared extension that can only NARROW an outcome, never widen one.*

```
margin  :=  pool(speaker, act)  −  obstacle(hearers, arrangement, rung, register)
degree  :=  ladder.degree(margin, veto = <the licence gate failed>)
```

## C.1 · The obstacle — four terms, each sourced, none numbered

| term | source | direction |
|---|---|---|
| **latitude** | Fig. 4, derived from `interposed[]` (`03_PARAMETERS.md` §B.1) | **low latitude raises the obstacle** — that is what an interposition is *for* |
| **reception** | Fig. 3 + Fig. 25 — what the hearers read off the speaker, weighted by attention | **high standing lowers it; and it tilts rather than dominates an attending room** |
| **the rung** | Fig. 5 — a lower rung is a smaller claim | **descending LOWERS the obstacle.** That is why the ladder is worth descending, and why the descent must cost something visible or it would be free |
| **register fit** | Fig. 8 — which misreading this manner invites, before this room | ⚠ **the term this design is least sure of** — `05_PROCEDURE.md` §D |

⚠ **NO COEFFICIENTS, NO WEIGHTS, NO BAND EDGES ARE PROPOSED.** `F.9` — *the ladder's margin model and
band edges* — is an open gap in the architecture itself, and `H-31` records that **nothing in the
tracer has ever produced a `net`**, so the margin-graded branch of `degree_of()` (`shape.py:6668-6679`)
is *a reader with no producer.* **This design is the first producer. It supplies the shape and refuses
to supply the numbers**, and the honest statement is that **the subsystem cannot run until somebody
rules the band edges.**

## C.2 · The veto — a demotion, and the licence gate is what fires it

`§E.3`'s extension *"can only narrow an outcome, never widen one — injected by the wrapper, never
resolved by the engine"*, and the constraint is **structural by signature**: `veto : bool`, and the
ladder takes the minimum.

**Fig. 26's four conjuncts are the veto's source.** Frankness toward someone who can be hurt by it is
a **licence**, and when it is unlicensed the speech *"is received as an attack and priced as one."*
**Mechanically: the best available band is demoted.** ⚠ **And the four conjuncts are ALSO a `requires`
with a refusal per conjunct** (`03_PARAMETERS.md` §B.4) — the difference is which act they gate. **On
a `charge` they refuse it outright; on a `speak` that shades into one they demote it.** That is a
real ambiguity and it is registered as `P-17`.

## C.3 · The bands, and why an undecided proceeding must be one of them

**Named by what the subsystem can actually distinguish, per the 2026-09-03 ruling: *the degree is READ
OFF the subsystem, never mapped onto it by the table.***

| band | what it means | writes |
|---|---|---|
| **Carried** | the matter moved as the speaker pressed it | the rung, and the speaker's stance |
| **Advanced** | it moved, short of what was pressed for | the rung |
| **Held** | nothing moved | **nothing** — and the act still emits (`§C.4`) |
| **Turned** | it moved **against** the speaker | the rung, and the speaker's stance |

⭐ **`Held` IS THE LEGITIMATE UNDECIDED OUTCOME, AND IT IS LOAD-BEARING.** `§C.5`: *"an undecided
outcome is a legitimate result, and inventing a tiebreak to fill the contract is how a refusal becomes
a fabrication."* The precedent is exact and ruled: `wrapper.fight` returns `0` and *"an undecided
fight is a legitimate outcome"* (Jordan, 2026-06-02). **A hearing that settled nothing is a hearing.**

⚠ **AND `Turned` IS WHAT MAKES THIS A DESIGN ABOUT OVERSHOOT.** The study's central finding (`S3`) is
that the named fault across seven traditions is **excess of a virtue**, not deficiency — *"a competent
thing done too hard, too soon, or too visibly."* **A ladder with no adverse band cannot express it**,
and the design would then be about how much you win by.

---

# PART D · WHAT A LOSS COSTS, AND THE TWO BOUNDS THAT NEED NO MECHANISM

**The `writes` above are the whole of the cost, and the recoverability grading (Figs. 11, 21) is what
decides which write it is.**

| grade | what it writes | why it is that |
|---|---|---|
| **FREE** | **nothing** — the unused proof, the unspent objection, the construction not needed | *"they cost nothing; the corpus holds that they are hoarded"* — an act not taken emits nothing |
| **COSTLY** | `Person.stance`, and claims into every witness's ledger | recoverable at a **visible** price — visible because it was witnessed |
| **TERMINAL** | a `Tenure` closed, or a `commit` severed | **no later step repairs it**, and no interposition absorbs it (Fig. 24) |

## D.1 · The two bounds on reception, which the study adds and which cost nothing

**▣ Bounded by elaboration.** *Position dominates an inattentive room and merely tilts an attentive
one.* **Mechanism: the weight of the reception term scales with the arrangement's attention** — which
is a property the arrangement already carries through `genre` and `latitude`. **No key is added.**

**▣ Bounded in time — and this is free in the most satisfying way.** *"Low standing suppresses
reception NOW and does not reliably suppress it LATER. A speaker with no standing may still place an
argument that outlives the discount on its source."*

> ### **THE MECHANISM IS THAT THE DEPOSIT DOES NOT DEPEND ON THE DEGREE.**
> A speech emits an Event; **WITNESS fans it out to everyone present regardless of how it went**; each
> deposits claims into their own ledger. **So a speaker who is dismissed still puts the claim into
> every ledger in the room** — and what decays afterwards is the claim's **confidence**, on `AX-3`'s
> licensed carve-out (*fading REMOVES, never REVISES*), not its content.
>
> **Nothing is added for this. It is what the loop already does**, and it means the lowest-standing
> person in the room can still change what everybody knows — which is `AX-2` paying for itself, and
> the reason a public debate with `disposal: none` is worth playing.
