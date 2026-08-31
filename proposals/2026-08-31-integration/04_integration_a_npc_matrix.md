# 04 — INTEGRATION, LANE (a): the NPC matrix / season machine into the PR #342 design suite

## Status: PROPOSAL (2026-08-31). Nothing here ratifies on merge.
## Deliverable: what changes in `proposals/2026-08-29-valoria-from-scratch/`, in what shape, at what cost.
## Binding inputs, in precedence order:
## 1. `proposals/2026-08-31-integration/03_corrected_findings.md` — §A struck (12), §B survivors (7), §C corrections (C-1..C-7), §D constraints (4)
## 2. `proposals/_session_provenance/2026-08-29-to-31/CODESHAPE_FORBIDDEN.md` and `11_code_shape.md` §2, §3, §7, §8
## 3. `proposals/2026-08-31-integration/00b_pessimistic_ners.md` — P-1..P-5, and RULE 3 (R binds at playable seats)
## Sources acted on: `2026-08-30-play-space-coverage/` (00_PLAN, 01_the_machine, 08_coverage_matrix, 09_GAP_REPORT) and `2026-08-30-fixes/01`–`05`

---

## How to read this document, and what it is allowed to assume

Every claim below is checkable against the working tree by a reader with no memory of this session.
Where I cite a #342 document I give the section, and where the exact words matter I quote them and
give a line number as of this commit. **A claim you cannot check is a claim you should strike, and a
struck claim voids the change built on it.** That instruction is not decorative: it is exactly what
happened to twelve claims in `03_corrected_findings.md` §A, several of which I would otherwise have
built on.

**What I may not argue from, and did not.** The interpretive frame that opened the source suite —
*a rich option set against an unreachable want is the exercise's most common result* — is struck
(S-1, S-2). So are: *office points the wrong way as a predictor* (S-6), *alignment = none is 5 of 5
bad* (S-4), *rank 1 is 4 of 4* as anything but directional (S-5), *the 22 convergences as
independent* (S-3), *D-4 confirmed by 56 probes* (S-7), and *dominance is the only clean separator*
(S-8). Two of the five source fixes were sized by a headline that S-1 falsifies and by an arithmetic
that C-6 shows double-counts. **Where a change I wanted was carried by one of those, I either
re-derived it on document-internal evidence or dropped it and said so (§5).**

**§D binds every sentence.** The coverage exercise's roster is hand-assembled, elite-heavy (~56 of
~90 registry ids, no stated exclusion rule, depth explicitly proportional to what canon supplies).
**Nothing below is a rate about the play population, and I have written no rate.** Where a count
appears it is a count of documents or of characters in that sample, labelled as such.

**Nothing in either body was executed** (§D). Every "the design produces X" is a reading of a
document, mine included.

**On falsifiers and C-4.** Each change carries a falsifier. Every one of them is either (a) a read
against a named #342 section, or (b) an *offline* seeded probe whose subject is the game — the same
class `11_code_shape.md` §4 licenses for the fidelity comparison harness. **None is an in-engine
check, a validator over the design documents, a freshness gate, or a guard.** That boundary is
C-4's, and it is `11_code_shape.md` §8's own: *"What must NOT be built: validators over the design
documents, freshness checkers, guards on the guards, or any apparatus whose subject is the
repository's own process rather than the game."* I propose none.

---

## 0. What I am integrating

Seven surviving findings from `03_corrected_findings.md` §B, plus the four corrections in §C that
bear on this lane.

| id | the surviving finding | where it is stated | acted on by |
|---|---|---|---|
| **D-1a** | the rank-3 verb gate is an **undeclared second class gate** in a document that declares exactly one | `02 §2.1` against `02 §2.3` | **I-1** |
| **D-1b** | the same gate makes `02 §2.2`'s advancement rule **unreachable** below rank 3 | `02 §2.2` against `02 §2.3` | **I-1** |
| **D-1c** | `mark_salience` reads **one referent kind of the four** `02 §3.1` carries | `04 §4.1` against `02 §3.1` | **I-2** |
| **A-6** | the firsthand salience floor is **ruled and unimplemented**; carrying it into `03` is named as outstanding work | `15` A-6, A-6b | **I-3** |
| **needs** | the exposure formula **closes** an existing interior/world read rather than opening one; `unmet` queries only the actor's own ledger | `07 §1.3` against `02 §6`, `15` A-1b | **I-4, I-5** |
| **act economy** | one act per person stands, unscaled; an office-holder's act count is his **reach**, not his allowance | `09 §1.1` against `14 §8`, adjudicated against `14 §1` | **I-7, I-8** |
| **convergences** | the three the review certifies as genuinely independent: vacancy-by-absence, the Goldenfurt address collision, the buy/no-payment collision | `09_GAP_REPORT` §6 as narrowed by S-3 | **I-9, I-10**, and §1 |

| id | the correction | consequence for this lane |
|---|---|---|
| **C-2** | the act-economy fix's supporting experiment is **confounded** — it uses King Almud's THIN verdict as a discriminator while `08_coverage_matrix.md` PART 4, convergence row #4, records that his verdict *flips with the branch each lane declared* | the conclusion is **re-argued from `14 §1`'s own text** in I-7; the discriminator is not used, and the part of Reading C that was genuinely *chosen* is separated out as I-8 and a live choice (§4.1) |
| **C-3** | E1 is a real but bounded compliance regression, **repairable at type level** by making the venue tuple's existing `convener` field required and non-optional | **I-6**, with the ordering constraint stated |
| **C-4** | an instrument is compliant iff it stays offline and its subject is the game | the standing rule above; and §5 records the two empirical questions I am *not* answering |
| **C-5** | R may be applied only at seats a player can occupy, and playability is undecided | every R line below is written conditionally, and §4.3 records the undecided question rather than settling it |
| **C-6** | the blocked-cores arithmetic double-counts; the totals do not sum to nineteen | the "four characters and three small edits" sizing is **not carried forward**; E1, E3, E4 are judged one at a time on their own warrants, and E3 is dropped (§5) |
| **C-7** | the conferral sweep does not close | I-7/I-8 make establishments load-bearing and therefore *raise the price* of leaving D-6 open. I propose no conferral ruling. §5 records the debt. |

---

## 1. Findings that need NO change, and why each closes

**1.1 The verdict tally (33 RICH / 16 THIN / 4 BLOCKED / 1 SPLIT / 1 SPECTATOR over 55).**
It survives attack — the row counts in `08_coverage_matrix.md` §2.1 sum exactly. It still licenses
no edit. It is a statistic over a hand-assembled sample (§D) and it is a property of the *instrument's
roster*, not of any #342 document. **Closed: a true number about a probe set is not a defect in the
thing probed.**

**1.2 The canon spot-checks — the Grandmaster's name contradiction, Maret Uln as succession fallback,
the Knot-gate aggregate, and stats being null for all five churchmen.**
All four survive as verified. All four are defects in the *roster and canon material used to probe*
the design. **No #342 document names any of these characters as mechanism**; they appear only as
worked examples. **Closed against #342, open against the roster.** The one that has a mechanical
consequence — churchmen with null stats make `03 §4`'s view budget `K = 7 + Focus` uncomputable for
them — is a fact about the probe data, not about the formula.

**1.3 The Goldenfurt address collision.**
Goldenfurt is placed under Kronmark (Crown) in one source and Grauwald (Vaynard) in another; two
lanes hit it independently, and it is one of the three convergences the review certifies as genuinely
independent. It needs no #342 change **because #342 already forbids it**: `01 §1.1` makes containment
a tree and single-parent *on purpose*. A settlement with two parents is not a gap in the substrate;
it is the exact thing the substrate refuses, appearing in the data. **Closed against #342.**
⚠ It is nonetheless load-bearing on I-2's worked arithmetic, which quantifies over a judging set
assembled from Goldenfurt's parish — see I-2's cost line.

**1.4 The Knot TS ≥ 30 gate.**
Five lanes reported it; S-3 shows the gate *and its consequence* were printed in the shared
instrument, so the count carries little independent signal. Separately, `02 §11.2` asks explicitly
that it not be "fixed", `01 §2`'s Ties row declares the asymmetry deliberate and says so *in order
that nobody later fixes it*, and `15` A-4 ruled it. **Closed: the design declared this, and a
convergence that was seeded is not evidence against a declared decision** (P-2).

**1.5 `act_salience`, the act-economy ruling, the needs formulas and the relational derivation as
COMPLIANCE objects.**
The lane review (`02_review_a_npc_matrix.md` F10) checked all five source fixes against
`11_code_shape.md` and found four compliant and one regressive. Those four need no *compliance*
change. Three of them still need *content* changes, for reasons that are not compliance reasons, and
those are I-2, I-5 and I-7. **The compliance question is closed; the design question is not.**

**1.6 The Settlement/Territory relational derivation.**
`04_relational_at_settlement.md` §1.1 derives — from `01 §4` (*Community owns peer judgment and the
admission gate*) and `14 §1.1` (*Settlement is the first rung whose stake is zero-sum across
communities that did not admit each other*) — that belonging at Settlement and Territory is **read
from Community, not conferred there**, and that the absence of a settlement-scale admission gate is
the rung's identity rather than a hole. **That derivation survives independently of D-4's struck
evidence** (S-7) because it cites two documents rather than the probe count. **Closed: the matrix's
EMPTY at those two cells is correct for three of its five sub-questions and needs no fix.**
The fourth sub-question — *is there a way in for a landless person* — I am **not** integrating, and
§4.2 says why.

---

## 2. The changes

Ten changes. **Seven are deletions, restrictions, or the application of a ruling already on the
books.** Two add a formula where a document already names a term it never defined. One adds a single
matching predicate, named rather than hidden. **No change adds an object, an act, a subsystem, a
field on a person, or a stored value** — which is the bar `03_corrected_findings.md` §D sets and
P-5 restates.

Each carries: the document and section it edits · the text or type change · an N/E/R/S line · what it
costs · the falsifier.

---

### I-1 · Delete the rank-gated verb clause. Rank supplies dice; it does not gate a verb.

**Edits.** `02_the_person.md` §2.3, the paragraph beginning **"Reach — verbs."** (line 204). Delete
it. `02 §2.3`'s "Magnitude — dice" block and the anti-leverage sentence that follows stay.

**The change.**

```
option eligibility consults:  remit (14 §1.1) · marks (02 §1) · place (09 §1.4 stratum 1)
                              · the claims the person holds (03 §4.1)
                              · class gates — of which there is EXACTLY ONE: Thread Sensitivity
                          and NOT practice rank.

pool(p, a) = attr[triad_axis(a)] + practice[a].rank + thread_pool          # 02 §2.3, unchanged
```

Every act named as *"added at rank 3"* or *"added at rank 5"* folds back into its base act as a
**declared standard** priced by `10 §2`. The act vocabulary gets shorter.

**Why it is warranted — three document-internal contradictions and a fourth that the source fix did
not use.** Each is checkable by reading two sections side by side. None depends on any coverage
statistic, any verdict, or the control's season.

1. **An undeclared second class gate.** `02 §2.1` (line 141): Thread Sensitivity is *"a **class
   gate** rather than a magnitude: below TS 30 certain verbs do not exist for you at any rank. That
   is P-08's inaccessibility, and it is **the one place this design gates a capability on something a
   person cannot acquire**."* `02 §2.3` (line 204), sixty lines later: *"At `rank ≥ 3` a practice
   adds **verbs to the actor's option list**, and at rank ≥ 5 it adds verbs that cannot be attempted
   at all below that rank."* Two class gates in a document asserting one.
2. **The gate makes the document's own advancement rule unreachable.** `02 §2.2` (line 186): *"A
   practice gains a rank when an attempt at a standard **above its rank** resolves and one of: it was
   witnessed by a person holding the practice higher, or it failed at a cost the person actually
   paid. There is no experience clock."* For every verb the gate withholds, attempting above your
   rank is precisely what the gate forbids. **The ladder from 0 to 3 has no rungs**, by the two rules
   read together.
3. **`01 §1.4` refuses exactly this discontinuity**, in the other structure: *"there is nothing to be
   discontinuous: the same op, the same aggregation, the same read."* One rank buys a whole verb;
   the two below it buy nothing.
4. **The resolver document already asserts the behaviour this edit restores, and it owns the
   question.** `10_resolution_surface.md` §1.2, line 33, verbatim: *"Practice ranges 0–7, where 0 is
   'never trained' — **an untrained attempt is always legal (T1: a person with no office, and no
   training, can still try), it is just a small pool.**"* This is the strongest of the four and the
   source fix did not use it. It converts I-1 from a design change into **a choice between two
   documents that already disagree, decided in favour of the one that owns the resolver.**

**N/E/R/S.**
- **N** — cut this edit (i.e. keep the gate) and you lose *the only advancement route the design
  has*, for every practice a person does not already hold at 3. `02 §2.2` is the whole of
  progression; the gate closes it against the people furthest from it.
- **E** — the object count **falls**. One clause deleted; a set of "rank-3 verbs" and "rank-5 verbs"
  folds into their base acts. Nothing is added.
- **R** — *conditional, per C-5.* If a player can occupy the seat of a person below rank 3 in a
  practice, this widens their option set and the R claim is live. **Whether such a seat is playable
  is undecided and I do not settle it** (§4.3). Where it is not playable, this is a
  characterisation claim about NPCs and R does not bind — but N and the four contradictions above
  do, and they are what carries the change.
- **S-UP** — unchanged. **S-DOWN** — improved: an opportunity that requires a practice verb now
  reaches a person who holds the practice at 0, at a worse pool, which is the design's own stated
  intent in `10 §1.2`.

**What it costs.**
1. `02 §2.3`'s own N-line loses half its subject. It claims *"the capable person changes the option
   set and the pool source, never adds a flat bonus."* After I-1 only the pool-source clause is true
   of capability. The option-set clause survives as the **office** claim, which is `14 §1`'s, and
   `14 §1.2` states it there already. Somebody must edit doc 02 rather than leave two documents
   disagreeing — which is precisely what A-6b records happening to A-6.
2. The worked example in `02 §2.3` (Free Master vs journeyman, `commission on speculation`) must
   re-home to a **guild** gate: `04 §4.2`'s admission machinery, six persons' stances and a grade
   mark. That is a better home — a gate with a holder, a price and a grievance — but somebody must
   then write which guild rules gate which standards, and the risk is that this becomes a table of
   authored permissions rather than a dispensation contestable at the guild's standing date.
3. Doc 10 inherits the whole of *how hard is this for someone who cannot do it.* **It already has
   the machinery, which is why this cost is smaller than the source fix estimated:** `10 §2.1` line
   76 supplies a hard-impossibility form — *"If Obstacle > 2×Pool … the attempt is not merely
   unlikely, it is impossible, and the resolver refuses to roll it at all."* So "hopeless" is
   expressible without a verb gate. What is **not** established is whether a master's standard
   actually lands above that ceiling for a rank-0 attempt.

**Falsifier.** Compute `obstacle(the Free Master's commission standard)` per `10 §2.1` and compare it
to `2 × Pool` for an unpracticed attempt (`Pool = attr + 0`, so 1–7, ceiling 2–14). **If the standard
lands below the ceiling at a materially non-trivial success probability under `10 §1.3`'s table, I-1
has converted a hard gate into a soft one and is wrong as stated** — and the remedy is then to raise
that standard's resistance pool, never to restore the verb gate. Second falsifier: exhibit any verb
currently gated at rank ≥ 3 whose *object does not exist* below rank 3 — a verb that cannot be
re-expressed as a standard of a base act. One such verb defeats the "fold it back" half of I-1.

---

### I-2 · `mark_salience` → `act_salience`: read all four referent kinds, and give the attention floor the same term.

**Edits.** `04_hearth_and_community.md` §4.1 — the `publicity` block (lines 415–419) and the `θ(p)`
term inside `hears()` (line ~407). Consequentially: `04 §12` challenge 3, and the reasoning (not the
ruling) of `15` **B-3**.

**The change.**

```
referents(act) = marks(actor) ∪ { proposition(act) } ∪ objects touched ∪ { place }
                 — exactly 02 §3.1's four referent kinds, no new kind

act_salience(act) = 1 + 0.2 × | { r ∈ referents(act) : ∃ p ∈ JS(act) with |stance(p,r).valence| ≥ 3 } |
publicity(act)    = venue_factor × √(witness_count) × act_salience(act)      # otherwise unchanged
θ(p, act)         = θ(p) / ( 1 + 0.2 × | { r ∈ referents(act) : |stance(p,r).valence| ≥ 3 } | )
```

**Why it is warranted.** `02 §3.1` establishes **one** stance table over four referent kinds —
Person, Faction, Proposition, Place — and argues at length that fusing them is correct *"because
every consumer reads the same two numbers"*, listing the consumers. Publicity is a consumer and it
reads one kind. So an act is audible in proportion to *who did it* and not at all in proportion to
*what it was about*. For a person carrying no house name, no grade and no stigma the term is
`1 + 0.2 × 0 = 1.0` for every act of their life, and `04 §4.1`'s own band table then reads *"< 0.5 —
the hearth, and whoever holds a Knot."* **This is a formula reading one field of four, checkable by
holding `04 §4.1` beside `02 §3.1`.** It does not depend on the control's season, which C-6's sibling
finding F8 shows graded its own homework.

**Compliance, stated explicitly because a cold reader will attack it here.** `act_salience`
quantifies over other persons' stances. That is legal **because publicity is computed in P6 WITNESS,
not in P4 CHOOSE** — `09 §1.2` puts `choose(person, view)` in P4 and event fan-out *"by presence and
channel; `witness` per person"* in P6. `resolve` and the fan-out take the world by signature
(`11_code_shape.md` §2); `choose` does not, and nothing here is read inside a decision function.
`act_salience` is **computed per act and never stored**, so it is not the forbidden *stored
aggregate, norm, density, unrest or reputation field*. And it does not broadcast: `04 §4.1`'s
judging-set deposits remain per-person and divergent, so `witness(Person, Event)` is untouched and
consensus broadcast stays a type error.

**What is preserved.** `15` B-3 ruled `mark_salience`'s second effect ALLOWED because *"without it a
house name changes how you are judged but not how much you are talked about."* **That ruling
survives intact** — marks are the first of the four clauses, unchanged — so Maret Uln's transgression
still travels further than her neighbour's and a Duke still cannot act quietly. What changes is that
a mark stops being the *only* way into the sum. This **improves** `04 §12`'s own self-flagged
weakness, which is that `mark_salience` is *"an addition to the substrate's account of marks, not a
consequence of it."* After I-2 it is a consequence of `02 §3.1`.

**N/E/R/S.**
- **N** — cut it and an unmarked person is permanently inaudible in both directions whatever they do,
  so no act by such a person can ever produce a consequence that reaches a person who could respond
  to it. The lost possibility is *the ordinary person becoming politically visible by what they did
  rather than by what they are.*
- **E** — the object count is unchanged; one term is generalised and one special case is removed from
  each of two places (publicity read one kind; the attention floor read none). Vocabulary shrinks by
  one name (`mark_salience` goes).
- **R** — *conditional, per C-5.* At a playable ordinary seat this converts a wall into a fork
  (spend a root, and to whom). At an unplayable one it is characterisation. **N carries it either
  way**, because the defect is a formula reading one field of four.
- **S-UP** — improved: an act touching a contested proposition now reaches persons at a rung above
  the actor's, which is the precondition for their demand being filtered by a named person rather
  than never arriving. **S-DOWN** — improved symmetrically through `θ(p, act)`: news about something
  a postless person cares about now reaches them.

**What it costs.**
1. **Compute, and it is an inner loop.** `act_salience` quantifies over `JS(act)`, which `04 §4.1`
   already did — but `θ(p, act)` now varies per person **and** per act where θ was per person.
   `09 §10` budgets `≤ 17,600` acts a tick and `~2 × 10⁷` view comparisons; this multiplies an inner
   term. **I am not asserting it fits.** `11_code_shape.md` §9 already says the view-budget question
   *"is an empirical question this document cannot answer by reasoning"*, and it is the same question.
   §5 records it as an open empirical item, measurable offline.
2. `04 §12`'s challenge 3 must be rewritten. The behaviour survives; the argument for it does not.
3. **The dependency on the parish ruling.** `act_salience` quantifies over `JS(act)`, and the source
   fix's worked numbers assume an ordinary Goldenfurt person's judging set is her parish
   congregation — whose membership rule is presence over a district, which one lane showed cannot
   coexist with `01 §1.1`'s single-parent containment for a hearth already inside a guild community.
   **Resolve it the other way and there is no judging set for `act_salience` to quantify over in
   that worked case.** The formula change is independent of the ruling; the worked numbers are not.
   This is the largest single dependency in I-2 and it is somebody else's ruling.

**Falsifier.** Compute `publicity` for an act with **zero** contested referents at a private
dwelling: `venue_factor 0.2 × √(3 witnesses) × 1.0 = 0.35`. **It must stay below `04 §4.1`'s 0.5
band.** If any act with no strongly-held referent rises a band under the new term, the term has
become a floor rather than a generalisation, and I-2 is a notability stat in disguise — which
`04 §11`'s refusal of a prestige currency forbids. Second falsifier: if `act_salience` and the old
`mark_salience` produce the same band for **every** act in a seeded sample, the generalisation is
inert and costs compute for nothing.

---

### I-3 · Apply A-6's firsthand salience floor to the document that owns the formula.

**Edits.** `03_knowledge_telling_investigation.md` §4, the `salience(c)` block at line 336.

**The change.**

```
salience(c) = recency × confidence_live × relevance × stanceweight            # told_by, inferred — UNCHANGED
salience(c) = max( that product, recency(c) × confidence_live(c) )            # firsthand ONLY
```

**Why it is warranted, and why this is the cheapest change in the document.** This is not a proposal.
`15` **A-6** ruled it, and **A-6b** records in the register itself that it never landed: *"the
accepted half of A-6 is a ruling with no owner in the design, and a session implementing salience
from doc 03 would build the clamp and never see this row. **Carrying it into 03 is outstanding work,
not a settled fact.**"* Direct read confirms A-6b is still accurate: `03 §4` line 336 is still the
flat product `recency × confidence_live × relevance × stanceweight`, with the 0.05 clamp and no
`max`. **The only thing I-3 does is make the tree match a ruling it already contains.**

**N/E/R/S.**
- **N** — cut it and `01`'s promise that *"correction comes from collision with the world"* cannot be
  kept for the case A-6 accepted: a person with a hard stance cannot surface a thing they saw
  themselves. What is lost is *walking into the room and seeing it.*
- **E** — one `max` on one source class. Nothing added, nothing named.
- **R** — not applicable as a fork; this changes a ranking, not an option set. C-5's caution does not
  arise.
- **S-UP/S-DOWN** — unchanged directly. Indirectly S-DOWN improves, because a firsthand claim about a
  distant event now competes for the view budget.

**What it costs.**
1. **It widens the gap A-6b left open, and makes it more urgent rather than less.** With firsthand
   floored and testimony still under the 0.05 clamp, the distance between *what you saw* and *what
   you were told* grows — so `09`'s original case, *a sixty-year-old revelation must move people who
   do not want to be moved*, gets **harder**. I-3 does not answer that half and must not be reported
   as if it did. A-6b names the likely shape (corroboration lifting a claim past a hostile stance
   weight) without adopting it; I adopt nothing.
2. **On its own, I-3 nearly does not work.** A floored firsthand claim competes against the person's
   *other* floored firsthand claims under `03 §4`'s budget `K = 7 + Focus`. What carries it into the
   working set is I-1, through the `relevance(c, q)` term: relevance is measured against the pending
   decision, and the pending decision is drawn from the option set. **I-1 and I-3 are one change in
   two documents; shipping I-3 alone moves very little.**

**Falsifier.** A-6b's own objection, run as an offline probe: construct a person holding **more than
K** recent high-confidence firsthand claims — the investigator the game is about. **If the floor
changes no inclusion outcome for that person, I-3 is inert for exactly the character it was meant to
serve**, and the real fix is at the budget, not the floor. A-6b predicts this and says the divergence
*"widens the more the person has seen."*

---

### I-4 · Split `exposure(edge)` into a true value and a per-observer estimate — the same split `rarity` already has.

**This is the lane's strongest compliance argument and it should be read first.** It is the only
change here that **removes** a read from a decision function rather than adding one.

**Edits.** `07_alignment.md` §1.3, the `exposure(edge)` block at line 152.

**The defect, by direct read.** `07 §1.3` as written:

```
exposure(edge) = Σ over persons q holding a claim about it of
                 confidence(q's claim) · hostility(q → the proposition)
```

The outer sum ranges over **every person in the world who holds a claim**, including persons the
subject has never met, and the summand reads *their* confidence and *their* hostility. Under `15`
**A-1b**'s three-way distinction — *"world / view / another agent's interior … the third is readable
by nobody except through a claim"* — this is a read of other agents' interiors, at no cost, by
whoever consults it.

**It reaches a decision function, and `07 §1.3` names the consumer itself.** Its own loop line lists
exposure as *"consumed by judging sets, by **requisition** (you cannot ask a man to act openly for a
faction he must hide), and by the derived exposure read."* Requisition is an act: a person choosing
whom to ask. That choice happens in `choose(person, view)` — `09 §1.2` P4 — which by
`11_code_shape.md` §2 **has no `World` parameter**, *"not a masked world, not a read-only world, not
a world behind an accessor."* A covert faction's leader deciding whom to requisition, reading
`exposure(edge)` as written, has a world in scope inside a decision function.

**The precedent is in the tree and it is exact.** `02 §2.2` imposes precisely this split on `rarity`,
and says why, in the document's own words: `rarity_true` *"is readable by **no agent**"*; any person
reasoning about scarcity reads `rarity_est(practice, rank, node, observer)`, *"built from that
observer's own claims about who holds what."* `02 §2.2` calls the missing split **"a leak"** and
attributes the requirement to A-2. **`07 §1.3` did not get the split.** It is the same object, the
same adjudication, and the same omission, one document over.

**The change.**

```
exposure_true(edge)      = Σ over all q holding a claim: confidence(q) · hostility(q → prop)
                           — the world's value. Readable by the RESOLVER and by nobody else.
                           Consumed by judging sets and by P5 outcome computation.

exposure_est(edge, p)    = Σ over q such that P'S OWN LEDGER holds a claim that q holds a claim
                           about the edge, of
                             confidence(p's claim about q's knowing) · hostility_as_p_reads_it(q → prop)
                           — the only exposure any agent may read, including in `choose`.
```

**What this buys that is not compliance.** Both the paranoid and the complacent fall out with no
trait: a person whose ledger over-names his enemies carries a crushing exposure over a secret nobody
is chasing; a person whose ledger is empty walks into an investigation feeling nothing. Neither
needed a personality field, and `02 §3.2` has already cut every trait but two.

**N/E/R/S.**
- **N** — cut the split and *being wrong about how exposed you are* becomes impossible. Every covert
  actor knows exactly how blown they are, so infiltration has no tension, an informer's existence is
  self-announcing, and `07 §1.3`'s own N-line (*"no infiltration, no informers, no Burned, no cover
  identities"*) is half lost — not because avowal was cut, but because the secret's holder is
  omniscient about it.
- **E** — one function becomes two names over the same arithmetic, and one of them is *restricted*.
  This is the same delta `02 §2.2` already paid for `rarity`; the vocabulary grows by exactly the
  suffix pair the tree already uses.
- **R** — not a fork; it removes information from a decision, which changes what forks *feel* like
  rather than what they are. C-5 does not arise.
- **S-UP** — unchanged. **S-DOWN** — unchanged.

**What it costs.** `07 §1.3`'s covert-faction ceiling argument (*"a covert faction's capacity is
bounded by its members' Bonds"*) reads the **true** value at the world side and is unaffected; if a
later reading shows that argument was implicitly using the estimate, the ceiling changes and would
need re-deriving. And the split creates the ordinary hazard of any true/estimate pair: two functions
that can drift. `02 §2.2` already accepted that cost for `rarity`; I am not proposing a guard against
it, because a guard here would be apparatus (§0's C-4 rule, `11_code_shape.md` §8).

**Falsifier.** Enumerate `07 §1.3`'s consumers and locate each in `09 §1.2`'s phase list. **If every
one of them turns out to sit in P5/P6 — that is, if no decision function reads exposure at all — then
the leak I claim does not exist and I-4 is unnecessary**, reducing to a clarification. My reading is
that `requisition` is chosen in P4 and therefore reads it; that reading is the thing to attack. Second
falsifier: if `exposure_est` and `exposure_true` coincide for every actor in a seeded probe, the split
is inert and the design was already safe by accident.

---

### I-5 · Both polity need terms emit `(proposition, urgency)` pairs; urgency is ruled `[0,1]`; `unmet` is defined.

**Edits.** `02_the_person.md` §6 — the `COMMITMENT` and `EXPOSURE` blocks, and the `0..5` range note.

**Why it is warranted — a two-document contradiction, in the same class as D-1a/D-1b.**
`05_up_stroke.md` §1.1, line 22, verbatim: *"A need is a pair `(proposition, urgency)` where the
proposition is a **specific change to some container's terms** that would satisfy it, not a mood."*
`shortfall(p, prop) = urgency(prop) − reach(p, prop)` ranges over that proposition, and
`petition(prop)` enters `own_acts(p)` only when `shortfall > 0`. **`02 §6`'s COMMITMENT and EXPOSURE
blocks emit a bare `urgency` and no proposition.** So for those two terms `shortfall` has nothing to
range over and `petition` — the design's entire up-stroke — never enters the act menu from them.
That is checkable by holding `02 §6` beside `05 §1.1`, and it explains why a figure (`0.91`) appears
beside a duke's name in `05 §1.1` with nothing deriving it.

Two further preconditions are settled minimally rather than left to a second implementer:

**(a) Range.** Four sites, three ranges: `04 §1.2` computes `clamp(0, 1, (2.0 − margin)/2.0)`;
`05 §1.1` compares urgency against a reach that is an expectation in `[0,1]`; `13 §1` reads the same
object; `02 §6` says `0..5`. **Ruled: urgency is `[0,1]`.** The unbounded tail above 1.0 belongs to
`subsistence` alone, because only the body can produce a want that outranks every stance a person
holds — which is `04 §1.2`'s N-line. `02 §6`'s `0..5` is retained as a **display band**,
`band = round(5·u)`, so existing citations still resolve. This is the smallest available choice:
three of the four sites already use `[0,1]`.

**(b) `unmet` needs a predicate that does not exist.** `02 §6` says *"`unmet` = 1 if the person's
LEDGER holds a claim that p is unsatisfied"*, and **"unsatisfied" is defined nowhere in #342.**
`08 §1.1` gets *collision* for free (assertion and denial collide because `when` is a mandatory
interval) but collision is not satisfaction. So:

```
unify(c, P)  — claim row c and proposition P agree on (subject, predicate, when∩, scope∩)
               and differ only in mood.  Existing tuple, existing interval intersection.
agree(c, P) ∈ [0,1] — 1 if P's value is atomic and c asserts it; 0 if c asserts otherwise;
                      |c ∩ P| / |P| if P's value is a set or a quantity.
unmet(p, P) = 1                                if p's ledger holds no unifying row
            = 1 − confidence(c) · agree(c, P)  for the highest-confidence unifying row c
```

**This is the only genuinely new machinery in the whole lane, and it is a predicate, not an object.**
Stating it is not optional: a session implementing `need(commitment)` from `02 §6`'s pseudocode alone
will invent an incompatible one. **It is not an addition under P-5** — it is the definition of a term
`02 §6` already uses.

**Compliance.** `unmet` queries **only the actor's own ledger**; the default when no row exists is
`1`, which is `11_code_shape.md` §2.1's rule that *"absence of a claim must produce absence in the
view, never a widened interval."* Nothing is stored — `02 §6`'s own line, *"needs are never stored"*,
is unchanged. **Both terms read the view, per A-1**, and the EXPOSURE term reads it through I-4's
`exposure_est`, which is what makes I-4 a precondition of I-5 rather than a sibling.

**N/E/R/S.**
- **N** — cut it and a commitment edge is inert: joining a faction changes what a person may be
  *asked* and never what they *want*. Every magnate, churchman and movement leader is motivated by
  their larder and their rank alone, and `07 §1.2`'s `burden` term (*cost to the member's computed
  need*) has nothing to read. The lost possibility is **any politics that is not hunger.**
- **E** — two formulas where two prose sketches sat, one range ruling that deletes a
  disagreement between four sites, one predicate. **No object, no act, no field.**
- **R** — the two hazard classes emit differently-shaped propositions: a term hazard emits a
  container-facing OUGHT that routes to `petition`; a concealment hazard emits a private proposition
  naming one person, which `05 §6.2` says is satisfiable by grace only, and which routes to `tell`,
  to requisition, to purchase, or to force. **Same formula, two act shapes.** *Conditional per C-5*
  as to whether either seat is playable.
- **S-UP** — this is the change that makes S-UP work at all above subsistence: without emitted
  propositions, `shortfall` cannot originate a petition from a polity need, so a demand that is not
  hunger has nothing to travel. **S-DOWN** — a published dispensation now generates a need in a
  person who has heard of it and none in a person who has not, which is `06`'s reach machinery
  acquiring a motivational expression.

**What it costs.**
1. **`loss(h)` runs `opening_set` a second time per hazard per person per tick.** A settlement of
   individuated persons under three live dispensations enumerates options four times instead of once.
   Cohorts absorb most of it — but a crisis is exactly when a cohort individuates, so the cost spikes
   when the tick is already expensive. Same class of open empirical question as I-2's; see §5.
2. **Fractional `agree` makes a proposition's granularity mechanically load-bearing.** A proposition
   written over twenty-one guild gates behaves differently from one written over "the caste order",
   and nothing in #342 governs how coarsely a faction's proposition is written. That is a real
   authoring lever with no editorial rule behind it — and I am **not** proposing one, because an
   editorial rule over design documents is the apparatus C-4 forbids.
3. **It makes A-6b's unresolved testimony half load-bearing on motivation, not merely on belief.**
   Once `unmet` is a ledger read, a *contradicting* claim from a hostile source runs into `03 §4`'s
   0.05 clamp — so a movement leader's comfortable lie is attenuated on the way out by the same
   mechanism that buries every inconvenient truth. **I-3 does not fix this and I-5 makes it worse.**
4. **The range ruling touches published text.** A reader who takes `02 §6`'s `0..5` as the quantity
   rather than the display band will over-weight every need fivefold. Retaining it as a band is
   deliberate so citations resolve; deleting it would be cleaner and would break them.
5. **Division by zero at the bottom.** `worth(p)` is the denominator of every exposure row, and a
   person distrained, expelled and unhoused has an empty `opening_set`. `worth(p) = max(EV(opening_set),
   subsistence_floor(p))` is what stops it; the floor is load-bearing, not defensive punctuation.

**Falsifier.** `unify`'s two failure modes, run offline on a seeded ledger: **over-match** — a
vaguely related rumour discharges a faction's proposition, so committed characters go quiet after
hearing gossip; **under-match** — a directly satisfying claim leaves `unmet = 1`, so every committed
character sits permanently maximal. **Either observation falsifies the predicate as specified.** This
is the one place in the lane where a second implementer will build something incompatible, and it is
where I-5 should be attacked first.

---

### I-6 · Make `Venue.convener` REQUIRED and NON-OPTIONAL — *then* widen `Petition.respondent_container` to `respondent_venue`.

**Edits, in this order.** (1) `14_office_and_upper_rungs.md` §5, the door tuple. (2) `01_substrate.md`
§5.1 line 392, `05_up_stroke.md` §1.2 (the `Petition` block) and `05_up_stroke.md` §3.1 (the `carry`
precondition, line 173).

**The change.**

```
# step 1 — 14 §5
Venue door := (convener: Person — REQUIRED, NON-OPTIONAL, exactly one, enter, speak,
               admissible_source, attendance_cost)
   — a venue with no named person as convener is not constructible.

# step 2 — 01 §5.1, 05 §1.2, 05 §3.1
Petition( petitioner, proposition, respondent_venue, backing )
   respondent_venue : a Venue in 14 §5's sense, whose `container` field may be a
                      containment node, an office, or NONE.
carry(c, P) precondition: c holds STANDING at respondent_venue(P)
```

**Why it is warranted, and why the ordering is the whole of C-3.** `15` **B-11** accepted a price
deliberately: *"'The Dicastery decided' is permanently inexpressible … **You cannot address a
petition to a Dicastery**; you address it to a person, and that person can drop it. That is T1
refusing to be talked around, and **the fiction must never render an institution as a speaker.**"*
The first half is right and must stand. The second half does not follow from it: `Petition` names a
container for one reason — the container carries the standing date and the door — and `14 §5` already
parameterises venues by **convener and date**, not by node. `15` **B-5** already ruled that *"a
private negotiation is a venue with no container — ALLOWED."* So the containerless venue is not new.

**But the widening as filed is a compliance regression**, and this is C-3 stated precisely. Before
the widening, *you cannot address a Dicastery* was enforced by the `Petition` **type** demanding a
container. After it, the type permits it and the discipline is a sentence — which is the class
`11_code_shape.md` §8.1 exists to forbid: *"A property enforced by naming can be spelled around; a
property enforced by a type cannot."* **The repair is available and costs nothing: `14 §5`'s door
tuple already carries `convener`, and every one of its nine table rows already names a person.**
Making it required and non-optional restores the invariant at type level — a petition names a venue,
a venue names a person, that person can drop you. **The convener requirement must land first or in
the same edit; landing the widening alone is the regression.**

**N/E/R/S.**
- **N** — cut the widening and every office cluster in the setting (four Dicasteries, the
  Löwenritter, every trans-settlement guild) is politically unaddressable, so the up-stroke has no
  legal object against the most institutionally mature bodies in the world. What is lost is
  `05 §5.1`'s stated point: *"the specific injury of being heard and refused."* Being refused becomes
  indistinguishable from having nowhere to ask.
- **E** — one field is retyped in three documents and one field is made required in a fourth. Object
  count unchanged. `carry`, `forward`, `amend`, `bundle` and `drop` are untouched.
- **R** — the door is unchanged, so a layman still needs an intercessor with standing at a
  Dicastery — strictly harder than a settlement petition. Nothing about the power balance moves; only
  the legality of asking does. *Conditional per C-5* as to which of these seats is playable.
- **S-UP** — this is an S-UP change and nothing else: it is the only one here that adds a
  destination a demand may travel to, and the filter at that destination is still a named person.
  **S-DOWN** — unchanged.

**What it costs.**
1. **Three documents, not one.** `respondent_container` appears at `01 §5.1` (line 392),
   `05 §1.2` and `05 §3.1` (line 173). A partial edit leaves the substrate and the up-stroke
   disagreeing about the petition object's shape.
2. **Forum-shopping gets materially cheaper across the whole game.** A petitioner refused at one
   venue may try a cluster venue. `08 §2`'s rung-4 objection (*this chamber may not hear it*) is the
   right counter and exists — but **nobody has costed how a first refusal enters a second venue's
   record**, and `08 §6`'s recorded defeat plus its pattern counter may now fire in rooms they were
   not written for. This is new surface, unpriced, and I am not pricing it.
3. It moves a design claim from prose into a type, which is the intended direction, but it also means
   any future venue that genuinely lacks a convener becomes unrepresentable. That is the point, and
   it is also the falsifier.

**Falsifier.** Sweep `14 §5`'s venue table and `08 §10`'s tuple for a body that decides and has **no
person who can be named as its convener**. `14 §5`'s nine current rows all name one — the Duchess, the
Praefect, the Cardinal, the guild warden, the chapter master, the King. **If a real body exists that
decides with no convener, the type cannot be made total, and E1 as repaired reintroduces exactly the
institutional speaker B-11 refused.** Second falsifier: if making `convener` required forces any
existing row to name a person canon does not supply, the repair has pushed a mechanical requirement
into the roster — which is a cost, not a defect, but it must be counted.

---

### I-7 · Rewrite `14 §8`'s worked ducal season with per-actor attribution. `09 §1.1` stands, unscaled.

**Edits.** `14_office_and_upper_rungs.md` §8 (line 562 onward) — rewritten, not annotated.
`09 §1.1` is **unchanged**, which is the point.

**⚠ Re-argued, because C-2 struck the support the source fix leaned on.** `02_the_act_economy.md` §2
called the coverage exercise *"the decisive argument"* and used King Almud's THIN verdict to falsify
Reading A. **That argument is not available**: `08_coverage_matrix.md` PART 4, convergence row #4, records the
act economy as a convergence in which *"three lanes declared a branch before writing and each states
what flips: Almud THIN↔RICH, Himlensendt THIN↔RICH."* His verdict is a function of the branch the lane chose, so it
cannot discriminate between branches. The establishment correlate was extracted post hoc.
**I do not use it.** I also do not use *"office points the wrong way"* (S-6, struck by its own
numbers) or any share of the roster (§D).

**What the conclusion rests on instead — `14 §1`'s own founding claim, read against `14 §8`.**

`14_office_and_upper_rungs.md` line 13, verbatim: *"An office adds **no verb to the game**. … A Duke
and a hamlet fisher run the same `choose(person, view)` over the same act vocabulary. They differ in
three quantities and nothing else: **remit**, **reach**, and **binding**."*

An **act allowance** would be a fourth quantity. So the reading in which an office-holder's budget
scales with office is refuted **by the document that would have to contain it**, with no reference to
any verdict, any lane, or any statistic. `01 §1.4` refuses the same shape in the other structure —
*"there is nothing to be discontinuous: the same op, the same aggregation, the same read"* — and
`09 §1.1`'s N-line says what a scaled budget deletes: *"A Free Master who can both stand for the guild
seat and answer his Einhir cousin's petition is never Southern Einhir in any way that costs."* A Duke
who can both hold his court and commit to breaking the caste order is never conflicted either, and
that is at the top of the ladder, where the design most wants the collision.

**So `14 §8` as written contradicts `14 §1`, and must be rewritten or deleted whichever branch is
taken.** That much is settled and does not depend on the discriminator.

**What follows with no ruling at all.** `14 §1` defines `establishment(o)` as *"the named persons the
office employs."* `01 §2` says *"Persons act. Nothing else does."* `09 §1.1` gives every person one
act. **Therefore the reeve, the granary keeper, the ducal proxy, the riders and the watchmen each get
one act a season, chosen from their own view.** This is a consequence of three sentences already in
the suite, not a proposal. And the reason they mostly serve is also already written: `14 §1.3`'s
**upkeep** fills an establishment member's larder from the office's stake, so his `need(subsistence)`
is answered by the post and threatened by failing it. `14 §1`'s own line — *"an unpaid establishment
… does not disperse, it becomes a faction and treats plunder as wages"* — has had no mechanism
producing it, and under this reading it is produced by construction.

**The rewrite.** `14 §8`'s seven named acts, re-attributed:

| the passage's act | who spends it |
|---|---|
| `convene`s the Grauwald court and orders its items | **the ducal proxy** — `05 §3.1` names the proxy, not the Duke, as that court's convener |
| `issue`s a levy dispensation over five territories | **the Duke.** Publication is not further acts of his: `06` deposits by presence and channel |
| `dispatch`es two riders | **the Duke, once** (see I-8); the second rider goes where his own view sends him, or does not |
| `confer`s a sub-remit on a reeve | **the Duke**, and irreducibly his |
| `revoke`s a benefice he cannot revoke | **the Duke** |
| `carr`ies a bundled petition into the Realm's standing date | **the Duke**, and one of the Realm's seat items |
| `commit`s at degree 4, avowed | **the Duke**, and irreducibly his |

Six of the seven are the Duke's own and he has one. **The season still contains about ten acts; it
contains more. Ten acts, nine actors, one Duke.**

**Two acts nobody can perform for you**, and stating them is what makes the reading sharp rather than
deflationary: **`confer`/`revoke`**, because `14 §1` carries the conferrer's name as the source of
the `post:` mark, so a herald conferring in your name confers his own nothing; and **`commit`**,
because a faction edge is a person's own commitment at their own degree. **The undelegable acts are
exactly the ones that change who serves you and who you are.**

**N/E/R/S.**
- **N** — cut `09 §1.1`'s unscaled one act and you lose priority, therefore every dilemma, and you
  lose it *first at the top of the ladder*. Cut the re-attribution instead and `14 §3.1`'s reach
  becomes a number rather than a roster, `14 §1.2`'s *"choosing which of your people performs the act
  is the whole of a leader's tactical choice"* has nothing to attach to, and the difference between a
  large office and an **obeyed** one is inexpressible.
- **E** — a rewrite of one worked passage. **No rule is added.** The "derived count" is an
  observation about the same roster `14 §3.1` already keeps, not a new field: one list, two questions.
- **R** — a magnate's fork is `{issue, dispatch, confer, determine, carry, commit}`, and the shapes
  differ: `issue` is broad and uncertain (compliance is nine people's own choices, resolved by `06`);
  `dispatch` is narrow and near-certain but degrades the man and coarsens every node you did not
  reach. *Conditional per C-5 — **crown playability is explicitly undecided** and I do not settle it.*
- **S-UP** — unchanged. **S-DOWN** — improved, and this is the change's best structural property: an
  opportunity now reaches a *reeve* rather than a duke's abstract capacity, and the reeve is a person
  with a larder and kin in the hamlet he is collecting from.

**What it costs.**
1. **The player holding a Duke does not get a big turn.** He gets one act and a personnel problem.
   Some of that reads as a demotion and there is no way to soften it without becoming the scaled-budget
   reading.
2. **It converts a roster gap into a mechanical gap.** An office whose establishment canon does not
   name produces one act a season. That is honest and it is expensive: the gap report records that
   canon names no guild warden and two Cardinalates are unfilled. **Every office must name its
   establishment or accept being a one-act office.** The mitigation is that this is cheap authoring —
   a list of names — and not a mechanism.
3. **It shifts the upper-rung game from decrees to staff.** A player who came for proclamations gets a
   game about who is reliable in Grauwald this year. That is a real change of genre at the top of the
   ladder and it should be stated as one rather than smuggled.
4. **It costs nothing in compute.** `09 §10` already budgets one `choose` per person per tick
   (`≤ 17,600` acts, *"≤8,000 persons + ~9,600 cohorts, one each"*). The re-attribution spends no
   additional call; it re-attributes calls already being made.
5. **C-7's debt.** Establishments become load-bearing, establishments are filled by `confer`, and
   conferral in the Church is a cycle with no external root (D-6). **I-7 raises the price of leaving
   D-6 open and does not pay it**, and C-7 records that the sweep concluding conferral need not be
   person-rooted does not close.

**Falsifier.** Enumerate a magnate's season and count the acts that are (a) not delegable to a named
establishment member and (b) not `confer`, `revoke` or `commit`. **If that count exceeds one for any
office in the roster, the unscaled one-act rule is unsustainable at the top of the ladder on the
suite's own terms** and I-7 is wrong. Second falsifier, and the sharper one: `14 §8`'s own table
asserts that a fisher's `requisition` and a Duke's `dispatch` are *"the same call, on an
establishment member."* **Under any reading in which a dispatch costs less than a requisition, that
sentence is false as written** — so the falsifier for I-7 is also the argument for I-8.

---

### I-8 · `dispatch` costs the holder one act and the member one act, and names one person.

**Edits.** `14_office_and_upper_rungs.md` §1.1, where `dispatch` is defined as requisition on an
establishment member.

**The change.**

```
dispatch(holder, member, act) :
   costs the HOLDER  one act — his own, for the season
   costs the MEMBER  one act — theirs, for the season
   the member still runs their own choose:  comply_pressure = claim_weight − strain   (04 §1.4)
   one dispatch names ONE person.
```

**Why it is warranted, separately from I-7.** This is the part of the act-economy reading that was
genuinely *chosen* rather than forced, and it should be labelled as such. Two document-internal
supports:
1. `14 §8`'s table already asserts `requisition` and `dispatch` are *"the same call."* `04 §1.4` owns
   requisition and prices it on the member's side. **Under a free or cheap dispatch that assertion is
   false**, because one call would cost a season and the other a fraction of one.
2. `05 §3.1` already charges an office operation a whole act — `compose_agenda` costs *"one of v's own
   acts for the season."* The precedent for "an office operation costs your season" is in the tree.

**N/E/R/S.**
- **N** — cut the price and a holder redirects his whole roster for free, which is the scaled-budget
  reading arriving by a side door: nine acts, one hour. What is lost is *the holder having to choose
  which of his people to spend.*
- **E** — a price on an existing act. No object, no verb. **This is the one genuinely new sentence in
  the act-economy material and I am flagging it rather than folding it into I-7.**
- **R** — *conditional per C-5.* `dispatch`'s gain compounds (`14 §3.1`: a dispatched man deposits
  firsthand claims, so that node stops being a cohort in your ledger for several seasons) against a
  cost that compounds two ways (`04 §1.4`'s regard price scales with how unreasonable the demand is;
  and every node you did **not** reach goes coarser). Concentrate and you burn a man; spread and your
  fidelity decays everywhere.
- **S-UP/S-DOWN** — unchanged.

**What it costs.**
1. **The convener becomes the most expensive office in the game to hold.** A ducal proxy who composes
   the Grauwald agenda can do nothing else that season. `14 §5` says *"the convener holds the cheapest
   real power in the game"*; under I-8 it stops being cheap. **Note carefully what may and may not be
   said here:** the *five-lane convergence* on that phrase is struck (S-3 — it is verbatim suite
   text, zero independent signal), so nothing is lost by contradicting the convergence. But
   `14 §5`'s **mechanism** claim — a convener who puts three items ahead of yours has spent nothing
   and killed your petition — is a design statement in its own right, and I-8 contradicts *that*.
   Somebody must decide whether the convener's power should be cheap. §4.1 records it.
2. **A quiet refusal may deposit nothing.** `14 §3.1` gives an overt refusal a deposit; a rider who
   simply does something else deposits nothing into the holder's coarse ledger, so a holder may be
   unable to distinguish an establishment that failed from one that never tried. That is arguably
   correct — it is the same blindness `14 §3.1` prizes — and arguably a hole.
3. **The establishment needs a boundary it does not have.** `14 §1.5` lists establishments as prose
   phrases — *"the watch, the granary keeper"*, *"a Dicastery's whole graph"*. Under I-7 and I-8 each
   phrase is an act count, and **a person appearing in two establishments spends two acts.** The
   roster must become named persons with exactly one membership, or the count double-counts.

**Falsifier — the cohort exploit, and it is the reason I-8 should be tested before it is trusted.**
`09 §1.1` gives a cohort one act too. If an establishment is held at cohort fidelity — "the watch",
eleven men, one record — it contributes **one** act; individuated, eleven. **Run it offline: if
individuating one's own establishment strictly increases throughput at no cost, the derived count is
a fidelity exploit and I-8 must be re-specified.** This is the one place the act economy touches the
resolution machinery, and it is where a cold reader should push.

---

### I-9 · Vacancy-by-absence: apply `14 §2.4`'s revocation-in-fact test at the hearth seat.

**Edits.** `04_hearth_and_community.md` §1.3, *The succession pointer*.

**Why it is warranted.** One of the three convergences the review certifies as genuinely independent
(two lanes, unseeded). And it is a two-document asymmetry checkable by direct read: `04 §1.3` says
*"**Death** does not resolve succession. It emits a **vacancy**"* — and death is the **only** emitter
at the hearth. `14 §2.4` already rules the general case one rung up: *"An office whose `exercise` is
zero across its whole scope for two standing dates is **vacant in the only sense that matters**, and
the world will have noticed before any venue has."* The rule exists; it was written for offices and
never applied to seats.

**The change.** One clause in `04 §1.3`: a vacancy is emitted on death **or** on zero exercise of the
seat across its whole scope for two standing dates, at the horizon table `04 §1.3` already publishes
(1 season untitled, 2 titled, 4 consecrated). **Everything downstream is unchanged** — `contest` opens,
the presumption is rebuttable, the third branch is still open war.

**N/E/R/S.**
- **N** — cut it and a person who is gone is mechanically identical to a person who is present, so a
  hostage, a conscript, a prisoner and an exile change nothing about the seat they hold. The lost
  possibility is *making a rival absent instead of killing him.*
- **E** — a clause reusing a test already ruled elsewhere, verbatim. **Nothing added.** This is the
  cheapest change in the lane after I-3.
- **R** — it creates a genuine fork rather than a strict improvement: **absence beats killing on
  risk** (no unsolved-killing hazard) and **loses on finality** (he is alive, so he can return,
  contest, and name you, and `12`'s `expel` is witnessed). *Conditional per C-5.*
- **S-UP** — unchanged. **S-DOWN** — improved: a seat becomes contestable by the person physically
  holding it, who is frequently the person with no post.

**What it costs.** It changes the value of every hostage in the setting at once. It also makes a
politics of engineered absence available to whoever can arrange one, which is disproportionately the
bodies with reach — the same asymmetry I-2 creates and for the same reason.

**Falsifier, and it is a real risk to the change as specified.** `09 §1.1` makes one act per season
a person's *discretionary* commitment, and doing nothing discretionary is a legal choice. **So exhibit
a present, functioning seat-holder whose `exercise` is legitimately zero across two standing dates.**
If such a person exists — a hearth head who simply takes no discretionary act for two dates — the test
emits **false vacancies against present holders**, and the predicate must be re-specified on presence
or on a narrower notion of exercise, not on the act count. `14 §2.4` may survive this at office scale
where a remit implies routine exercise and not survive it at hearth scale, which is exactly the kind
of thing a rung-to-rung reuse gets wrong.

---

### I-10 · `settle_in_full` loses its creditor precondition.

**The weakest of the ten, and the last to ship.** I include it because its evidence survives; I would
drop it before any other if a critic wants a smaller set.

**Edits.** `13_material_life.md` §8.

**Why it is warranted.** The third of the three certified-independent convergences: one lane had a
character *"simply **buy**, because a broker is a person with a price"*, and another proved **no
payment act exists between unrelated persons anywhere in #342**. The underlying collision is
document-internal and checkable: `07 §4`'s **purchased** power base says it *"rises by: buy it"* and
that its cut is *"money — the only basis whose cut is symmetrically available to any rich rival"*,
while `13 §9` refuses a currency outright — *"What dies: the flavour of coin. Every formula above uses
the same `stores` scalar the larder already banks in mouth-seasons."*

**The change is a deletion.** `13 §8` already has a priced, witnessable transfer between two parties:
`settle_in_full(hearth, creditor)` — *"pay owed + arrears in stores, before the reckoning, at the
going price (§4)."* **The creditor relation is the only thing making it a debt act.** Drop it:

```
convey(from, to, goods, quantity)  —  stores(from) −= q ; stores(to) += q,
                                      valued at 13 §4's price, witnessable, depositing a claim
                                      naming both parties.
```

**`13 §9`'s refusal survives intact**, and that is why this is the right shape: what moves is *goods
at the season's price*, not a token. You cannot hoard purchasing power in Valoria — only grain, which
rots, and iron, which is heavy.

**N/E/R/S.**
- **N** — cut it and `07 §4`'s purchased basis has no operation that raises it, so one of seven power
  bases is unreachable and every transaction between unrelated persons is either kinship, coercion,
  or nothing.
- **E** — a precondition is deleted and a name changes. Object count unchanged; the transfer already
  existed.
- **R** — a purchased position is the most fragile there is: `07 §4` gives it *"the cheapest named cut
  in the game"* — outbid, or devalue the instrument with a dispensation. And `convey` is witnessable
  (a cart moves) and deposits a claim naming both parties, so a bribe is findable exactly as
  forestalling is. *Conditional per C-5.*
- **S-UP/S-DOWN** — unchanged.

**What it costs.** **It is a ruling on a live collision, made inside an integration document.** I take
`13 §9`'s side (no currency) while giving `07 §4` the transfer it needs. That is coherent and it is
still a ruling; §4.4 records it as such rather than burying it. It also gives material wealth a route
toward political standing that #342 partly withheld.

**Falsifier.** `07 §4` says the purchased basis *"never consolidates far"* precisely because its cut
is money and is therefore **symmetrically available to any rich rival**. Under goods-only, a rival's
ability to outbid is bounded by carriage and by rot, not by wealth. **If the purchased basis stops
being cuttable by outbidding, it consolidates — the exact failure `07 §4` says it avoids**, and
I-10 has broken the row it was meant to serve. Test it offline against `13 §4`'s price and
`13 §2`'s production profile.

---

## 3. Amendment requests

**Two, and neither touches `11_code_shape.md` §7's forbidden list.** I want that stated plainly,
because the lane (b) world-substrate object *does* need an ownership-table amendment (C-1) and this
lane's changes do not. **No change above adds a stored aggregate, a pushed aggregate, a field on a
container, a scale field, a flat modifier, a second resolver, a per-entity branch, or an authored
per-person object.** `11_code_shape.md` §3's ownership table is untouched: nothing here gives a
container anything beyond *"its stake, its judging set, its standing dates."*

**A-1 · `Venue.convener` becomes a required, non-optional, single-valued field of a type.**
This is an amendment to `14 §5`'s door tuple, not to §7 or §3, and it makes the type **stricter**
rather than wider. **The cost of NOT making it:** I-6's widening ships with B-11's price carried by
prose — *"the fiction must never render an institution as a speaker"* becomes a sentence rather than
a type constraint, and `11_code_shape.md` §8.1's own doctrine says exactly what happens then. C-3
identifies this as available and not yet taken. **The amendment is the repair; refusing it means
refusing I-6, not shipping I-6 unrepaired.**

**A-2 · One new predicate — `unify(claim, proposition)` and `agree(claim, proposition)` — enters the
substrate's vocabulary.**
`11_code_shape.md` §7 forbids objects and fields; a matching predicate over a tuple the substrate
already carries is neither. But P-5 says *a fix that adds a system has failed*, and honesty requires
naming this as the one place the lane adds vocabulary. **The cost of NOT making it:** `02 §6`'s
`unmet` term stays undefined — *"unsatisfied"* is a word with no referent in #342 — so
`need(commitment)` cannot be implemented at all, and the first session to try will invent an
incompatible predicate silently. **I would rather the vocabulary grow by two named functions than by
one unnamed assumption per implementer.**

---

## 4. Live choices — where I refused to pick

### 4.1 Should the convener's power stay cheap?

**The choice.** `14 §5` states as a design finding that *"the convener holds the cheapest real power
in the game … a convener who puts three items ahead of yours has spent nothing and killed your
petition."* **I-8 contradicts this**, because under it composing an agenda costs a season — and
`05 §3.1` already charges exactly that for `compose_agenda`, so the two #342 documents disagree with
each other independently of anything I propose.

- **Option A — keep it cheap.** Ordering a docket is free or near-free; `05 §3.1`'s
  `compose_agenda` price is the oddity and should be relaxed. *Consequence:* filtering is the cheapest
  power in the world, so the guild warden and the Dicastery's clerk matter more than their remits,
  which is `14 §5`'s stated intent and a genuinely unusual thing for a strategy game to model.
- **Option B — make it expensive.** `05 §3.1`'s price is the model; a convener spends his season
  ranking a docket. *Consequence:* filtering becomes a real trade against every other act, so
  conveners are fewer and the up-stroke is less throttled — but `14 §5`'s most-quoted design claim
  is retired.

**Recommendation: B, but only weakly, and the reason is that A and I-8 cannot both hold.**
`05 §3.1` already prices it; consistency with an existing price is a better reason than consistency
with a phrase. But this is a live design choice that leads to materially different games — a world
where clerks are the real power against one where they are not — and it is not mine to settle.
**Note what may not be used to settle it:** the five-lane convergence on *"the convener holds the
cheapest real power"* is struck (S-3, verbatim suite text). Neither option gets support from it.

### 4.2 The way in: is there a legal route to an address for a landless person?

**I did not integrate the residence-admission change, and this is why.** The source fix
(`04_relational_at_settlement.md` §2) proposes a settlement-court conferral row with four
coefficients. I decline it on three grounds: its motivating finding D-4 was evidenced by *"56 probes
across six lanes failing to fill the cell"*, and S-7 shows the shared instrument **pre-declared that
cell EMPTY and forbade lanes from filling declared-empty cells** — so the probes are zero evidence;
its own §6.7 admits two of the four coefficients are guesses chosen to make the gate behave as
desired; and it **adds a stake and a conferral row**, which is the only change in the source suite
that grows the object count (P-5).

**But the underlying question is real and is a direct read.** `04 §9` says *"`migrate(person,
destination)` is an act **requiring admission at the destination** or the founding of a hearth
there"*, and the same section's table says *"you leave the holdings behind"*, while `04 §2.1`'s
`found_hearth` requires a portion of holdings. `01 §4` locates admission at **Community**.

- **Option A — there is no hole.** Every address passes through a community, so migrating *is* being
  admitted to some community inside the settlement, and `04 §6` supplies gates for guild, hamlet,
  parish and chapter. The landless migrant seeks a parish or a hamlet. **If this is right, D-4's
  fourth sub-question is answered and no edit is needed.**
- **Option B — the hole is real but narrower than reported.** Every community gate `04 §6` supplies
  is heritage-, deed- or sponsor-weighted and none is need-based, so the classes of community that
  exist do not admit a person with nothing. The fix is then at `04 §6`, one coefficient row, not a
  new settlement stake.

**Recommendation: establish which, by reading `04 §6`'s vector table against a landless candidate,
before anyone writes a settlement-scale gate.** I have not done that read and I decline to write the
change without it. **A settlement-scale admission gate would, per `14 §1.1`, collapse
`binds = persons-by-presence` into `members-by-admission` and delete the one thing the Settlement rung
owns** — so if the answer turns out to be A or B, the source fix's shape was wrong regardless of its
evidence.

### 4.3 Which seats can a player occupy?

**This is C-5's question and it is load-bearing on every R line above.** RULE 3 makes *"is this seat
playable?"* a precondition of applying R at all, and crown playability is listed as undecided. **The
same undecidedness applies to every other seat this lane touches** — the ordinary person's, the
Confessor's, the reeve's. I have therefore written every R line conditionally and carried each change
on its N-line and its document-internal contradictions instead. **No change above requires a
particular answer to this question**, which is deliberate: a change that only survives if a
particular seat turns out to be playable is a change that should wait.

### 4.4 `convey` is a ruling on an open collision

I-10 resolves S8 (`07 §4`'s *"buy it"* against `13 §9`'s refusal of a currency) in `13 §9`'s favour.
That is a defensible call and it is still a **ruling made inside an integration document**, which is
not where rulings belong. The alternative — leave the collision open and drop I-10 — costs one power
base its rise operation. **Recommendation: take I-10, but record it as a collision resolution rather
than as a fix**, so a later reader can find and reverse it.

---

## 5. What this proposal does not do

**5.1 It drops E3 (`found_hearth` widening to `found`) entirely, for want of surviving evidence.**
E3's warrant was one character's blocked core inside an arithmetic C-6 shows double-counts, plus
D-10, which is **not** on `03_corrected_findings.md` §B's survivor list. It is also the only change in
the source suite that **adds a creation act at every rung**, which P-5 puts the burden of proof on,
and its own filing admits *"whether `found` should require standing at the parent is a real question
and I have not answered it."* **Dropped. If D-10 is re-established on evidence that survives, E3
returns as a separate proposal.**

**5.2 It proposes no change carried by any struck claim.** In particular: nothing here is justified
by the blocked-cores headline, by any share of the roster, by office as a predictor, by alignment or
rank as predictors, by the convergence *count*, or by D-4's probe count. Where the source fixes
leaned on those, I re-derived (I-7) or declined (§4.2, §5.1).

**5.3 It does not settle D-6 (the conferral cycle), and I-7 makes it more expensive to leave open.**
C-7 records that the sweep concluding conferral need not be person-rooted **does not close**: "needs"
does double duty between structural necessity and a drama argument, and another lane's succession
material was never tested. I-7 makes establishments load-bearing, establishments are filled by
`confer`, and Church conferral is a cycle with no external root. **That is a debt this proposal
incurs and does not pay.**

**5.4 It answers neither of the two compute questions it raises**, and both are C-4-legal to answer
offline: (a) does `θ(p, act)` fit `09 §10`'s per-tick budget once the attention floor varies per act
as well as per person; (b) does running `opening_set` once per hazard per person per tick fit, given
that a crisis individuates cohorts precisely when the tick is most expensive. `11_code_shape.md` §9
already says the view-budget question *"is an empirical question this document cannot answer by
reasoning."* **I have not answered it either, and I have not proposed an instrument to answer it** —
if one is built it must be a seeded offline probe whose subject is the game, never an in-engine check.

**5.5 It records one collision it found and did not act on, because I-1 makes it load-bearing.**
`02 §2.2` line 153 defines a practice as *"(name, **rank 0–5**, provenance, idiom)"*. `10 §1.2` line
33 says *"**Practice ranges 0–7**, where 0 is 'never trained'."* Two documents, two ranges, on the
quantity I-1 moves the whole of difficulty onto. **This is not one of my surviving findings and I do
not act on it**; I record it because a reader implementing I-1 will hit it immediately and should not
have to rediscover it.

**5.6 It does not remediate any existing code.** `engine/` and `systems/` are reference here, never
ruling. #342 is a from-scratch suite and this is an integration proposal against it.

**5.7 Nothing here was executed.** Every claim above about what #342 produces is a reading of a
document, and every arithmetic figure I quote from the source fixes is a hand calculation over inputs
those documents chose. §D binds this document as much as the ones it integrates.

---

*Ten changes: seven deletions, restrictions, or applications of an existing ruling; two formulas where
a document already named a term it never defined; one predicate, named. Two amendment requests,
neither touching the forbidden list or the ownership table. Four live choices, unsettled. One change
dropped for want of surviving evidence, and one collision recorded rather than fixed.*
