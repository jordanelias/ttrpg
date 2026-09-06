# 05 · THE PROCEDURE — what is ordered, what is a map, and what is neither

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

> **`§G.2.9`, which is the criterion this file exists to apply:** *a procedure is required wherever the
> order of sub-steps changes the outcome — and nowhere else.* **Modelling a genuine procedure as a
> rate deletes the mechanism; modelling a rate as a procedure invents an order nobody authored, which
> is `AX-5`'s fourth motion arriving through the back door.**
>
> **And the criterion is its own falsifier: permute and compare.**

---

# PART A · THE PERMUTATION TEST, RUN OVER EVERY PART OF A PROCEEDING

| the part | permuting it changes the outcome? | therefore |
|---|---|---|
| **who speaks, in what order** | ⭐ **YES, and it is the whole of some games.** Roman senators called in rank order — *"precedence is a public ruling delivered without a word."* An alternating order makes a negotiation; a scripted one makes an interrogation | **A PROCEDURE.** And the order is a **parameter** (`arrangement.order`), not a constant |
| **the ladder's rungs** | ⭐ **YES.** Beginning at *it did no harm* has conceded the fact before anyone asked. The rungs are **ordered by what each concedes** | **A PROCEDURE** — and the descent is an act, so the order is authored |
| **evidence before argument** | **YES**, and it is `AX-3`. Conjecture is descended from, never returned to: *"never conjecture where one can prove"* | **A PROCEDURE**, and the same one |
| **which claims a person deposits at WITNESS** | **NO.** WITNESS is one global fan-out, then a per-person deposit | **A MAP.** `§D.3` — do not shard it |
| **who attends** | **NO.** Each person's travel decision is their own, from a frozen world | **A MAP** — DELIBERATE, and permuting it must not move the hash (`PART D` row 41a) |
| **the bench's determinations** | **NO — and this is the one worth checking.** Each bench member acts `via` their own seat and writes their own Tenure. Two determinations do not read each other | **A MAP.** ⚠ Unless a quorum rule reads the count, which would make the *n*-th determination different from the first — see §C |
| **the interposition set** | **NO.** A set | **A PARAMETER** |
| **the register a speaker chooses** | **NO** at the choice; **YES** in effect, since a register is heard against what preceded it | ⚠ **UNRESOLVED — §D** |

---

# PART B · THE NESTED RUN

**A proceeding is the season loop nested** (`02_HIERARCHIES.md` §B.2) — *the same steps over a smaller
person set on a shorter clock.* It runs **inside the seam**, opened by a `speak` that declares
`contests: "a matter"`.

```
proceedings.run(proj, place, claimants, depth, max_depth) -> Margin
  -- ⚠ SIGNATURE CORRECTED 2026-09-06, AND IT IS NOW THE SAME STRING AS `08_SEAM.md` PART A.
  --   A draft of this file wrote `seam.proceed(proj, venue, matter, arrangement, attendees,
  --   depth, max_depth)` -- THREE parameters the provider contract does not carry, under a
  --   name the seam does not have. Two files in one proposal spelled the entry point two
  --   ways, which is `T-k`'s defect one level up: one thing, one signature.
  --   `venue` IS `place`; `attendees` ARE `claimants`; `matter` and `arrangement` are READ
  --   OFF the projection, because they are facts about the convened body rather than things
  --   a caller supplies. `prize` is consumed by `seam.contest` to SELECT this provider and
  --   is not passed on -- a provider that read its own prize could branch on it.
  depth < max_depth                     or return Refusal(depth_cap)      -- NO DEFAULT (H-87)
  arrangement = data.arrangements[ occasion_at(proj, place).arrangement ] -- a ROW, read at load
  bench       = judging_set(proj, place, matter)                          -- a Query. §B.2
  attendees   = present_at(proj, place)                                   -- RESOLVED ONCE, then
                                                                          --   FROZEN for the run
  term        = the opening act's declared term, or NONE                  -- T-n. §B.1
  repeat until nobody acts, or `term` matures:
      ORDER    `attendees`, per `arrangement.order`                       -- THE PROCEDURE
      for each, in that order:
          the person forms candidates from WHAT THEY HOLD                 -- AX-2. No World.
          the act resolves against the world its predecessors left        -- the ordered fold
          the act EMITS, into the same log                                -- §C.5, crossing 3
  return Margin                                                           -- never a winner
```

**Five properties, each carried by a construction rather than a rule:**

| property | construction | grade (Py / GD) |
|---|---|---|
| the proceeding writes nothing | **the wrapper holds no token** (`§A.2`) | **STRUCTURAL / MECHANICAL** — GDScript needs a copy or a lock (`D-49`) |
| the roster cannot change mid-proceeding | `attendees` is resolved once from the projection at entry and never re-read; the projection itself is read-only, so there is nothing that could change it | STRUCTURAL by lifetime |
| an appeal terminates | `max_depth`, caller-supplied, typed `Refusal` at the cap | MECHANICAL |
| nobody reads world truth | each turn forms candidates from a `PersonInterior` | STRUCTURAL by signature |
| the order is the arrangement's | one sort, at one site, keyed on a data value | **MECHANICAL** — and see `08_SEAM.md` §3 |

## B.1 · What ends it, and the answer is never "the engine decided"

| ending | mechanism |
|---|---|
| **nobody acts** | every attendee forms no candidate, or takes none. **A proceeding everybody abandons lapses** — and *a hearing nobody pressed* is a legitimate outcome, exactly as an undecided fight is |
| **the declared term matures** | `T-n` — the opening act declared it; MATTER matures it, citing the act that wound it. ⚠⚠ **THE CARRIER IS UNDER REVIEW, NOT SETTLED** — see the flag below the table |
| **the depth cap** | a typed `Refusal`, never a raise. An appeal chain that exhausts itself |
| **the matter reaches the foot of the ladder** | the rungs are finite; below *quality* there is nothing to concede |

⚠ **THERE IS NO SYSTEMIC ROUND CAP AND THERE MUST NOT BE.** A number in the engine that ends
proceedings is a clock nobody wound (`AX-5`, `T-c`). **The bound is the attendees' willingness to keep
spending, and the term somebody declared.**

> ### ⛔ **CORRECTED 2026-09-06 — A DECLARED TIME LIMIT IS LAWFUL, AND THIS SECTION HAD REFUSED IT.**
> *(Jordan: "you can have turn limits because an adjudicator may impose a time limit on the
> proceeding")*
>
> **The refusal was aimed at the wrong thing.** What `T-c` forbids is a clock **nobody wound**. A
> presiding seat declaring *"this hearing closes at sunset"* or *"each party is heard twice"* is
> ⭐ **a clock a PERSON wound**, which is precisely what the theorem requires rather than what it
> forbids — and a draft of this file read the theorem as banning the very thing that satisfies it.
>
> **The carrier is proposed, not settled, and this sentence is weaker than the one it replaces.**
> `T-n` says the opening act declares the terms; `Tenure.term` — the one new field in `19_PLAN.md` —
> would carry `matures_at`, `declared_by` and `closer`. ⚠ **Two of those three are struck below.** **A time limit is then a term declared by the
> presiding seat, and it matures citing the act that wound it**, which is the same shape as the depth
> cap.
>
> ⚠ **WHY IT IS FLAGGED RATHER THAN BANKED (2026-09-06).** A draft here wrote *"the carrier already
> exists and costs nothing new."* **It does not exist** — `shape.py:2066-2091` shows `Tenure` with no
> `term` field — and *costs nothing* was doing the work of an argument. This is the only new field in
> the whole proposal, so it is the one place `PART A`'s zero-primitive claim is spent, and it should
> be spent knowingly:
>
> | the question | state |
> |---|---|
> | **is a term a property of the TENURE, or of the DOCKET ITEM?** | ⚠ **open.** A presiding seat's *"this hearing closes at sunset"* binds the sitting, not the seat — which argues for `DocketItem`. `Tenure` was chosen because `declared_by` and `closer` want a person and a seat, and `Tenure` already has both. **Neither is obviously right and the choice is not this file's to make alone** |
> | **does anything OTHER than a proceeding want it?** | **yes, and that is the argument for the field.** Any duty with a horizon — a surety, a term of service, a stay — matures the same way. A field only a proceeding reads would be this subsystem growing the shared shape for itself, which is `ID-2` |
> | **could a declared term be an existing `Date` instead?** | ⚠ **not examined.** `convene` already writes `Date.due_at`, and a maturing Date is machinery that exists. **If it can, the proposal's new-field count goes to ZERO** — which is worth an hour before the field is built |
> | ⚠⚠ **is `declared_by` the field the tracer DELETED three days ago?** | ⭐ **almost certainly yes, and this is the sharpest of the four.** `shape.py:2074-2083` deletes `Tenure.conferrer` (2026-09-03) for occurring exactly once and reaching no reader — `ID-13` — **and gives the reason a replacement must answer:** *"WHAT CONFERRED a Tenure is the opening Act, in an append-only log with `causes[]`. A field here would be a second home for a fact the act already holds — `ID-2`."* **`declared_by` is `conferrer` under a new name.** The act that wound the clock is already in the log. **And `closer` goes the same way for the same reason** — the tracer's own note says WHO MAY REVOKE is the Seat's declared `revocation` basis (`T-o`), not a field, and `T-m` already holds that closure is ownership. **So the field, if it is built at all, is `matures_at` and nothing else: ONE column, not three** |
>
> ⚠ **AND `Tenure` ALREADY HAS `until`, WHICH A READER WILL REACH FOR AND WHICH IS NOT THIS.**
> `shape.py:2072` — `until: Optional[int]`, and `live` is `until is None`. **It records when the edge
> CLOSED, not when it is due to.** Writing a future value into it makes the tenure dead on arrival.
> Named here because the resemblance is close enough to cost somebody an afternoon.
>
> **Registered `P-04`. Do not build the field on this document's say-so** — and if it is built, build
> it at ONE column.
>
> ⭐ **AND IT IS A BETTER GAME, NOT A CONCESSION.** A declared limit is *a thing somebody set and
> somebody can be reached about*: you may **petition to extend it**, **run it out deliberately** while
> holding the floor, or **reach the person who set it** before the sitting. **A clock nobody wound
> gives a player nothing to do; a clock the chancellor wound is a second contest.** The historical
> case is the Athenian *klepsydra* — a water clock, stopped by an officer for the reading of
> documents, which is a declared term with a declared exception.
>
> **What stays refused:** a fixture that ends a hearing after N turns with no author. **If no term is
> declared, the run ends only when nobody acts, the ladder bottoms out, or the depth cap returns.**

---

# PART C · THE LADDER, AND THE ONE PLACE THE MAP CLAIM IS AT RISK

**The ladder is a procedure and its state is one value: the rung the matter has reached.**

> ### ⛔ **CORRECTED 2026-09-06 — THIS PARAGRAPH CITED §B.2 AS ITS AUTHORITY WHILE ASSERTING THE
> EXACT MODEL §B.2 RETRACTED.**
> It read: *"held on the `commit` edge from the case's opener to the matter, in `Tenure.degree`
> (`00_DERIVATION.md` §B.2)."* **`00_DERIVATION.md:275-302` overturned that on five grounds** and
> `13_ADVERSARIAL.md:51` records the retraction. A live internal contradiction, found by the
> playability relay's lane A while running a falsifier that was aimed at something else entirely.
>
> **The rung is not stored and has no owner.** It is a fold over the run's own emissions —
> `00_DERIVATION.md:299-301`: *"the lowest rung **any** emitted `matter.*` Event in THIS run has
> named."* ⭐ **Note the word `any`: the fold is NOT filtered to the acting person**, so a matter
> stands where the *run* has put it and not where each speaker last left it. A speaker can therefore
> be pushed down the ladder by an opponent's emission without conceding anything — which the next
> paragraph, written under the discarded model, denied. `17_PLAYABILITY.md` §D.5.
>
> ⚠ **And the fold is band-blind:** all four `speak` bands emit `matter.*`, so a *failing* speech
> moves the shared rung exactly as much as a winning one. Whether that is right is an open design
> question, not a settled reading — `Event.degree` is assigned (`shape.py:5854`) and a
> winning-emissions-only fold is available if wanted.

```
issue ladder:   procedural → conjecture → definition → quality
                 ↑ neither    ↑ TRUE       ↑ hinge      ↑ RIGHT          (AX-3 tracks)
```

**Descending is an act — `speak` at a lower rung — and it writes the rung and emits.** WITNESS fans
the Event out; every person present deposits a claim that the descent happened. **The concession is
visible because it was witnessed, and no `concession_penalty` exists anywhere in this design.**

⚠ **THE ONE PLACE THE PURE-MAP CLAIM IS AT RISK IS THE QUORUM, AND IT IS FLAGGED RATHER THAN
DISMISSED.** §A says the bench's determinations are a map because each member writes their own
Tenure and none reads another's. **That holds only while nothing counts them.** The moment an
arrangement wants *a majority carries*, the *n*-th determination differs from the first, the map
becomes a procedure, and **the count is a tally across holders, which `T-a` refuses as a field.**

> **The lawful shape, if a quorum is wanted:** the count is a **Query** over the bench's live
> determinations, evaluated **by a later act** — somebody *declares* the matter carried, and their
> declaration is the write. **Nobody's determination is changed by anybody else's; a further person
> reads the sum and acts.** That keeps the map a map and puts the threshold where `T-b` allows it: *a
> threshold may change what can be chosen; it may never produce an outcome.*
>
> ⚠ **This design does not build a quorum**, and `records_dissent` is the only key that gestures at
> one. **Registered: `10_LOOPS_AND_GAPS.md` `P-15`.** A design that shipped a majority rule without
> noticing it had made a stored tally would be committing `T-a`'s worked defect in the one place it
> is most natural.

---

# PART D · THE UNRESOLVED ORDER QUESTION, STATED RATHER THAN SMOOTHED

**Fig. 8's register matrix does not say when a manner is heard.** A register is chosen per speech, and
the study's claim is that each manner invites a specific misreading — but a misreading is formed by a
*hearer*, over a *sequence*. **Is the effect of a register a property of the act, or of the act's
position in the order?**

| reading | consequence |
|---|---|
| **property of the act** | the register enters the margin at the moment of speaking. **A map.** Simple, and it loses *"the opening too elaborately worked up"*, which is a fault of being **first** |
| **property of the position** | a register is heard against what preceded it. **A procedure**, and the fold already provides the order |

**This design takes the second and says why, and the reason is thin enough to be worth marking.** The
corpus's register faults are overwhelmingly faults of *sequence* — opening into a house that has not
settled, the joke that follows a concession, saying it **twice** (Fig. 26's third conjunct is
explicitly about repetition). **A register model that could not express *said twice* would fail one of
the four licensing conditions outright.**

⚠ **But the permutation test has not been run on it**, because nothing runs. `§G.4.1`: *a stage can
close on representations and still be behaviourally wrong.* **Registered as `P-16`, and it is the
second-largest open question in the design after `P-05`.**
