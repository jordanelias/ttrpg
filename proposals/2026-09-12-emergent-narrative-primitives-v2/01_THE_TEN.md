# The set — each stated by an agonist, attacked by an antagonist, closed with its residual

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

**Ordered by what the game can do that it cannot today.** Every item carries its **grounds** (`G` a game
commitment · `A` architecture, no veto · `I` a cost line) and, where a `G` is in play, the R2 argument
rather than a citation.

**The test applied to each, which is the reverse of v1's:** *add it — name what the world can now do, and
what decision a player now has.* Not: *does something already carry it.*

---

## 1 · THE CHRONICLE RENDER — walk `causes[]` and tell a person why

### *the only way R-WORLD is ever experienced, and the data is already written*

**AGONIST.** Every write in the loop already carries its causal antecedent. `Event.causes[]` is populated
at every write (`loop/matter.py:79-84`), a `claim.deposited` names the act it came from
(`loop/witness.py:145-148`), and MATTER's term maturation chains *"decayed → … → deposited → the act that
was witnessed"*. `queries/world_q.py::occasioned_by` (`:273-352`) already reads `causes[]`, and
`fixtures.py:310-311` walks `Event.causes[]` as `_r3_propagates`.

**Nothing renders it.** So the world produces a causal history that no person and no player ever sees.

**And the design does not treat this as optional.** `architecture/meta/04_CODE_ARCHITECTURE.md:751-756`:

> *"removing the referee does not remove the question the referee answered: **why did that happen?**"*

and `:765`: *"the engine owes the **ARITHMETIC of what the character already holds**, and nothing else."*
A `causes[]` walk bounded to the events a person witnessed is **exactly** that arithmetic. §C.11 obliges
it; it is not built.

**ANTAGONIST.** Three attacks; one lands and narrows it.

1. **"Jordan vetoed the arc-recognition surface."** — ⚠ **This is the attack v1 accepted, and it is
   wrong.** The veto is of **arc labels**, and the same document licenses the render in the same breath
   (`audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md:130-136`): the NOT-list
   carries *"no arc labels ever surfacing (C2)"*, and immediately — *"**What the engine CAN produce:** …
   **retrospective coherence (chronicle + causes[] walk)** — experienced forwards as pressure and
   choices, **recognized backwards as story**."* The phrase *"the arc-recognition surface Jordan vetoed"*
   lives in a different file (`integration_with_ners_audit.md:26`) and refuses the **labels**. **Attack
   fails, and the licensed half is the proposal.**
2. **"`ED-IN-0011` says never a meter — a render is a surface."** — **Lands, and scopes it.** The ruling
   binds *anticipation* surfaces — *"no quantized horizon ever surfaces"*. A **retrospective** walk
   forecasts nothing. So: past only, no countdown, no progress bar, no act labels. **`G`, argued: the
   five properties are served by a player who can *see* persistence; they are not served by a player who
   is told what is about to happen.**
3. **"`AX-2` — a render would leak world truth."** — **Fails by construction.** The walk is bounded to
   the events in that person's own ledger, which is `View`'s existing bound. A person's chronicle is as
   partial as their beliefs, and two people get different stories from the same season — which is the
   feature, not the limit.

**RECONCILIATION.** A **retrospective, per-person, label-free** render over `causes[]`, bounded by what
that person witnessed.

⚠ **THE OBJECTION THIS PROPOSAL DOES NOT ANSWER, AND IT IS THE SERIOUS ONE.** Supplied by an outside
integration document (`04_PROVENANCE.md` §7) and adopted here rather than deflected: **the record's premise
is contradicted by how players treat the records that already exist.** The nearest shipped analogues —
Dwarf Fortress's legends mode, Tropico's almanac — are, on the research corpus's own accounts, used by a
minority of players willing to work for it. And the one case where a record demonstrably *functions* is
Banished's **age pyramid**: a graph, read at a glance, **whose shape is the argument**. That is not prose.

**So the form is unproven, and the argument for it here is analytic** — §C.11 *obliges* the "why", which
establishes that the engine owes an explanation, **not that a line of templated text is how to pay it.**
Three consequences, taken rather than argued around:

1. **The record must be shaped, not just written.** A per-person causal walk that renders as a wall of
   lines fails the same way the almanac does. What the age pyramid has is a **shape the eye reads**; the
   chronicle needs its equivalent, and finding it is design work this proposal does not contain.
2. **The discipline is in what is EXCLUDED.** If every write is rendered, nothing is legible. `causes[]` is
   populated at *every* write, so the raw graph is exactly the undifferentiated log that fails.
3. **The cheap falsifier, and it precedes the design.** Build the record and a reason table in a stub —
   no economy, a handful of delegates, refusals, and the record — and **hand one player another player's
   record.** Can they tell the story of that run from it, unaided? That test costs a fraction of any
   proposal here and it settles the premise all of them share.

⚠ **And it is a shared premise.** Proposal 11 has nothing to query without this, proposal 2's suspicion
has nowhere to become visible, and a run's carry-over has nothing to carry. **Integration concentrates
failure, and this is where it concentrates.** Stated as the cost of the set's coherence rather than
presented as elegance.

**Grounds:** `G` on the anticipation half (upheld, scoped); `I` on everything else.
**`I` cost:** a render — plus the shaping question above, which is real design work and not a line of
templated text. No carrier, no verb, no axiom; the data has been accumulating this whole time.
**What it buys.** **R-WORLD becomes legible** — the half of NERS with no player in it currently produces
hooks that nobody can perceive. A steward who embezzled (proposal 3), a seat that changed hands, a term
that lapsed (proposal 4): each is a hook *only if someone can find out*. **E-LEGIBILITY**: the design's
own answer to *"why did that happen?"*. **This is the highest-value item in the suite and v1 filed it as
`ABSENT — no render, no artifact`.**

---

## 2 · A PATRON WITH THREE PRESSURES — the Queen's Table, as a person

### *the corpus's "most sophisticated pressure design", and R7's own G-half asks for it*

**AGONIST.** The research suite's strongest proposal is three inverse-linked pressures — **Standing ·
Patience · Suspicion** — held by a court you serve. v1 called it *"Valoria's most comprehensively
refused"* and grounded that on R7 and `carriers.py:579/586`.

**Both grounds are `A`, and R7 read whole asks for the mechanic.** R7
(`references/design_rulings_2026-09-06.md:169-184`) names **"legitimacy, the leader's standing and
populace morale"** as Queries over `stance`/`convictions`, says *"the reason a magnitude carrier feels
necessary is that `H-62` is open"*, and rules **"a ruler can be wrong about their own standing."**

**Put the three on a person and every one already has its carrier:**

| pressure | what it is here |
|---|---|
| her **Patience** with you | her `stance` toward you — `H-62`/`W-F`, planned to the YAML |
| her **Suspicion** of you | the claims about you in *her* ledger — deposited by tellings, decaying |
| your **Standing** at her court | `standing_of` (`decision/options.py:443-464`), already a **computed gap** |

**The inverse linkage is not bookkeeping — it is one witnessed act read by observers with different
convictions.** An act that raises you with the court is the same `news.told` that raises her suspicion.
And the reckoning is a **`convene`d `Date`** with an author (`loop/effects.py:175-190`), at which she
`revoke`s — a verb with a working effect body that has never once been reached.

**ANTAGONIST.** Three attacks; two land as constraints.

1. **"Three meters is three magnitude carriers."** — **`A`. Void.** And R7's own text admits the three
   quantities by name. Where they live is decided after the gameplay question.
2. **"A reckoning that scores and wipes the board is `AX-6` — permanence without an author."** —
   **Lands, and it is a real `G`.** The **automatic** wipe dies. What survives is a sitting she
   *convened*, at which she *decides* — which `effects.py:181-183` names as the lawful shape (`H-32`/`W7`)
   and which is unbuilt. **Argued against R2: an automatic wipe is less *persistent* (it erases) and less
   *emergent* (nobody authored it) than a queen who chooses. The refusal earns its place.**
3. **"She cannot form a candidate about you — no question yields a person."** — **Lands hard.** This is
   proposal 8, and proposal 2 waits on it. Without it her three pressures accumulate and she never acts.

**RECONCILIATION.** One antagonist, a person, whose three pressures are Queries over her own interiors,
who convenes a reckoning and decides at it.

**Grounds:** `A` on the meters (void) · `G` on the auto-wipe (upheld, argued) · `I` on the rest.
**`I` cost:** rides `H-62`/`W-F` (Jordan's, planned) and proposal 8. Adds **no new carrier**.
**What it buys.** **R-CHOICE**: every act trades on three axes at once, so no act dominates — v1 measured
the opposite today, only 2–7 of 22 candidates separable by conviction. **E-LEGIBILITY**: three named
pressures is *"intuit complex outcomes from simple choices"*. **R-WORLD**: she revokes *someone else's*
seat while you watch. And `T-c`'s promise finally has a subject — **a patron can be bribed, delayed,
burned, or killed.**

---

## 3 · EMBEZZLEMENT, WHICH ALREADY RUNS

### *the cheapest item in the corpus, and v1 filed it as refused twice*

**AGONIST.** The suite's "Two Ledgers" wants a private store beside a public one, and corruption as the
gap between them. v1 refused it twice: *"a second store with no owner; `Rung.__setattr__` raises on
undeclared fields"* (**`I`**) and *"public liability feeding unrest is a stored aggregate"* (**`A`**).

**Both miss that the mechanism is already executing.** A hearth **is a Rung** — `contain` gives
person → hearth → community → settlement — and `_eff_transfer` (`loop/effects.py:436-452`) writes
`(Rung, stores)` **twice**, one per side, refusing any side that is not a Rung. **So a `transfer` from the
settlement store to a steward's own hearth is embezzlement, today, with no new object.** `transfer` is one
of the eleven verbs that execute, measured **723** times over the corpus.

The "public liability" needs no aggregate: it is **the claims WITNESS deposits about that transfer**. And
the audit is `interview` / `research` / `reconstruct` / `surveil` — four of the eleven executing verbs,
the tree's most-executing family.

**ANTAGONIST.** Two attacks; neither survives, and one improves the proposal.

1. **"Then it is a false N-line — the tree already provides it."** — ⚠ **Correct, and that is the
   finding.** By `skills/ners/SKILL.md` §3's own definition this is what a false N-line *is*: something
   already ruled in provides the possibility. **v1 filed it as a refusal instead, which inverts the
   verdict's meaning.** The honest statement: **nothing needs building; it needs *playing*.**
2. **"Nothing makes skimming cost anything."** — **Improves it.** The cost is epistemic and it is
   already modelled: who was co-located, who holds a `claim` about the transfer, whether a `tell`
   carries it. That is the one place a further object would help — and it is proposal 8's and v1 `P3`'s,
   not a new one.

**RECONCILIATION.** Recorded as **already expressible and unexercised.** No proposal body; the work is a
fixture and a case that exercises it.

**Grounds:** `I` on both of v1's disposals; nothing `G` was ever cited.
**`I` cost:** ~zero. A corpus case.
**What it buys.** **R-CHOICE** — skim or serve, priced by who can witness. **R-WORLD** — a steward
embezzling in a settlement no player holds is a hook with nobody watching, which is R's half that has
almost nothing in it today. **S-UP** — the grievance travels as a telling, filtered by a person at a
rung, which is `skills/ners/SKILL.md` §7.1's S-UP test almost verbatim.

---

## 4 · DECLARED TERMS ON TENURES — `T-n`'s unbuilt half

### *licensed verbatim by an axiom, recorded as unbuilt by the verb table, and counted by v1 as an applied cut*

**AGONIST.** `T-n` (`architecture/meta/01_AXIOMS.md:1138-1142`):

> *"Some relations should not end at the holder's whim — a term of service, a wardship that lapses at
> majority… But an end condition nobody declared is a clock nobody wound, which `T-c` forbids.
> **So the opening act declares the terms.**"*

`engine/season/verb_table.yaml:421` records the consequence in its own words: *"`Tenure` carries no `term`
field… `T-n`'s declared-ends half… is **unbuilt** and is recorded here as unbuilt."* Layer 1 spells it
`Tenure.term?` (`04_CODE_ARCHITECTURE.md:183` row 14).

**And the machinery to mature it exists and runs.** MATTER matures act-declared stages at a later tick and
writes `Record.matured` (`loop/matter.py:55-109`) — *"the only mechanism in the design by which one
season's act reaches into a later one WITHOUT anybody acting again"*, and it **stops if the maker is
gone.** The same branch on a `Tenure` is the whole proposal.

**ANTAGONIST.** Two attacks; both land as constraints, neither kills it.

1. **"`T-c` forbids a clock."** — **It licenses this one.** `T-c` (`:304-316`) calls a wound clock the
   design's *"best single property"* precisely because it *"can be bribed, delayed, burned, or killed"*.
   A term declared at the opening act has a maker.
2. **"`T-o` puts the closer on the Seat, not the term."** — **Lands, and must be carried.**
   `01_AXIOMS.md:1171-1174` names the defect in its own schema: *"`Seat.revocation` and
   `Tenure.term.closer` are two homes for who may end this hold… **The Seat's is authoritative.**"* So:
   the opening act declares *when*; the seat declares *who may end it early*.

**RECONCILIATION.** One optional `term` field on `Tenure`, set by the opening act, matured by MATTER's
existing branch, with the closer resolving against the Seat.

**Grounds:** `G` licenses it (`T-n`); `I` is the whole gap.
**`I` cost:** one field, one MATTER branch, one `release`-side read.
**What it buys.** **R-WORLD** — a wardship lapsing at majority, a truce expiring, a stewardship ending:
each a hook wound seasons earlier by an act and fired with nobody watching. **R-CHOICE** — renew, let
lapse, or break early and pay. And the research suite's own best line, which it could not place:
*"you can read the year of your own coup off the graph."*

---

## 5 · THE BODIES CLOCK — ageing, births and deaths on `Rung.envelope`

### *`R4` route (2), and the only compounding quantity the design permits without an author*

**AGONIST.** `AX-5` (`01_AXIOMS.md:151-181`) licenses exactly three motions the world makes unasked, and
**bodies is one of them** — *"birth is envelope weight"*. The carrier is declared: `write_matrix.yaml:288-293`
carries `(Rung, envelope)` at `[MAT, CEN]`, emitting `envelope.changed`.

**Nothing writes it.** `loop/census.py:33-37` generates nobody — v1 quoted its own comment, *"NO CLOCK
GENERATES ANYTHING"*, and read that as a refusal. It is a **missing producer**, and Jordan asked for it by
name. **`R4 · THE WORLD MUST CHURN**" (`design_rulings_2026-09-06.md:77-87`):

> *"world must churn"* — *"`Rung.exists` and `Site.exists` have **zero producers**. Nothing founds, builds
> or grows. Four routes; **three need no axiom moved and all four are unbuilt**… (2) churn by matter —
> generative harvest/growth/founding, **arguably inside `AX-5` motion 1**."*

**ANTAGONIST.** Two attacks; the second is the one that matters.

1. **"It was proposed on 2026-09-10 and graded `paper` — an applied cut."** — **No.** `paper` means
   *unbuilt*, not *rejected*. The cited document
   (`proposals/2026-09-10-…/02_PROPOSALS_SUBSTRATE.md:142-147`) is itself a **proposal**: *"P2 · THE
   BODIES CLOCK — ageing, births and deaths move `Rung.envelope` at MATTER… the only compounding quantity
   the design permits without an author."* v1 counted a pending proposal as a cut already applied.
2. **"A cohort clock is a fourth clock."** — **Lands as a boundary, and `R4` draws it:** *"⚠ **Do not
   answer churn with a clock.** `T-c`, `D-17`/`D-21` refuse a quantity advancing with no author."* So
   ageing rides **`AX-5` motion 2 (bodies)**, which is already authorless *by ruling*, and birth/death
   must not become a fifth thing. **Argued against R2: bodies-as-motion is the ruling; a separate
   demographic scheduler is the thing refused.**

**RECONCILIATION.** Ageing, birth and death move `Rung.envelope` at MATTER under `AX-5` motion 2 — and
**no new motion is added.**

**Grounds:** `G` licenses it (`AX-5`), `G` bounds it (no fifth motion); `I` is the gap.
**`I` cost:** a MATTER branch; the matrix row is declared and the carrier exists.
**What it buys.** The **one compounding quantity** the design allows: boom, bust, an heir coming of age,
an elder dying and a `hold` ending through the death. **R-WORLD** at the highest yield per object in the
whole catalogue — a settlement's population turning over is drama nobody authored. And it feeds the
existing scarcity channel: more mouths against the larder, which `verb_table.yaml:13-16` calls
*"load-bearing"*.

---

## 6 · COMPLICATION AS THE MODAL OUTCOME

### *the measured band is 19%; the corpus's is 41–45%; v1 handed this to nobody as a "measurement"*

**AGONIST.** Exact enumeration over all 100 two-die outcomes at the shipped fixtures, through the discrete
`roll_net` the season seam imports:

```
FAILURE 74%  ·  PARTIAL 19%  ·  SUCCESS 7%  ·  OVERWHELMING 0%
reachable nets [-2 … +4]; max margin +2 against a band needing ≥3
```

Against this, the research corpus measures PbtA and Blades holding the complication band at **41–45%
across the entire competent range**. And `engine/autoload/dice_engine.py:283` states what Partial *is*
here: *"the near-miss-by-nothing outcome, not the tried-and-failed one."*

**At 74% Failure, most acts produce a refusal and nothing follows.** A modal Partial means most acts
**succeed at a cost** — which is the hook generator, because a cost is a thing someone can later act on.

**ANTAGONIST.** Two attacks, and the boundary between them is the whole proposal.

1. **"The ladder is Jordan's, ruled 2026-08-14."** — **Correct, and untouched.** At pool 2 no obstacle ≥ 2
   reaches Overwhelming; that is arithmetic on a ruling, not a defect. **This proposal does not move the
   ladder.**
2. **"Then it is just fixture tuning, and parameters are Jordan's."** — **Half right, and the other half
   is the point.** `pool_default = 2` / `obstacle_default = 2` are `assumption` fixtures
   (`engine/season/data/fixtures.py:358-360`) — his tuning. But **there is no competence *range* at all**:
   `Person.capability` is `{}` for every person in every world, with one writer that zeroes it. **A
   two-die cast should never overwhelm. The defect is that everyone is a two-die cast** — a missing
   producer (`I`), not a number.

**RECONCILIATION.** Two separable things, and v1 filed both as one measurement with *"no ruling; no
one-object repair"*:

- **`I`** — give `Person.capability` a producer, so a competence range exists. Then the band distribution
  becomes a property of the cast rather than of one fixture.
- **A genuine design call, and the only one this suite surfaces:** ⚠ **should complication be the modal
  band of this game?** That is not tuning — it decides whether play is mostly *refusal* or mostly
  *success-with-consequence*, and the two produce different games. **Jordan's, and put to him here rather
  than filed.**

**Grounds:** `G` on the ladder (untouched) · `I` on capability · one **open design call**.
**What it buys.** **R-WORLD** — a cost is an antecedent; a refusal is a dead end. `tell` resolves at a
measured 21%, so a modal Partial `tell` is **news that spreads distorted**, which is the
belief-with-provenance drama the corpus rates rarest. **E-LEGIBILITY** — *"I will probably get it, and it
will cost me"* is intuitable; *"I will probably fail"* teaches a player not to act.

---

## 7 · INTELLIGENCE BEFORE ACTION

### *four of the eleven executing verbs are investigation, and v1 refused the one corpus idea that uses them*

**AGONIST.** The corpus's derived best idea — *timing your move against a rival's weakest season* — was
refused by v1 as *"requires reading a rival's aggregate, which is the same refusal"* (§C.11).

**§C.11 refuses no such thing.** `04_CODE_ARCHITECTURE.md:765-770` refuses showing the player **world
truth their character does not hold**. It does not refuse the character **learning** a rival's state by an
act and then being shown the arithmetic of what they now hold — that is §C.11's *first* obligation.

**And the acts exist and run.** `interview`, `research`, `surveil`, `reconstruct` are **four of the eleven
verbs that execute**. Acting on intelligence that may be wrong is `AX-2`'s stated purpose, and
`LedgerReader` returns the **stored** value, so what a person knows is already **stale by default** — the
corpus calls that rarer and more potent than fog of war.

**ANTAGONIST.** Two attacks; both fail, and the second sharpens it.

1. **"A rival's state is an aggregate, and aggregates are refused."** — **`A`. Void**, and R7 rules the
   opposite: *"a ruler can be wrong about their own standing"* is the design *wanting* per-knower
   estimates that disagree.
2. **"Then nothing is new — the verbs already run."** — **The verbs run; the loop gives no reason to use
   them.** No question asks about a person (proposal 8), and nothing makes a stale read *costly*. What is
   missing is not an act but a **stake**: something a player loses by acting on an old belief.

**RECONCILIATION.** No new verb. What this proposal names is that **the investigation family is the tree's
most-executing and least-exploited surface**, and that the corpus's one idea for it was refused on a
misreading of §C.11.

**Grounds:** `A` on v1's disposal (void); `I` on the stake.
**What it buys.** **R-CHOICE** — spend a bounded budget to learn, or act blind. **R-WORLD** — a rival
misjudging *your* trough and moving too early is a hook that needs no author. **E-LEGIBILITY** — the
player reads their own estimate and can be wrong, which §C.11 makes structural rather than a courtesy.

---

## 8 · A PERSON-REFERENT ROUTE INTO DELIBERATE

### *carried over from v1 unchanged in substance, because it was never the part v1 got wrong*

**AGONIST.** No question source produces another person as a referent, so no candidate carries one as a
subject. Measured by instrumenting `opening_set` across the corpus: **177,170 candidates formed · 17,400
carry a person id · every one is the asker naming themselves · zero name anyone else.**

**And ratified Layer 1 already requires what this supplies.** A `Tenure` is owned by its subject
(`state/carriers.py:378`, `:387-388`); Layer 1 requires a `hold`'s subject to be **a Person, only**
(`04_CODE_ARCHITECTURE.md:181` row 12); a computed act's subject is its question's referent
(`decision/options.py:307-310`). **Layer 1 as ratified is unsatisfiable by the running grammar**, and the
measured *0 live `hold` tenures across 86 worlds* is that arithmetic.

**ANTAGONIST.** The scope is the live question, not the clause. Which claims qualify — *every witnessed
actor* versus *a narrower predicate* — differs by roughly the size of the cast, and the narrow reading
should be tried first. **This is `CLAUDE.md` §0's step-5 call and must be argued in the landing commit.**

**RECONCILIATION.** One clause at `queries/world_q.py:213` admitting a claim whose subject is a Person id.

**Grounds:** `I` throughout — and a Layer-1 conformance gap, not a new idea.
**`I` cost:** one clause.
**What it buys.** **Five of the ten proposals above and below wait on it**, and it moves three primitives
the corpus catalogues from unreachable to expressible: poaching, the delegate as a defection vector, and
opinion diffusion. **Falsifier, already run and reading the wrong way:** instrument `opening_set` and count
candidates whose subject is a person other than the asker. **It reads zero now; it must read non-zero
after.**

---

## 9 · FOUNDING — `R4` route (1) and (3)

### *`Rung.exists` has zero producers, and Jordan asked for four routes*

**AGONIST.** `write_matrix.yaml:294-299` declares `(Rung, exists)` at `[RES]`, class `ACTS`,
`social: true`, `by: "W2/H-41 — founding a hearth"`. **Nothing writes it.** `R4` is Jordan's directive on
exactly this: *"`Rung.exists` and `Site.exists` have zero producers. Nothing founds, builds or grows."*

v1 disposed of the corpus's site-selection primitive as *"no producing verb… the gap is R4's four unbuilt
churn routes, not D3's."* **That sentence concedes the point and files it as a refusal.** R4's route (1) is
*"churn by NPC action — `AX-1`-native"*, and route (3) *"churn by authored occasion… already called
lawful, entirely unbuilt."*

**ANTAGONIST.** One attack, and it is R4's own.

**"Spontaneous generation needs `AX-5` amended."** — **True of route (4) only**, and route (4) is not
proposed. Routes (1)–(3) *"need no axiom moved"*, by R4's own count. And the boundary is stated there:
*"Do not answer churn with a clock."* A founding is **an act**, by a person, at a venue.

**RECONCILIATION.** A founding verb — route (1) — writing the declared `(Rung, exists)` row.

**Grounds:** `G` licenses it (R4, and `AX-6` makes it contestable); `I` is the gap.
**`I` cost:** one verb; the matrix row, the emission (`rung.founded`) and the carrier are declared.
**What it buys.** **R-VARIETY** — the map differs between playthroughs, which is the corpus's most common
source of replay value and which this tree has none of. **R-CHOICE** — a decision with a permanent
footprint, and `AX-6` makes permanence contestable rather than absolute. **R-WORLD** — an NPC founding a
hearth changes the containment tree with nobody watching.

---

## 10 · CASUS BELLI AS A `Record`

### *v1 disposed of this with a single word and no ground*

**AGONIST.** The corpus's *claim / casus belli as a legal gate* was scored by v1 as **`ABSENT`** — no
citation, no analysis, no line. It is expressible today in declared vocabulary: a war with a **reason**
that is a `Record` others can be told about, which can be **forged** (`verb_table.yaml:236-244`) or
**destroyed**, and a succession claim that is `succeed` + `heir.designated` (`:479-495`).

**And the ruling on inherited casus belli already exists.** `design_rulings_2026-09-06.md:30-35`: when a
declarer dies, the inheritor *"gains **standing in a peace negotiation, not an automatic exit** —
standing, not a switch, which keeps the ending contestable rather than automatic"*, closing `F.32`.
**Jordan has already ruled on this mechanic's hardest edge.** v1 never found the ruling.

**ANTAGONIST.** One attack, and it lands as the cost.

**"`forge` does not execute and `destroy_record` cannot fire for any actor."** — **True, and it is the
`I`.** `forge` declares `Record.forgery_quality` and has no `EFFECTS` entry, so `driver.py:99` excludes
it; `H-75` records that `destroy_record` *"CANNOT FIRE FOR ANY ACTOR"*. **Both halves of the
evidence-fabrication channel are declared and unreachable** — which is a work estimate, not a refusal.

**RECONCILIATION.** Give `forge` an effect body and `destroy_record` a reachable eligibility; the casus
belli is then a `Record` like any other, with the succession edge already ruled.

**Grounds:** `I` throughout; one `G` already ruled *in favour* (`F.32`'s standing-not-a-switch).
**`I` cost:** one effect body; one eligibility fix.
**What it buys.** **R-CHOICE** — manufacture a pretext, or wait for one. **E-LEGIBILITY** — *who has the
better claim* is intuitable without simulating anything. **R-WORLD** — a forged succession record
surfacing years after its maker died, which composes with proposals 1 and 4 into the single most
narratively loaded object available here.

---

---

## 11 · THE WRIT — SIFTING AS A PLAYER'S VERB

### *the one idea an outside document contributed that this session never reached, and its substrate is nearly built*

**AGONIST.** In the research literature a **sifter** is an authoring instrument: a query run over a
simulation's event log to find fragments shaped like a story, offered to a designer or a writer. **Make it
an institution inside the fiction and it becomes a player's verb.** A player — or a rival — serves a
**writ**: a pattern matched against the causal record.

> *a delegate who received a posting shortly after making a gift, and whose district's yields then fell
> twice*

What comes back is **evidence** — carrying a strength, a believability and a decay — supporting a
dismissal, a prosecution, a restitution or a public accusation. **Writs cost. Writs can return nothing.
A writ served on a loyal delegate costs loyalty. And rivals serve them against you, over the same
record.** An ordinary strategy game's log is inert; here the player's principal instrument against a
subordinate is *reading the record correctly*, and their rival's principal instrument against them is the
same.

**Why this belongs in this suite rather than in a research document.** Proposal 1 makes the record
*readable*. This makes it **playable** — and it is the difference between a chronicle the player consults
and one they *use*. Without it, proposal 1's ledger has exactly the problem Objection 1 below names: it is
a thing to look at.

**And the substrate is closer to complete than anything else in this set.** Checked against the tree:

| the writ needs | the tree has |
|---|---|
| a causal graph to query | `Event.causes[]` written at **every** write; `queries/world_q.py::occasioned_by` (`:273-352`) already reads it. Its own docstring calls the chain *"the one that is actually the game"* and records it *"built end to end except for this one edge"* (`N3`, measured: 60 act-Events, 0 resolving to a question) |
| an institution that opens an inquiry | **`open_case`** — `writes: ["Record.exists", "Record.stages"]`, emits `case.opened` / `case.refused`, `requires: "the act DECLARES the stages and their terms"` (`verb_table.yaml:373-382`). ⚠ **And its eligibility is swept with `own` as an arm**: *"`own` is a different game (anyone may open a case), which is why it is swept rather than chosen"* |
| evidence that can be strong, false and perishable | **`Record`** carries `forgery_quality`, `subject_matter`, `ttl` and `stages` (`state/carriers.py:414-423`); `Claim` carries `source`, `confidence` and `when`, and confidence **decays at MATTER** |
| a term that ripens | **`Record.matured`** — ruled by Jordan 2026-09-10, *"add `Record.matured`, write it at MATTER"*, on the grounds that *"**THE MATRIX ROW IS THE GAME**"* |
| someone to adjudicate | **`determine`** — declared, `grade: absent`, `judging_set` **raises**. This is `H-32`/`W7` |

**ANTAGONIST.** Three attacks. One is fatal to the naïve form and names the real design problem.

1. **"A query language is unshippable."** — ⚠ **Lands, and it is the whole difficulty.** The answer is a
   **pattern deck**: a small set of pre-written patterns with slots the player fills — *this delegate,
   this district, this window of years* — composed from a fixed set exactly as a storylet is selected
   rather than authored. **The deck's size is the central unknown**: too few and every session runs the
   same three writs; too many and it is a language again.
2. **"The ledger must be prose for a reader and structure for a matcher, and those pull apart."** —
   **Lands.** It means proposal 1 and this one must be specified **together**, because the writ constrains
   the record's line format. Building the writ late means rewriting the record.
3. **"Auditing makes delegates disloyal, so the player never audits and the sub-game deletes itself."** —
   **Fails, and the failure is the idea's point.** A writ is not maintenance with a downside; it is **a
   bet with an information payoff**, and **rivals are serving writs against you**, so declining to
   investigate is not a free strategy.

**RECONCILIATION.** A pattern deck served against the record, returning perishable evidence, available to
rivals, and specified jointly with proposal 1.

**Grounds:** `I` throughout. Nothing `G` refuses it, and nothing `A` is in the path — it stores no
aggregate and pushes no magnitude; it *reads* a graph the tree already writes.
**`I` cost:** the pattern deck (content), a matcher over `causes[]`, and `determine`'s effect body — which
is `H-32`/`W7`, already the tree's named gap.
**What it buys.** **R-CHOICE** — *reading the record correctly* becomes a skill, and the decision *"is this
worth a writ?"* is a real one because it can return nothing. **R-WORLD** — a rival investigating you is a
hook that needs no author, and `AX-1` is satisfied natively because **a person serves the writ**.
**S-UP** — a grievance becomes a **prosecution** carried by an accountable party who spends something,
which is `skills/ners/SKILL.md` §7.1's S-UP test almost word for word. And **E-LEGIBILITY**: evidence with
a provenance chain is intuitable in a way a loyalty bar is not.
**Falsifier.** Across ten sessions, what fraction of writs return nothing? **Below about a third, the
patterns are too loose and the record is being confirmed rather than interrogated.**

---

## 12 · A TELLING SHOULD RENEW THE BELIEF IT IS ABOUT

### *the authored half of memory, and the reason "he loses the town by being forgotten" is not yet a move*

⚠ **This slot previously held a proposal that forgetting be a player's choice — curation as an act, the
person picking what to drop. It is withdrawn, on two grounds, and the second is the one that should have
stopped it at the start.**

**Nobody chooses to forget.** Forgetting is not a decision; it is what happens when a memory has degraded
past retrieval. A prompt asking a person which memory to give up is fiction-breaking whatever its
mechanics.

**And there was no gap to repair.** The withdrawn proposal argued that eviction has *no author* and is
therefore an `AX-1` hole. `AX-5` licenses it by name:

> ### **AX-5 · THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS: MATTER, BODIES, AND THE FADING OF MEMORY.**
> *"Nobody wound any of the three, and you cannot bribe silt."*

**The fading of memory is the third motion.** It is *supposed* to have no author, and the comparator
`confidence × (when + 1)` is degradation-to-lost expressed exactly: low confidence and old goes first.
That is shipped and correct.

---

**AGONIST — and what the correction exposes.** If forgetting is authorless, the authored half is the
opposite act, and `07_DYNAMICS.md:171-175` names it:

> *"influence is not taken away; **it lapses**. **He loses the town by being forgotten** is not a mechanic
> anyone wrote — it is what happens when **nobody spends a scene renewing the claim**."*

**Renewing a claim is the move, and the channel for it already works.** `LedgerReader.read`
(`queries/person_q.py:82-88`) selects the maximum `(when, confidence)` for a given
`(subject, predicate)` — so a **fresher claim about the same thing wins the read.** A telling deposits a
fresh claim. Being told about something therefore *renews* your belief about it, and `tell` is one of the
eleven verbs that execute.

⚠ **But the renewal carries the wrong payload, and that is the whole finding.** A telling deposits
`Claim(subject, predicate = e.kind, value = True, …)` — `predicate` is the **event kind**, `news.told`
(`loop/witness.py:137`). So a telling renews **`(B, "news.told")`** and never **`(B, "is_loyal")`**. You
cannot keep a specific belief alive by speaking about it; you can only refresh *that something was said
about B* — the one predicate nothing reads.

**So `07_DYNAMICS`'s sentence is not yet true of the running loop.** Spending a scene renewing a claim is
the design's stated counter to lapsing, and today there is no claim it can renew.

**The proposal** is the one v1 reached and v2 dropped from its numbered set: **a telling about a person
deposits the predicate and value the teller actually holds**, in the namespace `standing_of` already reads
(`person_predicates`). `OwnLedger` names the owed half at the predicate that does the reading
(`data/requires.py:317-319`): *"A liar and a mistaken witness both pass it, and **the distortion lands at
the receiver's WITNESS deposit**."* And `epistemic.py:76-83` calls it an open item in its own words —
*"`H-116`'s other half — WITNESS depositing claims in that namespace — is not this item."*

**ANTAGONIST.** The three routes that close, and the one that does not, are stated in full at
`02_THE_RESCORE.md` and in v1's `P6`: no `Event` payload field (S19.3, with a stated bar against a
fourth); `claim.held` is excluded from the deposit by a tested guard; and a content predicate is inert
against `belief_contradicts`, whose vocabulary is eight **structural** stems. ⚠ **That third attack fails
on the consumer that matters** — `standing_of` pairs on `person_predicates`, a **content** vocabulary, so
`REQUIRES_STEMS` never enters the path and no grammar change is needed.

**RECONCILIATION.** Tellings only, subject a Person, predicate in `person_predicates`, `source = "told_by"`
— already a declared `claim_sources` value. `tell` keeps `writes: []`.

**Grounds:** `I` throughout. `AX-5` governs the *forgetting* and is untouched.
**`I` cost:** one deposit branch and a second Observation at `OwnLedger.check`.
**What it buys.** **It closes the memory loop the design already describes**: decay is authorless
(`AX-5`), and renewal becomes an act that keeps *a particular belief* alive. A reputation now survives
only while someone keeps speaking of it — which is `07_DYNAMICS`'s sentence, running. And it is measured:
**25 worlds, 4,499 deposited claims, every one `firsthand`, zero `told_by`, and `standing_of` at maximum
gap for 75 of 75 persons.**

---

## 13 · THE POPULACE AS A WEIGHTED PERSON — named intermediaries over an anonymous cohort

### *the shape every management title in the corpus uses, and Valoria's carrier vocabulary already unifies it*

**AGONIST.** Every settlement game in the corpus resolves one question: how does a player govern many
people without addressing each one? The corpus's answer is **an anonymous population plus a hard-capped
tier of named intermediaries** — Banished's cohort with nobody named, Knights of Honor II's capped court
with nobody modelled below it, and the composition of the two that no surveyed title has.

**Valoria does not need a new object for this, and that is the finding.** `state/carriers.py:365`:

> *"S9. **A COHORT IS A PERSON AT `weight > 1`. ONE CLASS (S9.1).**"*

`weight` is a field with a floor of 1 (`:399-400` raises below it), and probe **P21** — *"a cohort and a
named person are one type"*, `by="construction"` — has a cohort **`speak`**. So a crowd is an actor in
the same class as a duke, by construction, and every measured world has **3 persons, every one at weight
1.** The mechanism is built and has never been used.

**ANTAGONIST.** Two attacks; both land and together they are the proposal's real content.

1. **"A weighted Person that acts is a crowd deciding — that is `AX-1`."** — ⚠ **Fails, and the axiom is
   the reason this works.** `AX-1` refuses *an institution, a container or an engine* as the subject of a
   decision. A cohort at `weight > 1` is **a Person**, in one class, and S9.1 says so deliberately: the
   design chose to make a crowd an actor rather than an aggregate. This is `AX-1`-native and it is *why*
   the carrier is shaped this way.
2. **"Then what does a cohort's interior mean?"** — **Lands, and it is the open question.** A cohort holds
   one ledger, one stance, one set of convictions — *the beliefs of a crowd as a single knower*. That is
   a real design call: it makes a village's opinion a thing that can be told, be wrong, and decay, and it
   makes it **one** thing rather than a distribution. Cheap, coherent, and a choice rather than a default.

**RECONCILIATION.** Populate a world with a few named persons at `weight 1` and a small number of cohorts
at `weight > 1`, and let the existing grammar run over both.

**Grounds:** `I` throughout — the class, the field and the floor all exist.
**`I` cost:** a world-build change. **No carrier, no verb, no axiom.**
**What it buys.** **Scale without micromanagement**, which is the corpus's central management finding and
which Valoria has no answer to at 3 persons. **R-WORLD** — a cohort that holds beliefs can be lied to,
can refuse, and can move (`move` executes 650×). And it is the substrate proposals 5 and 12 need: a
bodies clock with nobody in it moves nothing, and a crowd that forgets is a village losing its memory of
a grievance.


## §S · THE SET AT A GLANCE

| | proposal | grounds | `I` cost | waits on |
|---|---|---|---|---|
| **1** | the chronicle render | `G` scoped (retrospective only) | a render | nothing |
| **2** | a patron with three pressures | `A` void · `G` on the auto-wipe | rides `H-62`/`W-F` | **8** |
| **3** | embezzlement | `I` ×2 | ~zero — a case | nothing |
| **4** | declared terms | `G` licenses (`T-n`) | one field, one branch | nothing |
| **5** | the bodies clock | `G` licenses (`AX-5`, `R4`) | one MATTER branch | nothing |
| **6** | complication as modal | `G` untouched + **one design call** | capability producer | Jordan |
| **7** | intelligence before action | `A` void | a stake | **8** |
| **8** | a person-referent route | `I` — Layer-1 conformance | one clause | nothing |
| **9** | founding | `G` licenses (`R4`) | one verb | nothing |
| **10** | casus belli as a `Record` | `I` ×2 | one effect body | nothing |
| **11** | **the writ — sifting as a player's verb** | `I` throughout; nothing `G` or `A` in the path | a pattern deck, a matcher, `determine`'s effect body | **1** (jointly specified) |
| **12** | **a telling renews the belief it is about** | `I`; `AX-5` governs the forgetting and is untouched | one deposit branch + a second Observation | nothing |
| **13** | **the populace as a weighted Person** | `I`; the class, field and floor all exist | a world-build change | nothing |

---

### §S.1 · FOUR REFINEMENTS TO PROPOSALS ALREADY IN THE SET

Mined from the same outside document's five composed designs. None is a proposal; each changes how one
above should be built.

**→ Proposal 1 gets its shaping answer: PROVENANCE AS THE INTERFACE.** The unanswered question in
proposal 1 was *what shape* a record takes, given that the one record shown to work is a graph read at a
glance rather than prose. The answer offered: **display a belief as its chain of sources, not as a
magnitude** — so the affordance the player reaches for is the chain. That discharges §C.11's obligation
*without a meter*, which is what `ED-IN-0011` forbids, and it is a shape rather than a wall of lines.
Its sibling instrument, **a dated stale display**, is nearly free here: reads are already stale by default
and `Claim.when` exists; nothing timestamps what it shows. ⚠ **The third instrument — salience-ranked
unprompted reporting — Valoria must refuse**, per `03_WHAT_SURVIVES_R2.md` §5, and saying so is the
honest half of adopting the other two.

**→ Proposal 2 gets its pricing: COSTS ARE RELATIONAL, NOT MATERIAL.** *"A writ served on a loyal delegate
costs loyalty."* Valoria has no currency and R7 refuses stored magnitudes, so the only pricing available is
in **stance and in what others come to hold** — which is not a workaround but the design's native answer
to cost. And the paired anti-degenerate device: **rivals serve writs against you**, so declining to act is
not free. The general form — *make the instrument symmetric and its cost relational* — applies to every
act in the set.

**→ Proposal 6 gets a better argument than "more hooks".** The outside document's P1 replaced a scheduled
coup with **continuous small refusals**, and states why: one scheduled catastrophe *"reads as scripted
doom"*, while a distribution of small legible costs is individually survivable and cumulatively legible.
Valoria's problem is the mirror image — at **74% Failure** most acts produce a refusal and nothing follows.
So the case for a modal complication band is not merely volume: **it is small authored costs instead of
one big unauthored event.** Its paired requirement: *"the override must cost something durable"*, or the
intermediaries are decorative.

**→ Proposal 8 generalises from persons to PLACES.** Its P5 moves population on *reputation in transit* —
what a household believes about a valley, not its true state. Valoria's `move` executes **650 times** with
its destination bound from **the question's referent**, so *a person moves to what they were asked about*.
If what they are asked about is **a claim they hold about a place**, migration-by-belief is nearly there —
and it is the same clause as proposal 8, with a place-referent rather than a person-referent. Worth
specifying together.

---

### §S.2 · ONE CORROBORATION OF `AX-1` FROM OUTSIDE

The outside document's own Objection 4 says of its weakest design: *"**P5's weakest joint is not the peace
trap; it is that nobody in it can be blamed**"* — its households are not persons, so attribution has
nothing to attach to. **That is `AX-1` derived independently, by someone analysing a different game and
never having read this tree.** `03_WHAT_SURVIVES_R2.md` §1 argues `AX-1` earns its place; this is the
first evidence for it that did not come from inside the design.

**Not one of the thirteen requires revising a `G`.** Five are *licensed and unbuilt* — a ratified line already
asks for them. Three need no new object. One is a question for Jordan. **The refusals that do hold are in
`03_WHAT_SURVIVES_R2.md`, each argued rather than cited, as `R2` requires.**

⚠ **Proposals 1 and 11 must be specified together, and 1 carries the suite's single point of failure.**
The writ constrains the record's line format, so building it late means rewriting the record. And if the
record's *form* does not work — the objection inside proposal 1 — then 11 has nothing to query, 2's
suspicion has nowhere to surface, and a carry-over has nothing to carry. **The falsification stub in
proposal 1 is therefore the first thing to build, before any design in this set.**
