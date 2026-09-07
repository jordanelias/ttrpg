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
  writes:                                   # ⭐ EVERY `Person.stance` IS THE SPEAKER'S OWN. See (ix)
    Overwhelming: ["Person.stance"]         #   the actor's, not the hearers'
    Success:      ["Person.stance"]         #   the actor's
    Partial:      ["DocketItem.matter"]     # ⭐ CORRECTED 2026-09-06 — was []. See (vii)
    Failure:      ["Person.stance"]         # ⚠ an ADVERSE write, and the actor's. See (v)
  emits:
    Overwhelming: ["matter.carried"]
    Success:      ["matter.advanced"]
    Partial:      ["matter.held", "docket.formed"]   # ⭐ the question MULTIPLIES
    Failure:      ["matter.turned"]
  emits_on_refusal: ["speech.unheard"]
  grade:       "assumption"
```

> ### ⚠ **THE BAND NAMES ARE THE LADDER'S OWN, AND A DRAFT OF THIS ROW COINED FOUR OF ITS OWN.**
> The draft keyed `writes`/`emits` on `Carried · Advanced · Held · Turned`. **That row could not have
> loaded and could not have run.** `VerbRow.writes_at` / `emits_at` **raise on any degree the row does
> not declare**, and a margin-graded contest returns `DEGREE_LABEL[…]` — `Overwhelming · Success ·
> Partial · Failure` — from `engine/autoload/dice_engine.py::degree_from_net`, *"THE degree ladder.
> Single owner for every scale of the game (Jordan ruling, 2026-08-14)."* **Every `speak` would have
> raised at the first fold.**
>
> **And it was not merely a naming slip — it was the exact defect `09_IMPOSSIBILITIES.md` row 16
> names as this design's weak point**, committed in its headline verb. Jordan, 2026-08-15: *"systems
> should not need different degree bands. it should be consistent in application."* Combat's
> three-band exemption exists **by ruling, because combat reads a scene rather than a margin**, and
> `rosters.yaml` says it "MUST NOT BE CONFUSED" with the ladder's four.
>
> **The four canonical bands say everything the coined ones did**, and the mapping is one-to-one:
> carried → `Overwhelming`, advanced → `Success`, held → `Partial`, **turned → `Failure`.** The
> *emission* kinds keep the proceeding's own vocabulary, because Event kinds are per-row and declared;
> **only the KEYS are the ladder's**, which is exactly the line `T-k` draws.

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

**(iv) ⛔ SUPERSEDED 2026-09-06 — `Partial: []` was NOT lawful here, and (vii) below replaces it.** ~~`Partial: []` is a lawful empty write, and it is the difference between a refusal and a loss.~~
`§C.4`: *the act still emits, so the attempt happened, was witnessed, and cost a scene.* **A speech
that moved nothing is not the same as a speech that was never made** — and in a game about overshoot,
that distinction is most of the point. ⚠ **A draft called this *"the one lawful empty write"*; it is
not.** Every band of all five investigation rows writes `[]` for the same reason (they deposit at
WITNESS), so the claim was falsified fifteen times in this file. **Corrected: an empty write is lawful
wherever the act's product is a deposit rather than a state change.**

⚠ **`Failure` WRITING `Person.stance` IS WHAT MAKES THIS A DESIGN ABOUT OVERSHOOT RATHER THAN ABOUT
WINNING.** A speech can move the matter **against** the speaker, and the band writes the speaker's own
stance when it does. **This is the mechanical home of the corpus's whole fault catalogue** — the
turnable opening, the joke that costs the speaker his dignity, the detailed denial that reads as
anxiety. **A ladder whose bottom band wrote nothing could not express the study's central finding**,
and the one ladder's `Failure` is exactly the adverse band the coined `Turned` was reaching for.

**(vii) ⭐ WHAT A `Partial` BRINGS FORWARD — THE QUESTION MULTIPLIES (Jordan, 2026-09-06).**

> *"what does a partial bring forward mechanically that a failure or success doesn't?"*

**Under the row as it stood, nothing.** `Partial` was the only band that wrote no state and moved no
rung — `matter.held` and an empty write. `Failure` at least turns the matter and writes an adverse
stance. **So the middle band was strictly emptier than the bottom one**, which is the classic dead
middle band and it is worse than having three bands.

**And a weaker Success is not the answer either.** If `Partial` is *"you moved it, but less far"*, it
sits on the same axis as the two bands above it and adds no state. **A middle band earns its place
only by being OFF that axis** — a state neither winning nor losing produces.

> ### **`Partial` WRITES `DocketItem.matter` AND EMITS `docket.formed`. THE MATTER STAYS WHERE IT IS
> AND THE DOCKET GROWS.**
> You did not move the matter. **You made the room take up something that was not before it.** That is
> what a held matter does in every real proceeding — it is referred, adjourned, or answered with a
> subsidiary question — and it is the one outcome neither `Overwhelming` nor `Failure` can produce.
> Mechanically it is a **detour**: the proceeding now has more to get through, and somebody put it
> there on purpose or by accident.

**It costs nothing new.** `(DocketItem, matter)` is a live `[CAL, RES]` matrix row emitting
`docket.formed` (`write_matrix.yaml:119-125`); `carry` already writes it. **No carrier, no field, no
Event kind, no verb.**

⭐ **AND THIS IS FAIL-FORWARD, WHICH THE ROW HALF-HAD ALREADY.** `Failure` emits `matter.turned` — the
matter changes hands rather than the turn evaporating, so losing already **changes course** instead of
negating. `Partial` was the band that negated. **Now every one of the four leaves the proceeding in a
different place**, which is the condition a flowchart cannot satisfy.

**(viii) ⭐ WHERE THE BAND CONTENT COMES FROM, AND WHY THE READING WAS DONE (Jordan, 2026-09-06).**

> *"this is also why we did all that research so that we could reason degrees of success/failure from
> it whether it was presented directly or shown by omission or seeing how success would define what a
> failure is."*

> **Jordan, sharpening it:** *"each figure by showing success within its set of constraints by the
> same token shows failures, and the qualitative corpus and discussion will therefore discuss that
> either directly or indirectly as the opposite of success."*

> ### ⭐ **THE DERIVATION IS TOTAL, NOT SELECTIVE. A CONSTRAINT SET DEFINES BOTH SIDES OF ITSELF.**
> **You never go hunting for the failure material.** A figure that states what a move must satisfy to
> land has, by stating it, said what happens when it does not — the corpus then discusses that either
> directly (a fault table) or as the opposite of the success it named. **So every one of the 27
> figures yields bands, not only the ones that happen to be written as faults.**
>
> **This is what the reading was FOR**, and it is why the bands cost a data roster rather than
> measurement: the study is not being mined for numbers, it is being read for **what a move is taken
> as** when it satisfies its constraints and when it does not. `PERCEPTION` at **155 atoms in 26 of 27
> figures** is that, and it is inherently graded — *how a thing is taken* has no binary form.

**The four bands are DERIVED from the figures, not invented, and the census says the material is
there.** `16_THE_FLATTENING.md` measured the study at **591 atoms**, of which **`CONDITION` is 86 in
21 of 27 figures** and **`PERCEPTION` is 155 in 26 of 27** — and its PART B finding was that *"the
study's conditions **price** a move and this design's **refuse** one."* **That is the same correction
as §B.1's, arriving from the atom side before Jordan made it.**

| how the corpus states it | worked examples — **these are illustrations of the rule above, not an exhaustive list of where bands can be found** |
|---|---|
| **stated directly** | Fig. 26's four conditions each name **what a frank criticism is READ AS** when the condition fails — hostile · competing · characterizing · bargaining. That is a failure catalogue, not a veto |
| **shown by omission** | Figs. 9 and 10 — *conduct under attack*, *attacking without cost* — are **68 atoms of fault tables**, the densest material in the corpus, and they enumerate ways a move goes wrong with no matching table of ways it goes right |
| ⭐ **by seeing how success defines failure** | Fig. 5's ladder gives what is being asked for at each rung; **the failure is the same request read at the wrong rung**, which needs no separate authority |

⚠ **So a band's content is a READING obligation, not a magnitude to sweep** — which is exactly the
distinction `§B.1.2` draws below between aptness and coefficients, and it is why the twelve speech
kinds cost a data roster rather than 144 numbers.

**(ix) ⭐ WHOSE STANCE — THE SPEAKER'S, ON ALL THREE BANDS (settled 2026-09-07).**

The row wrote `Person.stance` at three bands and named the owner for one of them. **(v) says of
`Failure` that *the band writes the speaker's own stance*** — and it says it there precisely because
the speaker's stance moving on a *loss* is the surprising half. On `Overwhelming` and `Success` the
natural reading is the opposite one: the speech moved **the hearers'** stances, which is what
*carrying the room* means in the fiction.

> ### **IT IS THE SPEAKER'S ON ALL THREE, AND THE ARCHITECTURE FORCES IT RATHER THAN PREFERRING IT.**
> A `Person` carrier holds nothing about another person, and an act writing many hearers' interiors
> is **one act, many owners** — which is the exact objection `00_DERIVATION.md` §B.2 uses to KILL the
> `Tenure.degree` proposal in this same directory: *each party who descends would write the OPENER's
> edge. Many writers, one owner.* **The design applied that objection to a field it rejected and not
> to the verb it kept.** `17_PLAYABILITY.md` §D.3 and §I item 3 reached the same place independently
> and called it *a live `AX-4` breach in the row as written*; this is that edit, made.
>
> ⚠ **And the matrix cannot settle it, which is why it needed saying in the row.** `(Person, stance)`
> is one row with no subject column, so **both readings load**. Nothing would have caught the wrong
> one.
>
> **What moves in the hearers is not a stance at all** — it is what they now hold about the speaker
> and the matter, deposited at WITNESS as claims, per person, per channel, each of which may be
> wrong. That is `AX-2`'s currency and it needs no interior write.

### B.1.1 · ⭐ **ONE VERB, MANY SPEECH KINDS — and a proceeding weights them by APTNESS, not by coefficients**

> **Jordan, 2026-09-06:** *"I assume the different proceedings weigh different kinds of social verbs
> (eg speak, refute) differently?"*

**The intuition is right and the mechanism is not a weight.** Refutation matters at a trial and is
meaningless at a parliament; amplification carries an epideictic occasion and is empty at the
conjecture rung. **What varies is whether the move is APT — and an inapt move is REFUSED, not
discounted.**

**First, there are not many social verbs. There is one, with kinds in data** (`ID-7`: *one type, many
kinds; the membership in data*):

```yaml
# rosters.yaml: speech_kinds — a closed set in DATA. Adding one is a data edit.
#   what the move DOES to the matter                      which rung / genre it is apt at
propose      · concede      · refute       · define       · construe   · amplify
object       · impugn       · pre-empt     · recapitulate · withhold*  · elicit-in-room*
```
*(the two starred are named for completeness and are not this design's to roster — `withhold` is not
an act at all, §C, and asking is `interview`, §B.3.)*

**Then three data facts decide aptness, and none of them is a coefficient:**

| what decides | mechanism | effect |
|---|---|---|
| ⭐ **the genre** (Fig. 23, derived from the bench's remit) | ⛔ **CORRECTED 2026-09-06 — a mismatch PRICES, it does not refuse.** See the block below | *"Inverted, the case is lost regardless of its merits."* ⭐ **Lost, not FORBIDDEN.** An inapt speech forms, draws against a higher obstacle, and can still land — which is what makes the frame refusable |
| **the rung** (Fig. 5) | the ladder's current position | `refute` is apt at **conjecture** and empty at **quality**, where the fact is admitted. `construe` is the reverse |
| **`registers[]` · `proofs[]`** (Figs. 8, 6) | admissibility sets on the arrangement | a ceremony admits few manners; a deliberative body admits **no proofs at all** |

> ### ⛔ **CORRECTION, 2026-09-06 (Jordan) — THE GENRE MISMATCH WAS A REFUSAL AND MUST BE A PRICE.**
>
> > *"if you have a character roll a pool against an obstacle, then you can have someone choose the
> > 'wrong' action and roll against a higher obstacle but still succeed, which means that the entire
> > proceeding has pivoted from its deterministic flow for what is optimal by being subverted. finally
> > you can have a character roll against the obstacle of the right choice as per flow chart and still
> > fail!"*
>
> **Three facts, and they point the same way.**
>
> 1. ⭐ **THE ROW ALREADY DOES THE RIGHT THING. ONLY THIS PROSE SAID OTHERWISE.** `speak`'s
>    `requires_typed` is a **single clause** — `form: existence · of: subject · kind: DocketItem`.
>    There is no genre conjunct in the schema and there never was. **The refusal existed only in the
>    sentence above**, which under `CLAUDE.md` §0.05 is reference and not mechanism. Found by the
>    playability relay's lane A.
> 2. ⭐ **AND THIS DESIGN'S OWN SHOWCASE EXAMPLE REQUIRES THE ACT TO FORM.**
>    `03_PARAMETERS.md:133` celebrates *Demosthenes on the crown* — *"it explains why Demosthenes
>    **wins by refusing the frame**"*. **The rule as written refuses that speech.** A design cannot
>    both forbid a move and cite winning by it as its best worked case.
> 3. **A refusal is still a binary, which is the whole complaint.** You could speak or you could not.
>    Priced, the inapt move is a *decision under uncertainty*: you may take the worse ground on
>    purpose, and you may get away with it.
>
> **`§B.1.2`'s defence below survives in a better form and is NOT discarded.** Its real argument is
> *"a refusal EMITS and a weight does not — the player is witnessed committing a category error."*
> ⭐ **So does a failure.** `matter.turned` fans out to every ledger in the room exactly as a refusal
> does. **The public category error is delivered by the BAND, and does not need the gate** — so the
> argument's substance is kept and its mechanism is dropped.
>
> **What this costs:** one obstacle term (`aptness`), composed and floored like the others. What it
> buys is the thing a flowchart cannot have — **the right choice can fail and the wrong choice can
> land.** `17_PLAYABILITY.md` §D.1 killed a position proposing this term; the kill was right about
> that position's four errors and **wrong to take the mechanism down with it** (§D.1a).

## B.1.2 · Why aptness rather than weights, and it is not a preference

| | |
|---|---|
| ⭐ **weights grow with the PAIR COUNT** | 12 speech kinds × 12 games = **144 numbers nobody measured.** `§0.06`'s emergence rule: *"interaction must be uniform — the rule count must not grow with the pair count. When it starts to, you have stopped composing and started scripting"* |
| **and the study forbids the numbers** | *"a type inventory is not a frequency inventory… Han Fei's seven registers exhaust the ways a manner can be misread and say nothing about which misreading is likeliest before a given ruler"* |
| ⭐ **a refusal EMITS, and a weight does not** | an inapt move at `-2 dice` is a bad roll nobody sees. **An inapt move refused is an Event, fanned out to everyone present, deposited in every ledger.** The player is *witnessed committing a category error* — which is exactly the corpus's fault at requirement row 2, and it is how they learn |
| **and it keeps the closure claim** | aptness reads `genre`, the rung and two admissibility sets. **Nothing reads the game's name** |

> ### **WHAT *IS* GRADED IS THE MANNER, NOT THE MOVE.**
> `register fit` is a term in the obstacle (`06_RESOLUTION.md` §C.1) and it is exactly *"which
> misreading this manner invites, before this room."* **So: WHICH move you make is apt or refused;
> HOW you make it is graded.** That is Fig. 8 and Fig. 23 doing two different jobs, and collapsing
> them into one weight table would have lost both.

⚠ **CONVERGENCE, RECORDED BECAUSE IT IS THE ONLY CLEAN ONE IN THIS EXERCISE.** An independent Fable
synthesis under the same brief and the same scope ban reached **`speak` with fifteen data-rostered
speech kinds** from the other end. **Two derivations reaching *one verb, kinds in data* without either
taking it from the other is corroboration** (`§G.4.3`) — and neither reached a weight table.

## B.2 · `determine` — *to dispose of a matter that has been heard*

Blocked since it was written, on a Query that raises. **The design supplies the Query and the
`requires`, and does not change what the verb writes.**

```yaml
- verb:        "determine"
  stratum:     "binding_decision"
  eligibility: ["remit:determine"]          # unchanged
  requires:    "a fired Date with a DocketItem, and the actor's seat is in judging_set(venue, matter)"
  requires_typed:
    all_of:
      - { form: existence,   of: subject, kind: DocketItem }       # form 1
      - { form: basis,       of: subject }                         # form 7 -- CORRECTED, see below
      - { form: cardinality, of: subject, amount: <the row's quorum> }   # form 4 -- the quorum
  writes:                                    # ⭐ DEGREE-KEYED, and no longer "unchanged"
    Overwhelming: ["Tenure.since", "Tenure.degree"]
    Success:      ["Tenure.since", "Tenure.degree"]
    Partial:      ["Tenure.degree"]
    Failure:      []
  emits:
    Overwhelming: ["matter.determined"]
    Success:      ["matter.determined"]
    Partial:      ["matter.determined"]
    Failure:      ["matter.undetermined"]
  emits_on_refusal: ["determine.refused", "determine.unseated"]
  grade:       "assumption"                  # was `absent`
```

> ### ⭐ **TWO CORRECTIONS TO THIS ROW, 2026-09-07 — and the first reverses a correction this file
> ### already made and was proud of.**
>
> **⑴ `writes` GAINS `Tenure.since`, AND THE *UNCHANGED* NOTE IS STRUCK.** The table below records a
> draft being corrected *away* from `[Tenure.degree, Tenure.since, Tenure.until]` on the ground that
> the live row writes only `degree` — **and the live row is precisely the thing this design changes.**
> The result was a verb that can GRADE a Tenure and cannot OPEN one, in a design whose every
> arrangement row carries a `disposes:` key naming what a finding writes. **`disposes:` had a
> declared meaning and no writer anywhere in the table.**
>
> `19_PLAN.md` step 15 already ruled it — *the declaring act is the determination … the declaration
> writes the disposal* — and `04_CODE_ARCHITECTURE.md` §B.7 names `determine` as a seat's conferral
> basis, which is what licenses opening an edge on somebody else. **Who owns the Tenure a determiner
> opens: its SUBJECT**, exactly as `confer` opens a `hold` owned by its conferee and not by the
> conferrer. `AX-4` is untouched; what licenses the write is the seat's basis, not the actor's
> ownership.
>
> ⚠ **Two consequences, both stated rather than discovered later.** The row now declares `contests:`
> in the same build step, so loader invariant 12 requires `writes` and `emits` to be degree-keyed
> with equal key sets — they are, above. And **the write gate needs one more clause**: `§C.2`'s `F3`
> admits `actor == subject`, `T-n`, `T-o`-with-`via` and the destroy cascade, and a conferral-basis
> opener matches none of the four. **So does `confer`, today**, which is an `IN`-lane defect this
> design reveals rather than causes.
>
> **⑵ THE `basis` CONJUNCT NAMED AN OPERAND ITS FORM DOES NOT ADMIT.** The corrected cell read
> `{ form: basis, of: actor, on: subject }`. `rosters.yaml` gives `basis` the operand set
> `[subject, from, to]` — **`actor` is not in it**, and a cell naming an operand outside its form's
> set refuses at load. **So the correction that fixed one load failure introduced another**, and the
> table below is one row short of the truth. The conjunct binds `subject`; the actor is the acting
> person by construction and needs no operand.
>
> **⑶ AND THE QUORUM CONJUNCT IS ADDED, WITH ITS PRICE ON THE RECORD.** `19_PLAN.md` step 15 states
> it plainly: this **widens the precondition grammar by two entries, counted as a design change and
> taken because it is what works best** (`ED-SC-0034`). ⚠ **A read-only planning pass proposed making
> it free** by binding the threshold to `amount` through form 4 as it stands; `cardinality`'s operand
> set is `[subject, from, to]` and **does not admit `amount`**, which is the same defect as ⑵ one
> form along. **The widening is real and is paid for openly** — `21_RECONCILIATION.md` PART A.1.

⚠ **THREE CORRECTIONS TO A PUBLISHED DRAFT OF THIS ROW, EACH OF WHICH WOULD HAVE FAILED THE LOADER.**

| the draft | why it fails |
|---|---|
| `writes: [Tenure.degree, Tenure.since, Tenure.until]` **while the prose said *"does not change what the verb writes"*** | the live row writes `["Tenure.degree"]`. **The prose and the YAML contradicted each other in the same section** — and the prose was the true one, so the YAML is corrected to it |
| `{ form: basis, of: actor, on: via }` | ⚠ **`via` is not in the closed operand roster** `(actor, subject, from, to, site, kind, amount, floor)`, and *"a cell naming an operand outside this roster REFUSES AT LOAD."* **`Act` has no `via` at all** (`P-03`), so this conjunct was unloadable twice over |
| `{ form: relation, of: subject, holds: heard }` | **no act in this design writes a `heard` relation**, so the conjunct had no producer — `ID-13` committed inside a `requires` cell |

⭐ **AND THE THIRD CORRECTION COSTS THE DESIGN A RESULT IT LIKED.** The `heard` conjunct was what
produced `determine.unheard` — *a bench that determines a matter nobody has pressed is refused.*
**Without a producer for `heard` that refusal does not exist**, and the "hearing precedes judgment"
tempo below now rests on the stratum order **alone**, which is a weaker claim. Registered `P-23`.

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

> ### ⛔ **CORRECTED 2026-09-07 — THE FIVE ROWS CARRIED THREE PRIVATE BAND VOCABULARIES, IN THE
> ### DIRECTORY THAT NAMES A SECOND LADDER AS ITS WEAK POINT.**
> They keyed `writes`/`emits` on `Found · Partial · Nothing`, `Read · Misread · Nothing`,
> `Sound · Wrong · Nothing` and `Seen · Glimpsed · Nothing` — **eight names that are not the
> ladder's**, three bands per row instead of four, across five rows on the page after §B.1 retracts
> exactly this defect for `speak`. **The retraction did not travel one section.**
>
> **Executed rather than argued:** building the `examine` row as it stood and handing it the band a
> margin-graded contest actually returns raises —
> *`'examine' has no `writes` branch for degree 'Success'. Declared: ['Found', 'Nothing', 'Partial']`*.
> `writes_at`/`emits_at` refuse an undeclared degree rather than defaulting, so these rows would have
> raised at the first fold exactly as the coined `speak` bands would have.
>
> **Why the ladder's four and not a ruled exemption:** combat has three bands **by ruling**, because
> it reads a scene rather than a margin. **These five have no provider at all** — nothing routes
> `what persists` or `a disposition` to any subsystem — so nothing can report a non-margin band, and
> `§C.4` forbids a verb declaring a band its subsystem cannot report. If an investigation provider is
> ever built that reads something other than a margin, *that* is when an exemption is earned, and it
> must be argued as combat's was. `Found → Success`, `Partial → Partial`, `Nothing → Failure`, and
> `Overwhelming` is declared because the ladder can return it.
>
> ⚠ **`{ form: path }` is corrected to `{ form: contain_path }` in the two rows that used it** —
> `path` is in no roster and would have refused at load. Two of the five preconditions §B.3.1 calls
> *expressible without inventing anything* were written in a form name the grammar does not carry.

⚠ **THE STRATUM IS THE SOURCE ROW'S, NOT THIS DESIGN'S.** `verb_table.yaml:491` carries
`stratum: "contested_physical"` for `the six investigation acts`, and a draft of this section silently
wrote `social` on all five. **`rosters.yaml` says the strata are ordered semantically and that
*"editing the order changes which acts see which world — that is a game change"*, so moving five acts
two strata later is a game change, unstated.** Kept at `contested_physical`. **The consequence is
worth naming: investigation resolves BEFORE speech in the same season, so what an `examine` finds can
be `tell`-ed at a hearing in the season it was found.** Under the draft's `social` it could not have
been.

```yaml
- verb: "examine"
  stratum: "contested_physical" · eligibility: ["own"]
  requires: "the actor is present where the thing examined is"
  requires_typed: { form: contain_path, of: subject, kind: contain }          # form 3
  contests: "what persists"                                          # vs `retention`
  writes:  { Overwhelming: [], Success: [], Partial: [], Failure: [] }
  emits:   { Overwhelming: ["facet.found"], Success: ["facet.found"], Partial: ["facet.found"], Failure: ["facet.none"] }
  emits_on_refusal: ["examine.impossible"]
  grade: "assumption"
  # COST — "you are witnessed examining" — NEEDS NOTHING. The act emits at a venue; whoever is
  # co-located deposits a claim that you were looking. AX-2 + WITNESS, at zero cost.

- verb: "interview"
  stratum: "contested_physical" · eligibility: ["own"]
  requires: "the actor and the subject are present at the same venue"
  requires_typed: { form: contain_path, of: subject, kind: contain }          # form 3
  contests: "a disposition"                                          # vs obstinacy
  writes:  { Overwhelming: [], Success: [], Partial: [], Failure: [] }
  emits:   { Overwhelming: ["said.given"], Success: ["said.given"], Partial: ["said.given"], Failure: ["said.withheld"] }
  emits_on_refusal: ["interview.impossible"]
  grade: "assumption"
  # COST — "they learn what you are asking" — NEEDS NOTHING, and it is the same mechanism:
  # the SUBJECT is co-located by the precondition, so they always witness the asking.

- verb: "research"
  stratum: "contested_physical" · eligibility: ["own"]
  requires: "the actor holds a live admission to the archive"
  requires_typed: { form: existence, of: subject, kind: Tenure }      # form 1 — an `oblige` or `hold`
  contests: "what the record holds"
  writes:  { Overwhelming: [], Success: [], Partial: [], Failure: [] }
  emits:   { Overwhelming: ["record.read"], Success: ["record.read"], Partial: ["record.read"], Failure: ["record.silent"] }
  emits_on_refusal: ["research.unadmitted"]
  grade: "assumption"
  # ⭐ "EVERY GATE IS A PERSON, SO EVERY GATE HAS A PRICE AND A GRIEVANCE" — the source's own words,
  # and the admission is an EDGE, so the three routes around it (interview an archivist, use a deep
  # channel, steal) are already three existing verbs. No gate mechanism is added.

- verb: "reconstruct"
  stratum: "contested_physical" · eligibility: ["own"]
  requires: "the actor holds claims bearing on the subject"
  requires_typed: { form: own_ledger, of: subject }                   # form 6 — `tell`'s own form
  contests: "what can be inferred"
  writes:  { Overwhelming: [], Success: [], Partial: [], Failure: [] }
  emits:   { Overwhelming: ["inference.made"], Success: ["inference.made"], Partial: ["inference.made"], Failure: ["inference.none"] }
  emits_on_refusal: ["reconstruct.groundless"]
  grade: "assumption"
  # ⭐ `Sound` AND `Wrong` EMIT THE SAME KIND. "A WRONG reconstruction deposits at real confidence
  # and is acted on." This is the purest AX-2 act in the game and the one most worth building first.

- verb: "surveil"
  stratum: "contested_physical" · eligibility: ["own"]
  requires: "the actor is present at the place, for a declared interval"
  requires_typed: none
  requires_typed_note: >-
    form 3 for the place, AND a declared interval, which is `T-n` — the opening act declares its
    term. ⚠ `Tenure` HAS NO `term` FIELD in the tracer (`shape.py:2066-2091`), so the second half
    is UNTYPABLE TODAY. Registered `P-04`; the row is written and the cell is honest.
  contests: "what is done unseen"
  writes:  { Overwhelming: [], Success: [], Partial: [], Failure: [] }
  emits:   { Overwhelming: ["watch.kept"], Success: ["watch.kept"], Partial: ["watch.kept"], Failure: ["watch.empty"] }
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
