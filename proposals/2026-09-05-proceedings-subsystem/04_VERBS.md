# 04 · THE VERBS — what a person may do, and the count that justifies it

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

> ### THE HEADLINE
> **The game structure adds ZERO new verbs.** It gives a body to **four rows that exist and do
> nothing**, and it lands **one verb the architecture already specified and the table never got**.
> Every other act a proceeding needs is already in `verb_table.yaml`, already graded `ruled`, and
> already doing the same job somewhere else.
>
> **That is the test `03_VERBS_AND_LOOPS.md` §F.1 sets** — *four stages of design added no primitive*
> — and it is the only defence against a proceedings subsystem, which is the single most tempting
> place in this game to write thirty verbs.

---

# PART A · THE COUNT

| | verb | status **at commit `1b1e382`** | what this design does to it |
|---|---|---|---|
| 1 | **`speak`** | `own` · `requires: "—"` · **`writes: []`** · `emits: [speech.made]` · **`grade: assumption`** | ⭐ **GIVEN A BODY AND A MEANING.** Today it is the table's emptiest row: no precondition, no write, no refusal channel, and no statement anywhere of what it is *for*. **It becomes the act of addressing a convened body on a docketed matter — and it is the verb that opens the contest.** §B.1 |
| 2 | **`determine`** | `remit:determine` · `writes: [Tenure.degree]` · **`grade: absent`** · `requires: "a fired Date with a DocketItem; judging_set — D11, absent"` | ⭐ **GIVEN ITS `requires`.** Blocked since it was written on `Query.judging_set`, which **raises unconditionally** (`shape.py:3161-3163`). §B.2 |
| 3 | **`the six investigation acts`** | `own` · **`writes: []`** · **ONE ROW FOR SIX ACTS** · `grade: assumption` | ⭐ **SPLIT INTO ROWS — five of six, with typed preconditions, contests and bands.** The six were already named and specified *in prose*, which Jordan's *"unless they are rows, they are useless"* correctly grades as **not existing**. §B.3 |
| 4 | **`convene`** | `remit:convene` · `writes: [Date.due_at, ConveningCondition.attached]` · **`grade: ruled`** | **CORRECTED, not extended.** `scale: "settlement"` → an ordinal floor above the person tier (Jordan, 2026-09-05). `03_PARAMETERS.md` §C.1 |
| 5 | **`release`** | ⚠ **DOES NOT EXIST IN THE TABLE.** Specified as `§A.3` row 14 of Stage 4 — *one generic `release` verb, eligibility `own`, generic over kind* — and `HANDOFF_NEXT.md` §2a records the consequence: *"`hold` is closable only by `revoke`, so **A PERSON CANNOT RESIGN AN OFFICE**"* | ⭐ **LANDED.** `ID-14` requires it — every duty a proceeding imposes must be dischargeable — and **this design cannot be `AX-6`-compliant without it** |

**Everything else is reused unchanged:**

`move` (to attend) · `utter` (to make a Proposition) · `commit` / `repudiate` (to take and abandon a
position) · `tell` (to produce a proof) · `oblige` (to bind) · `open_case` (to raise the matter,
declaring its stages and terms) · `petition` (to ask) · `issue` / `comply` / `evade / defy` (a writ, a
stay, a summons, and defiance of one) · `confer` / `revoke` (the bench's seats) · `carry` /
`create_record` / `destroy_record` / `forge` (the record, and burning it).

> **Nineteen verbs reach into a proceeding. Fourteen are untouched. `speak` and `determine` gain a
> body, `convene` is corrected, `release` is landed, and one row is SPLIT INTO FIVE. Every name used
> was already in the tree; NO NEW ACT IS INVENTED, and the one this design nearly invented is
> recorded at §B.3 as the error it was.**

---

# PART B · THE FIVE, IN FULL

## B.1 · `speak` — *to address a convened body on a docketed matter*, and it is the contest

**Today `speak` is the emptiest row in the table**: `requires: "—"`, `writes: []`, `emits_on_refusal:
[]`, `grade: assumption`, `writes_note: "—"`. Nothing says what distinguishes it from `tell` or
`utter`, which is why it does nothing.

**The distinction the design gives it is exact, and it is the reason the row exists:**

| | |
|---|---|
| **`utter`** | brings a `Proposition` into existence. Immutable, authored, permanent (`AX-6`) |
| **`tell`** | transmits a **claim you hold** to whoever is present. Evidence. Deposits at WITNESS |
| **`speak`** | **presses a matter before those who may dispose of it.** It is only formable where there is an occasion to press it at |

```yaml
- verb:        "speak"
  stratum:     "social"
  eligibility: ["own"]                      # ⚠ NEVER a seat. §A.3 — a seat adds no verb
  requires:    "a live occasion at the actor's venue whose docket names the subject"
  requires_typed:
    form:      existence                    # §F.24a form 1 — existence over an edge kind
    of:        subject
    kind:      DocketItem
  contests:    "a matter"                   # ⭐ THE PRIZE
  writes:
    Carried:    ["Tenure.degree", "Person.stance"]
    Advanced:   ["Tenure.degree"]
    Held:       []                          # ⚠ lawful ONLY here — the attempt happened and cost a scene
    Turned:     ["Tenure.degree", "Person.stance"]
  emits:
    Carried:    ["matter.carried"]
    Advanced:   ["matter.advanced"]
    Held:       ["matter.held"]
    Turned:     ["matter.turned"]
  emits_on_refusal: ["speech.unheard"]
  grade:       "assumption"
```

**Four things about this row are load-bearing.**

**(i) `eligibility: ["own"]` — and it must never become `remit:`.** `§A.3`: *a seat makes ORDINARY acts
eligible where they otherwise are not, and no verb exists only for seat-holders.* **Anyone may
speak.** Whether anyone listens is reception, which is a different thing (Fig. 1's three layers, and
`03_PARAMETERS.md` §A row 1). ⚠ **The failure mode this forbids is the obvious one:** gating `speak`
on standing would make low standing an *unavailable option* rather than *a story*, and `§A.2` is
explicit that this *"deletes the best thing about the option set."*

**(ii) The `requires` is what stops `speak` being everywhere.** Without an occasion whose docket names
the subject, the Candidate does not form — so `speak` cannot be used to chat, and the table gains a
verb with a meaning instead of a verb with a gap.

**(iii) `contests: "a matter"` makes the proceeding ONE act at the season scale.** See §C.

**(iv) `Held: []` is the one lawful empty write, and it is the difference between a refusal and a
loss.** `§C.4`: *the act still emits, so the attempt happened, was witnessed, and cost a scene.* **A
speech that moved nothing is not the same as a speech that was never made** — and in a game about
overshoot, that distinction is most of the point.

⚠ **`Turned` is the band that makes this a design about overshoot rather than about winning.** A
speech can move the matter **against** the speaker: it writes the rung *and* the speaker's stance, and
it is the mechanical home of the corpus's whole fault catalogue — the turnable opening, the joke that
costs the speaker his dignity, the detailed denial that reads as anxiety. **A three-band ladder with
no adverse band could not express the study's central finding.**

## B.2 · `determine` — *to dispose of a matter that has been heard*

Blocked since it was written, on a Query that raises. **The design supplies the Query and the
`requires`, and does not change what the verb writes.**

```yaml
- verb:        "determine"
  stratum:     "binding_decision"
  eligibility: ["remit:determine"]          # unchanged
  requires:    "a fired Date with a DocketItem · the actor's seat is in judging_set(venue, matter)
                · the matter has been heard"
  requires_typed:
    all_of:
      - { form: existence,  of: subject, kind: DocketItem }        # form 1
      - { form: basis,      of: actor,   on: via }                 # form 7 — a basis lookup on the exercised seat
      - { form: relation,   of: subject, holds: heard }            # form 5
  writes:      ["Tenure.degree", "Tenure.since", "Tenure.until"]
  emits:       ["matter.determined"]
  emits_on_refusal: ["determine.refused", "determine.unheard", "determine.unseated"]
  grade:       "assumption"                  # was `absent`
```

**`Query.judging_set(w, venue, matter)`** — the function `shape.py:3161-3163` reserves and refuses:

```
judging_set(w, venue, matter) := { seat : seat.remit.acts ∋ arrangement.bench_basis
                                        ∧ under_purview(seat.scope, venue)      -- the containment WALK
                                        ∧ live hold on seat exists }
```

⚠ **THE LIVE SIGNATURE IS `judging_set(w, rung_id)` — TWO PARAMETERS, NOT THREE** (`shape.py:3161`).
This design's third parameter, the **matter**, is an extension and is stated as one. **The reason it
is needed rather than convenient:** `§B.7` says the judging set is *the seats whose remit covers **the
matter** at that venue*, so a signature that cannot see the matter can only answer *who sits here*,
never *who may decide this*. **A venue-only judging set would make two different questions before one
bench return the same answer**, which is the `Rung.judging_set_rule` defect — decision-shaped state on
a place — arriving one level up. The function currently raises and therefore has no caller whose
signature this breaks.

**Owned by nobody, computed, stored nowhere** — which is `§B.7` verbatim: *"the judging set is the
seats whose remit covers the matter at that venue — a Query over seats, which are arrangements of the
political layer, not a rule stored on a place."* And `Rung.judging_set_rule` was **deleted** by
`§A.3` row 7 for being decision-shaped state on a container, so this is the home the architecture
already chose.

⚠ **THE STRATUM ORDER DECIDES THE TEMPO OF EVERY TRIAL IN THE GAME, AND IT IS ALREADY IN THE DATA.**
`rosters.yaml:129` — `[movement, binding_decision, contested_physical, uncontested_material,
social]`, *"ORDER IS SEMANTIC HERE… editing the order changes which acts see which world."*
**`binding_decision` resolves BEFORE `social`.** So a `determine` and a `speak` in the same season
resolve **decision first, hearing second** — and a bench that determines a matter nobody has yet
pressed is **refused, with `determine.unheard`, witnessed.**

> ### **SO A HEARING AND ITS JUDGMENT CANNOT BE THE SAME SEASON, AND THAT IS A GAME RESULT RATHER
> ### THAN A CONSTRAINT TO ROUTE AROUND.**
> `convene` in season *n* · the matter pressed in season *n+1* · determined in season *n+2*. **The
> interval between the hearing and the judgment is a whole season in which people can act** — flee,
> bribe the bench, produce a document, reach the man who must renew the term, or die. **A design that
> resolved a trial in one tick would have deleted the most interesting part of one.**
>
> ⚠ **Recorded rather than claimed as designed.** This falls out of a stratum order somebody set for
> other reasons; it was not chosen here. **It is `§G.4.5`'s *answered by precedent* — and it should be
> checked against Jordan's intent, because if trials are wanted in one tick, the stratum roster is
> the row to argue about, not this verb.** `10_LOOPS_AND_GAPS.md` `P-14`.

## B.3 · The six investigation acts — **SPLIT INTO ROWS, because prose is not a mechanism**

⚠ **TWO CORRECTIONS, RECORDED RATHER THAN OVERWRITTEN, BECAUSE THE SECOND OVERTURNS THE FIRST.**

**First**, a draft of this section **invented a verb called `elicit`**. That was wrong: the six are
already named and specified in `proposals/`, and inventing a seventh name for one of them is
`§G.4.6`'s hazard — deriving without first asking whether the tree had decided the shape
(`§G.4.5`: *answered by precedent*).

**Second**, the correction to that was **also wrong**, and Jordan said why in five words:

> ### **"...unless they are rows, they are useless."**

**That is `CLAUDE.md` §0.05 applied to this design's own best find.** A table in a markdown file
giving each act a pool, a product and a cost is **reference**. `verb_table.yaml` carries **one row for
all six, with `writes: []`**. *If that document were deleted, would the game behave differently?* **No.
So the six do not exist**, and citing them as though they did would have been this proposal claiming a
mechanism it had only read about. `HANDOFF_NEXT.md` §2b says the same thing and calls it *the real
backlog*: **split into six rows with writes.**

### B.3.1 · What the prose supplies, and what it does not

*(`proposals/2026-08-31-unified-code-shape/08_FUNCTION_SURFACE.md` §3.3, citing `KTI:526-531`;
indexed at `proposals/2026-08-31-throughlines.md:413`.)*

| act | contests | produces | cost / risk |
|---|---|---|---|
| `examine` | *vs* `retention` | `firsthand` facets still persisting | **you are witnessed examining** |
| **`interview`** | *vs* obstinacy | **their `SAID` row — which may be a lie** | **they learn what you are asking**, and can tell others |
| `research` | *vs* the record's silence | `told_by(record, …)` with verified rootprints | access is an **admission gate held by persons with stances** |
| `surveil` | *vs* concealment | `firsthand` over the interval | duration; **exposure accrues to you** |
| `reconstruct` | *vs* the gap in the evidence | `inferred` claims and root identification | **a WRONG reconstruction deposits at real confidence and is acted on** |
| `Thread-Read` | — | rendering-side facets | Coherence risk; **claims most people cannot be told** |

*(The source's fifth column named a pool per act. It is struck, per the ruling above; the obstacle
side of each contest is kept, because it is a property of the world rather than of a stat roster.)*

⚠ **THE POOL COLUMN IS NOT ADOPTED — RULED BY JORDAN, 2026-09-05: *"ignore their use of
attributes."*** *Acuity · Charisma · Attunement · Focus · Agility · Will · Thread Pool* is an
attribute vocabulary from another exercise, and the roster it belongs to is **not settled**:
`CLAUDE.md` §5 records the derived-stat schema as **IN FLUX**, with the count ruled at ten, the
registry shipping nine, and **the tenth unnamed**. Adopting six pool expressions off a roster in that
state would be `ID-12`'s failure — branching on the members of a set that is still being decided —
and it would put this proposal's rows on a foundation somebody else is still pouring.

> **What is taken from the table is the NAME, the PRODUCT and the COST of each act. What is taken from
> the pool column is nothing.** Every row below therefore says what it contests **and not what it
> contests with**; `capability` supplies the dice, its keys are content by `ID-12`, and this design
> names none of them (`06_RESOLUTION.md` PART B, registered `P-06`).

**So the table supplies a product and a cost. It supplies NO `requires` for any of the six** — which
is precisely why the live row's note refuses to type the cell: *"typing it would mean inventing six
preconditions."*

> ### **THAT REFUSAL WAS CORRECT WHEN THE ONLY OPTION WAS INVENTION. IT IS NO LONGER THE ONLY OPTION.**
> `§F.24a` derived a **seven-form grammar** from the 32 live cells *after* that note was written.
> **Five of the six preconditions are expressible in it without inventing anything** — each falls out
> of the act's own stated product or cost. **The sixth is not, and is registered rather than forced.**

### B.3.2 · The five rows

```yaml
- verb: "examine"
  stratum: "social" · eligibility: ["own"]
  requires: "the actor is present where the thing examined is"
  requires_typed: { form: path, of: subject, kind: contain }          # form 3
  contests: "what persists"                                          # vs `retention`
  writes:  { Found: [], Partial: [], Nothing: [] }
  emits:   { Found: ["facet.found"], Partial: ["facet.found"], Nothing: ["facet.none"] }
  emits_on_refusal: ["examine.impossible"]
  grade: "assumption"
  # COST — "you are witnessed examining" — NEEDS NOTHING. The act emits at a venue; whoever is
  # co-located deposits a claim that you were looking. AX-2 + WITNESS, at zero cost.

- verb: "interview"
  stratum: "social" · eligibility: ["own"]
  requires: "the actor and the subject are present at the same venue"
  requires_typed: { form: path, of: subject, kind: contain }          # form 3
  contests: "a disposition"                                          # vs obstinacy
  writes:  { Read: [], Misread: [], Nothing: [] }
  emits:   { Read: ["said.given"], Misread: ["said.given"], Nothing: ["said.withheld"] }
  emits_on_refusal: ["interview.impossible"]
  grade: "assumption"
  # COST — "they learn what you are asking" — NEEDS NOTHING, and it is the same mechanism:
  # the SUBJECT is co-located by the precondition, so they always witness the asking.

- verb: "research"
  stratum: "social" · eligibility: ["own"]
  requires: "the actor holds a live admission to the archive"
  requires_typed: { form: existence, of: subject, kind: Tenure }      # form 1 — an `oblige` or `hold`
  contests: "what the record holds"
  writes:  { Found: [], Partial: [], Nothing: [] }
  emits:   { Found: ["record.read"], Partial: ["record.read"], Nothing: ["record.silent"] }
  emits_on_refusal: ["research.unadmitted"]
  grade: "assumption"
  # ⭐ "EVERY GATE IS A PERSON, SO EVERY GATE HAS A PRICE AND A GRIEVANCE" — the source's own words,
  # and the admission is an EDGE, so the three routes around it (interview an archivist, use a deep
  # channel, steal) are already three existing verbs. No gate mechanism is added.

- verb: "reconstruct"
  stratum: "social" · eligibility: ["own"]
  requires: "the actor holds claims bearing on the subject"
  requires_typed: { form: own_ledger, of: subject }                   # form 6 — `tell`'s own form
  contests: "what can be inferred"
  writes:  { Sound: [], Wrong: [], Nothing: [] }
  emits:   { Sound: ["inference.made"], Wrong: ["inference.made"], Nothing: ["inference.none"] }
  emits_on_refusal: ["reconstruct.groundless"]
  grade: "assumption"
  # ⭐ `Sound` AND `Wrong` EMIT THE SAME KIND. "A WRONG reconstruction deposits at real confidence
  # and is acted on." This is the purest AX-2 act in the game and the one most worth building first.

- verb: "surveil"
  stratum: "social" · eligibility: ["own"]
  requires: "the actor is present at the place, for a declared interval"
  requires_typed: none
  requires_typed_note: >-
    form 3 for the place, AND a declared interval, which is `T-n` — the opening act declares its
    term. ⚠ `Tenure` HAS NO `term` FIELD in the tracer (`shape.py:2066-2091`), so the second half
    is UNTYPABLE TODAY. Registered `P-04`; the row is written and the cell is honest.
  contests: "what is done unseen"
  writes:  { Seen: [], Glimpsed: [], Nothing: [] }
  emits:   { Seen: ["watch.kept"], Glimpsed: ["watch.kept"], Nothing: ["watch.empty"] }
  emits_on_refusal: ["surveil.impossible"]
  grade: "assumption"
  # COST — "exposure accrues to you" — is the duration: a longer term is more occasions on which
  # somebody co-located deposits a claim that you were there. Again, WITNESS, at zero cost.
```

### B.3.3 · The sixth is NOT written, and that is the honest state

**`Thread-Read` gets no row here.** Its risk is *Coherence*, which this design does not touch, and its
obstacle is not a property of the world but of a rendering layer this proposal has not derived.
**Writing a row that refers to a mechanism this proposal has not derived would be exactly the
invention the live note refuses.** Registered:
`10_LOOPS_AND_GAPS.md` `P-19`, graded `absent`, **with no default.**

⭐ **AND ITS EXISTENCE EXPLAINS A SOCKET THIS DESIGN DECLINED TO TAKE.** `Thread-Read`'s cost is
**Coherence risk** — which is why `(Person, coherence)` is the one matrix row the gate licenses to a
`driver="Seam"` (`shape.py:2829-2836`), and why `F.5` asks what reads it. **That socket belongs to
Thread-Read.** `00_DERIVATION.md` PART C refuses it because a seam that writes has begun to own; **the
refusal now has a second and better reason — the field is already spoken for.**

### B.3.4 · Why this belongs in a proceedings proposal at all

Because **row 4 of the requirement table is TERMINAL and `interview` is the only act that clears it.**

| the study says | the act already said it |
|---|---|
| `S5` — **the read is MADE, not taken.** Perspective-*getting* is the one positive result in twenty-five experiments; perspective-*taking* raised confidence without accuracy | it is contested **against the other person**, so the read is produced by acting on them |
| the *Guiguzi* loop — *draw the other party out; provoke a reply, because the reply reveals; if it does not fit, say the opposite and listen again* | the product is **their `SAID` row**, not a fact about them |
| Han Feizi 12 — *the divided motive*, where **both the stated and the operative motive are unsafe to address** | ⭐ **the cost is that they learn what you are asking** |

⚠ **AND THE SOURCE'S OWN FRAME IS THE ONE THIS DESIGN NEEDED AND WOULD OTHERWISE HAVE ARGUED FOR:**
*"Every one is available to any person; the substrate's rule that action eligibility never consults
office binds here without exception — the detective seat is not a seat, it is six acts anyone may
take"*, and *"there is no clue counter, no case object, no investigation skill, and no threshold
anyone sets."* **That is `§A.2` and `§A.3` stated from the other side, by somebody who was not writing
a proceedings subsystem** — which is corroboration rather than a source.

⚠ **THE ONE DEFECT THE SPLIT DOES NOT FIX, AND IT IS THIS PROPOSAL'S LARGEST.** All five rows carry
`writes: []`, because what an investigation produces is a **claim**, and claims are deposited at
**WITNESS**, not written at RESOLVE — which is why `tell` writes nothing either (*"deposits at WITNESS,
not here"*). **So five verbs emit a degree that nothing consumes**, which is `ID-13` on rows this
proposal is itself adding — the half `HANDOFF_NEXT.md` says sessions forget. The mechanism that would
carry a degree into a deposit is `observation_deposit_modes` / `H-122`, **open**. Registered `P-05`.

> ### **SO THE HONEST HEADLINE FOR THIS SECTION IS NARROWER THAN "THE SIX ARE LANDED".**
> **Five of six become rows with typed preconditions, contests and bands. None of the five can yet
> deposit what it found.** The split is necessary and is not sufficient, and saying so is the
> difference between this and a document that claims discovery works.

## B.4 · `convene` — corrected, not extended

Covered at `03_PARAMETERS.md` §C.1. One key changes: `scale: "settlement"` becomes an **ordinal floor
above the person tier**. Nothing else about the row moves, and the design adds nothing to it.

## B.5 · `release` — landed, because `AX-6` cannot hold without it

**Specified by Stage 4 `§A.3` row 14 and absent from the table.** A proceeding imposes duties —
penances, sureties, terms of service on a commission, obligations under a treaty — and **`ID-14` says
what an act can open, an act must be able to close.**

```yaml
- verb:        "release"
  stratum:     "social"
  eligibility: ["own"]                       # T-m — closure IS ownership. Generic over kind
  requires:    "a live Tenure of the named kind whose subject is the actor"
  requires_typed: { form: existence, of: subject, kind: Tenure }    # form 1
  writes:      ["Tenure.until"]
  emits:       ["tenure.released"]
  emits_on_refusal: ["release.impossible"]
  grade:       "ruled"                       # the shape is ruled; only its absence was the defect
```

**Domain: `tenure_kinds \ {contain}`** — the `F4` correction, because `contain`'s subject is a `Rung`
and a Rung can never act.

⭐ **AND IT IS ALSO ROW 14 OF THE REQUIREMENT TABLE.** *Close, and leave the other party a way down* —
the study's most consistently neglected step, terminal for the relationship, and **one of only three
rows whose failure no later step repairs.** Mechanically, **giving the other party a way down is
releasing something you could have held them to**: the surety you could have called, the penance you
could have exacted, the oath you could have enforced. **The corpus's hardest step is an existing verb
the table forgot to carry**, and no new mechanism is needed for it.

---

# PART C · WHY THE PROCEEDING IS ONE CONTEST, NOT A SEASON OF ACTS

**`speak` declares `contests: "a matter"`, so the fold hands the whole proceeding to the seam.** The
alternative — each speech as its own season-level act, the proceeding emerging over many seasons —
was tried first and fails on three counts:

| | why the season-level model fails |
|---|---|
| **the architecture forbids it** | `§E.1`: *"a contest attaches at RESOLVE, where a conflict subdivides the tick and runs the same steps over a smaller person set on a shorter clock. A battle, a hearing, an examination and two siblings arguing over a barn are the same call"* |
| **the frozen world forbids it** | `§D.2`: everyone decides simultaneously from a frozen world; **nobody reacts to a same-season act.** A back-and-forth in which nobody may react is not an exchange |
| **the stratum order forbids it** | `social` is **last**, so all speeches resolve after everything else — and within the stratum the order is `(stratum, actor-hash, …)`, which means **a hash would decide who spoke first.** `F.26` already says this about larders; at a proceeding it would be intolerable |

> ### **AND INSIDE THE SEAM, THE ORDER IS THE ARRANGEMENT'S — NOT THE STRATUM ROSTER'S.**
> `§G.2.9`: *a procedure is required wherever the order of sub-steps changes the outcome, and nowhere
> else.* **At a proceeding the order IS the mechanism**: Roman senators were called in rank order, so
> precedence was *"a public ruling delivered without a word"*; an alternating order is what makes a
> negotiation a negotiation; a scripted order is what makes an interrogation one. **So `order` is a
> parameter of the game and the nested run is a procedure**, and the season fold's canonical sort has
> no authority inside it.
>
> ⚠ **This is a real extension of the seam contract and it is stated as one, not smuggled.** No
> subsystem before this one has needed the *caller's* ordering to be a parameter. `08_SEAM.md` §3
> sets out why it is an amendment to the one owner rather than a second story, and what would show
> that judgment wrong.

---

# PART D · THE FIFTEEN STEPS, AND WHICH VERB CLEARS EACH

The study's requirement table has fifteen rows. **Mapping the roster onto it is the test of whether
the verbs are the right ones** — and the interesting result is the third column.

| step | cleared by | |
|---|---|---|
| **0** whether to enter at all | **no verb** — not taking `move` | ⭐ **TERMINAL, and free.** The largest lever in the corpus is the absence of an act |
| 1 audit one's own standing | **no verb** — `standing` is a Query the player is shown of their own character | reception, not action |
| 2 classify the body | **no verb** — a claim the person holds, which **may be false** | `AX-2`. A wrong classification is a story |
| 3 find who decides | **`interview`**, or `tell` from someone who knows | the judging set is resolver-side and **unreadable from a decision** |
| **4** what may not be said | **`interview`** | ⭐ **TERMINAL, and the one evidenced capacity** |
| 5 inventory the proofs | **no verb** — the claims in one's own ledger | the mirror test is the player's reasoning |
| 6 fix the concession in advance | **no verb** — deciding what one will `release` before entering | prior specification under low arousal |
| 7 choose a register | **a parameter of the act**, admissible per `arrangement.registers` | Fig. 8 |
| 8 open | **`speak`**, first in the order | tolerance of dead air = not speaking first |
| 9 arrange | **which claims one `tell`s, and which one withholds** | the dilution effect; the unused proof is FREE and hoarded |
| 10 retrieve | **which Propositions and Records one holds** | *memoria* is what is in the ledger and in hand |
| 11 hold position under attack | **`speak`, or the absence of it** | Fig. 27's ladder; `Held: []` is a legitimate result |
| 12 supply a favourable construction | **`utter` + `speak`** at a lower rung | the descent, witnessed |
| 13 attack | **`speak`** with a person subject, under Fig. 26's four conjuncts | §B.4 of `03_PARAMETERS.md` |
| **14** close, leaving a way down | **`release`** | ⭐ **TERMINAL for the relationship** |

> ### **SIX OF THE FIFTEEN ARE CLEARED BY NO VERB AT ALL, AND THAT IS THE RESULT RATHER THAN A GAP.**
> Rows 0, 1, 2, 5, 6 and 10 are **things a person holds or declines to do**. They are not inert: they
> decide which Candidates form and which the player takes. **And two of the three TERMINAL rows are in
> that group** — row 0 is not acting, and row 4 is the one act nobody else in the game has a reason
> to take.
>
> **This is `S7` reproduced mechanically without having aimed at it.** The study's finding is that the
> corpus says least about exactly the steps that matter most, because they are the steps for which no
> rule can be written. **A verb roster derived from the corpus therefore has no verb for them — and
> the design's response is not to invent one, but to make sure the player can see the choice.** That
> is `07_THE_GAME.md` §3.
