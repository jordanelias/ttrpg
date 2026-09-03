# THE META-ARCHITECTURE — STAGE 1 · AXIOMS, IDIOMS, SCHEMA

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Scope: Jordan-directed, 2026-09-03. A **top-down** exercise to determine the ideal *logical
## shape* for future work. **Nothing here is built and nothing here is meant to run.**

---

# PART 0 · WHAT THIS IS, AND THE ONE TEST IT MUST PASS

## §0.1 · The instruction, and what it changes

Jordan, 2026-09-03, on the standing of this stage:

> *"This is a top-down exercise to develop axioms/idioms/schema and consequently hierarchies,
> dependencies, nests and scales and therefore discussing verbs, consequences alongside slices and
> season loops. We are not building something bottom up that can run as code — we are performing a
> meta-architecture exercise from top down to determine the ideal logical shape for future work."*

⚠ **`CLAUDE.md` §0.2 — *done means it runs* — DOES NOT GOVERN THIS DOCUMENT, AND SAYING SO IS NOT A
LOOPHOLE.** §0.2 exists to stop a *milestone juncture* being marked done on a `## Status:` line. This
stage is not a juncture; it is the layer a juncture would be derived **from**. Under §0's own
amendment — *"Work is this session's work if Jordan asked for it this session"* — the licence is
explicit. **What §0.2 still binds is everything downstream: nothing in this document may be cited as
evidence that any behaviour is correct.** Under §0.05 it is REFERENCE.

⚠ **AND `PLAN.md` IS PAUSED, NOT SUPERSEDED.** Its `W18→W20→W21→W22→W23→W26→W27→W30` path stands
and is not withdrawn. This document does not replace it and must not be read as replacing it. The
two answer different questions: `PLAN.md` says what to BUILD; this asks what the things ARE.

## §0.2 · The test this document has to pass, taken from the handoff that asked for it

`HANDOFF_META_ARCHITECTURE.md` names the recurring defect class, measured across five of seven
findings in the preceding audit:

> *"an artifact that reports success for something that did not happen"*, or *"a guard that cannot
> observe what it guards"* — **and: "A meta-architecture that does not make this class hard to write
> has not earned its cost."**

**That is the acceptance test, and it is met or failed in PART C, not in PART A.** An axiom set that
is elegant and leaves the defect class writable has failed. `ID-9` and `ID-10` are the two idioms
that exist to close it, and §C.3 states what each one costs.

## §0.3 · Why this stage was needed at all — the diagnosis, restated as a structural claim

> *"the tracer grew its entities one defect at a time. `Person` has whatever fields a verb needed;
> `Office` gained `body`/`faction` yesterday because Jordan asked a question; a "faction" is a STRING
> in a roster with no type at all; a `Site` is a rung + kind + condition because MATTER needed one.
> **Nothing states what any of them IS, so every new requirement lands as another field.**"*

**The generative defect is the absence of an admission test.** A schema that lists fields can only
grow; a schema that states what a thing IS can *answer* a new requirement — sometimes by adding a
field, more often by showing the requirement is already expressible, and sometimes by showing it
belongs to a different thing entirely. **PART D is written as admission tests, not as field lists,
and that is the whole of the difference.**

---

# PART A · THE AXIOMS

**An axiom is a statement that cannot be derived from the others and that changes what the game IS
if removed.** The chain currently states five "laws" of coordinate rank. **Two of them are not
axioms — they are theorems**, and PART B derives them. Demoting them is not a weakening: it tells a
future session which statements it may never trade away and which it should expect to re-derive.

**There are SIX.** ⚠ The first publication said five; `AX-6` was found missing by an adversarial
pass, and §A.1 records which theorems had been leaning on it unstated.

---

### **AX-1 · ONLY A PERSON ACTS.**

> No institution, no faction, no threshold, no clock, no container, and no engine is ever the
> subject of a decision. An institution acts *by a named person at a venue*.

**Why it is axiomatic.** Nothing else here implies it. A design could keep every other axiom and
still let a faction take a turn. It is the seed of the whole shape and the chain says so: *"return
here: the answer is almost always the one that keeps a named person as the author of the change."*

**What it costs, stated at the top because it is real.** A residue of arc cases in the corpus is
core-blocked by refusals descending from this axiom, and they are not repairable by specification —
**they were authored against a model with faction meters, world tracks and a GM.** AX-1 is what
makes them unrunnable, deliberately.

⚠ **AND THE `22` IS NOT AX-1'S BILL. ONLY ABOUT A QUARTER OF IT IS.** The chain's own table makes 22
the **sum of five refusals**: a social aggregate on a Rung (~8, which is `AX-4`), a threshold
producing an outcome (~4, `T-b`), a fourth clock (~4, `T-c`), a faction acting (3, `AX-1`), a GM
adjudicating (3, `AX-1`). **Six of 22 descend from `AX-1`.** Parking the whole figure here
overstated this axiom's cost ~3.7× and understated `AX-4`'s — **in the one place this document
quantifies what an axiom costs**, which is the worst place to be loose.

⚠ **THE FIGURE IS ALSO ROUTER-ERA.** `W10` deleted the regex router,
so the query that produced it *"has no subject, and re-running it returns zero in both columns"*.
The qualitative claim — that the two pathways fail for categorically different reasons — is a **live
hypothesis**, not a measurement, and `W13`'s authoring lane is the test of it. **Do not cite `22` as
current; cite it as what a re-measurement has to beat.** (`CLAUDE.md` §0.1 point 4.)

---

### **AX-2 · NO ONE HAS PRIVILEGED ACCESS TO THE WORLD.**

> A person decides from what they hold, and what they hold may be false. There is no view of world
> truth available inside a decision — not capped, not filtered: **absent.**

**Why it is axiomatic.** Independent of AX-1: one could have persons as the only actors and make
them omniscient. This is the axiom that makes a false conclusion *indistinguishable from a true one
to the person holding it*, which is the condition every deception mechanism in the game rests on.

---

### **AX-3 · WHAT IS TRUE AND WHAT IS RIGHT ARE DIFFERENT KINDS OF THING.**

> They are held in different places, moved by different forces, at different times. **Evidence moves
> what is held true. Argument and consequence move what is held right.** Nothing moves either on a
> clock — ⚠ **save the one fading `AX-5` licenses, which only REMOVES and never REVISES.**

⚠ **THE CARVE-OUT IS A CORRECTION, NOT A HEDGE (F1, 2026-09-03).** The sentence read *"Nothing moves
either on a clock"* full stop, and it contradicted `AX-5` in the tree: **`(Claim, confidence)` is a
`MATTER`-class write** (`write_matrix.yaml`), Reading 07 calls fading *"one of only three things the
world does unasked"*, and eviction ranks on confidence × recency. **So what is held true DID move on
a clock, by the design's own third motion**, and two axioms were in contradiction with nothing
flagging it.

**What makes the carve-out safe rather than a hole:** fading changes a claim's **confidence**, never
its **value**. A memory can dim to nothing and can never become a *different* memory. **Revision
still requires evidence, which is the whole of what `AX-3` protects** — and the axiom set's own
falsifier (`§F.4` row 1) named `AX-5` as the standing candidate for dependence without ever checking
it against `AX-3`.

**Why it is axiomatic.** A design could have one layer carrying both. This axiom is the reason
investigation cannot become moral re-engineering: if evidence could move a conviction, then finding
a document would change what a person believes is *right*, and the moral layer would collapse into
a second epistemic layer.

The chain calls the collision *"the single most dangerous in the design"*, which is a statement
about **consequences**, not about likelihood — and it is dangerous precisely because the two layers
look alike from any distance.

---

### **AX-4 · EVERY VALUE HAS EXACTLY ONE OWNER, AND THE OWNER IS ITS ONLY WRITER.**

> Name any value in the game and something owns it, or the model is incomplete.

**Why it is axiomatic.** It is a commitment about state, not about persons, and nothing above
implies it. It is also the most *productive* axiom in the set — PART B derives four theorems from
it, including one the chain currently states as a coordinate law.

---

### **AX-5 · THE WORLD MOVES BY ITSELF IN EXACTLY THREE WAYS: MATTER, BODIES, AND THE FADING OF MEMORY.**

> Nobody wound any of the three, and you cannot bribe silt.

**Why it is axiomatic, and why it is stated as a LIST rather than as a prohibition.** ⚠ **This is a
correction to how the chain states it.** The chain's L5 reads *"every clock … was set by a nameable
act"* with the three as a carve-out. But the prohibition **is derivable from AX-1** (a quantity
advancing with no author is an actor arriving through a side door) — while **the membership of the
list is not derivable from anything.** Three is a stipulation. Two would be a different game; four
would be a different game.

**So the axiom is the list, and the prohibition is `T-c`.** Stating it the other way round hides the
one part that is a genuine design choice inside the part that is a consequence.

⚠ **AND THE LIST MAY BE INCOMPLETE — THERE IS A FOURTH CANDIDATE THIS DOCUMENT NEVER NAMED.** The
loop has **two** world-writing steps, not one: CENSUS reconciles the envelope and performs
**individuation**, admitting `(Person, exists)` and emitting `person.individuated`. **That is the
world creating the only kind of thing `AX-1` lets act** — and the easy defence is foreclosed by the
chain itself, which rules that *birth is envelope weight, not a `create`*, so individuation is not
"bodies". What demands one is graded `absent`.

**RESOLVED, and the list stays at three.** CENSUS is **demand-driven only** — *nothing generates
without a demand, and no clock generates anything*. A demand is produced by acts. **So individuation
is authored: the demand is its author**, and `T-c` is satisfied rather than evaded. `AX-5` says
three.

⚠ **What this costs, and it is a real constraint rather than a free pass:** the world may never
individuate a person nobody's act demanded. **A world-generation roster is not a clock and is
lawful; a population that grows on its own is not.** And `T-c` and §D.4's NEVER should be quantified
over *the licensed motions*, not over *MATTER*, or a CENSUS write evades them on a technicality —
which is the wording this document shipped.

---

### **AX-6 · NOTHING BECOMES PERMANENT WITHOUT AN AUTHOR.**

> A state that no act can undo is a state nobody chose to make final. **Every irreversibility IN THE
> GAME STATE was made by somebody**, and is therefore itself contestable.

⚠ **THE SCOPE CLAUSE IS LOAD-BEARING AND WAS MISSING (F2, 2026-09-03).** `AX-6` quantifies over
**state**, not over **schema**. Without that word it is either false or unusable:

| | |
|---|---|
| read as *any* permanence | it **forbids this document's own schema** — `Tenure`'s `NEVER: deletion`, `Proposition`'s immutability, the append-only log. No in-fiction act authored any of the three |
| read as *an in-fiction act* | it **cannot reach `T-a`'s ratchet clause**, whose monotonicity is a property of the schema rather than an authorless change |

**Both readings were in use at once**, which is how `T-a` came to derive the ended-edge refusal from
`AX-6` while `AX-6` simultaneously licensed the ended edges that make it monotone.

> ### **THE SPLIT, AND `§F.4` ROW 2 IS HEREBY RECORDED AS FIRED.**
> **`AX-6` governs GAME STATE: every irreversibility a person could be subject to has an in-fiction
> author.** **Schema permanences are a different thing** — authored by the designer, at a commit,
> and they are contestable by editing the design rather than by an act. They are not exempt; they are
> **enumerated**, and the enumeration lives in `PART D` as a marker rather than in a loader, because
> a loader cannot see a language-level guarantee. `ID-18` states the obligation.

⚠ **THIS AXIOM WAS MISSING FROM THE FIRST PUBLICATION, AND AN ADVERSARIAL PASS FOUND ITS ABSENCE.**
It is recorded that way rather than quietly inserted, because *how* it was found is the argument for
it: **two separate derivations reached for it and neither could get there from `AX-1`..`AX-5`.**

- **`T-a` could not derive L3's clause 3** — *any Query monotone in the ENDED-edge set is a ratchet
  and is refused.* That clause constrains a **Query**, which by construction has no owner and no
  writer, so `AX-4` — a statement about owners and writers — cannot reach it.
- **§E.1.2 found four of seven relations openable and never closable**, which no axiom forbade.

**Both are one thing: a state becoming final with nobody having made it final.** `AX-1` says nothing
*moves* without an author; `AX-6` says nothing *stops being able to move* without one. **They are the
same commitment about authorship, applied to change and to its cessation** — and the second was
being relied on throughout while never stated.

**What it costs to deny it:** permanent grudges, unbreakable bonds, duties nobody can discharge, and
counters that only climb — each of which the chain has an instance of, and each of which is a
shadow actor wearing a state's clothes rather than a clock's.

## §A.1 · What is NOT an axiom, and why the demotion matters

| stated in the chain as | actually | derived in |
|---|---|---|
| **L3** clause 1 — a counter only per `(Person, axis)` | **a theorem of `AX-4`** | `T-a` |
| **L3** clause 3 — no ratchet over ended edges | **a theorem of `AX-6`** ⚠ *not `AX-4`; corrected* | `T-a` |
| **L5**'s first half — a crossing may never produce an outcome | **a theorem of AX-1** | `T-b` |
| **L5**'s second half — every other clock was wound by an act | **a theorem of AX-1 + AX-5** | `T-c` |
| **L2**'s enforcement — `choose` takes no `World` | **a theorem of AX-2** | `T-f` |
| **§19.3** — `Event` carries no actor | **a theorem of AX-2** | `T-d` |
| **§19.3** — `Event` carries no target | **a theorem of AX-1** | `T-e` |
| **§14.2** — a faction is a Proposition plus `commit` edges | **a theorem of AX-1** | `T-h` |

> **WHY THIS IS WORTH DOING AND NOT PEDANTRY.** A theorem and an axiom fail differently. **Break an
> axiom and you have chosen a different game — deliberately, and you can say what you chose.** Break
> a theorem and you have introduced a *contradiction*, which shows up later as a defect nobody can
> localise. The chain has already paid this: `L3` was argued for four revisions as though it were a
> free-standing commitment, when its clause-2 hole is exactly what AX-4 predicts — a per-person
> tally summed across holders has no single owner, so AX-4 refuses it directly and needs no
> read-side patch.

---

# PART B · THE THEOREMS

**Each is currently stated in the chain as a free-standing rule. Each is derived here.** The
derivation is the value: it says what would have to be true for the rule to be safely broken, which
a flat list of laws cannot.

### **T-a · An aggregate cannot be stored.** *(the chain's L3)*
> **From AX-4.** An aggregate is by definition a value over many owners. A value over many owners has
> no single owner. `AX-4` says every value has exactly one owner and that the owner is its only
> writer. **Therefore an aggregate cannot be a FIELD.** What it can be is a function — which is why
> the chain assigns every aggregate to **Nobody**: ownerlessness is the licensed state of a Query,
> not a refusal condition.

⚠ **CORRECTED. THE FIRST PUBLICATION OF THIS THEOREM CONTRADICTED ITSELF INSIDE ITS OWN PARAGRAPH**,
and an adversarial pass caught it. It concluded *"an aggregate can only be computed"* and then, six
lines later, that a monotone count *"has no owner, **so it is refused**"* — **the same premise
yielding compute-it and refuse-it.** Both cannot follow.

**What `AX-4` actually reaches, stated exactly:**

| L3's clause | derives from |
|---|---|
| **1** — a counter exists only per `(Person, axis)` on a closed registry | **`AX-4`.** A cross-holder tally has no owner, so it cannot be a field |
| **2** — no resolver-side Query may aggregate tallies across holders | ⚠ **neither.** It is a **read-side check** on a Query, and a Query has no owner for `AX-4` to constrain |
| **3** — a Query monotone in the ENDED-edge set is a ratchet, and is refused | **`AX-6`**, and nothing else. It is a statement about **permanence**, not about ownership |

**So L3 is not wholly a theorem of `AX-4`**, and §A.1's demotion is corrected to say which clause
goes where. ⚠ **The document's own §E.1.4 was the tell:** it reached for clause 3 **by name** to get
reversibility, in a document whose PART B claimed that clause unnecessary.

⚠ **And a second correction: `T-a` says an aggregate cannot be STORED; `ID-1` licenses a cache at a
barrier, and a cache is storage.** The reconciliation is that a barrier cache is discarded at the
next barrier and therefore **cannot go stale**, which is what `AX-4`'s ownership rule is protecting
against. Say *cannot be a field*, never *cannot be stored*.

### **T-b · A threshold may change what can be chosen; it may never produce an outcome.** *(L5, first half)*
> **From AX-1.** An outcome is what a decision produces. Only persons decide. A threshold is not a
> person. **Therefore a threshold that produced an outcome would be an actor.**

**And the corpus agrees with the theorem rather than with the fear.** In the 50-arc in-chain survey,
**19** wanted a crossing to *force a moment* and then have a person choose. **The design supplies
that exactly.**

⚠ **THE COUNTERPART FIGURE IS WITHDRAWN, NOT CORRECTED.** This read *"only **8** wanted the crossing
to act"*, making a tidy partition of 27. **The chain does not carry an 8 for that refusal** — its
figure for *a threshold producing an outcome* is **~4**, and the two 8s that do exist are a
different bucket and the faction/world re-scale count in this document's own next sentence. **The
same token was doing two incompatible jobs one line apart**, which is `ID-11`'s failure and `G11`'s,
by the author who wrote them down.

⚠ **CARRY THE CONDITION, NOT THE LITERAL.** `PLAN.md` `W20` measures that **11** of those 19 are
reachable today — the other 8 are `faction`/`world`-scaled and unrepresentable until `W28`
re-scales them. **19 is the post-`W28` figure**, and the first draft that published it without that
condition is the error this note exists to not repeat.

### **T-c · Every clock outside the three was wound by a nameable act, and therefore has handles.** *(L5, second half)*
> **From `AX-1` + `AX-5`, and the step needs stating rather than waving at.** `AX-5` lists what moves
> by itself. `AX-1` forbids a non-person actor. **The step that was smuggled:** `AX-1` as written
> forbids a non-person being *the subject of a decision*, and an authorless clock decides nothing —
> so the derivation goes through only if *causing a change the game reads* counts as acting.
> **It does, and that is the reading `AX-1` is stated under**; but a reader who takes `AX-1`
> narrowly gets no prohibition, so the chain is right to also carry the fourth-clock refusal
> **first-class** rather than only as a consequence.

**The consequence is the design's best single property and it is a THEOREM, not a preference:** a
wound clock can be **bribed, delayed, burned, or killed** — bribe the clerk who set the term, burn
the Record that carries it, kill the man who must renew it. **An unwound clock is unbuyable,
undelayable and unkillable, which is what a GM is.**

### **T-d · An `Event` carries no actor.**
> **From AX-2.** A field on the Event is read identically by every observer. Attribution as a field
> is therefore privileged access to who did it. **Attribution must be a per-witness `Claim`.**

**This is why covert action and false attribution are expressible without a mechanism for either.**

⚠ **AND TODAY THE THEOREM IS HONOURED IN A FIELD NAME AND VIOLATED IN MECHANISM.** `Event` has no
`actor` field — but it has `subject`, **which the fold sets to the actor**, and WITNESS deposits
every claim with `subject = event.subject`. **So every ledger in the world reads "I hold that
`<actor>` did `<kind>`", certainly and identically** — exactly the privileged access `AX-2` forbids,
arriving one field over. The chain agrees: `W24` proposes making `subject` the changed object and
depositing the actor per-witness, describing it as **restoring** §19.3 — and *restoring* concedes it
is not there. **`T-d` is currently a naming convention, not a mechanism.**

### **T-e · An `Event` carries no target.**
> **From `AX-1`.** A target field presumes delivery. Delivery without an act is transport by nobody.

⚠ **SOFTENED. The gloss *"the only transport is a person telling another person"* is quoted
faithfully from the chain and the chain contradicts itself:** four of its five witness channels —
co-location, a document, a witness key, a chronicle — deliver a claim with nobody telling. **The
theorem survives on the narrow ground (`Event` names no recipient); the strong gloss does not**, and
promoting it here without noticing was an inherited error rather than an invented one.

⚠ **These two are the pair a porter will want to break for routing convenience.** T-d and T-e say
the cost is not convenience — it is the deletion of two mechanisms the design has no other way to
express.

### **T-f · `choose` receives no `World`.**
> **From AX-2, made structural.** Enforcement is by parameter list, not by discipline: every
> resolver-side Query takes `World` first, so calling one from inside `choose` fails at the call
> site for want of an argument.

⚠ **In GDScript this degrades to a convention plus a token scan, permanently.** Record it as a
known degradation of an axiom's enforcement, not as an equivalent.

### **T-g · Obstruction needs no verb.**
> **From `AX-1` + `AX-4`.** A stranger takes the seat. **No `obstruct` verb, no knowledge of her in
> the stranger's decision, no branch in the resolver.**

⚠ **CORRECTED — the mechanic is real and the first derivation offered for it was not.** It said
*"the seat's state changed, written by its one owner"*, which §D.6 forbids in its own NEVER row:
**who holds an office is not on the office.** Nothing about the seat changes; a **new Tenure owned
by the stranger** comes into being. And *"the ambition-holder reads the seat"* is the object-side
index — Nobody's, resolver-side, and therefore unreachable from `choose` by `T-f`.

**The lawful account:** the obstruction is enforced at RESOLVE by `confer`'s 1-per-object
precondition, which refuses the second conferral. **The ambition-holder never reads anything; her
act is simply refused, and the refusal emits.** That is a better result than the first version
claimed — it needs no read at all — and it is `emits_on_refusal` doing the work `§27.1` assigns it.

**This is the worked example of what "emergent" means here** — and it is a proof that the axioms
carry weight, because obstruction is a mechanic the design never implements and always has.

### **T-h · A faction is not a thing that acts; it is what people are committed to.**
> **From AX-1.** If a faction cannot act, it cannot be an actor-shaped object. What remains that can
> carry its identity across time is an utterance — a `Proposition` — plus the edges of the people
> who signed it.

⚠ **AND A THIRD, ADDED 2026-09-03: T-h SAYS WHAT A FACTION OWNS, NOT WHETHER IT EXISTS.** It is not
an actor and owns nothing — **and it is still a first-class object code deploys**, resolved at a
barrier (§D.11). Reading `T-h` as *there is no such object* is what left every consumer recomputing.

⚠ **TWO CORRECTIONS, BOTH FOUND ADVERSARIALLY.**

**(a) The step does not go through as written.** *"What remains that can carry identity across time
is an utterance"* is false — a `Rung`, a `Record` and an `Office` all carry identity across time and
none of them acts. `AX-1` gets you *a faction is not an actor*; it does **not** get you *therefore a
Proposition*. That choice is an argument about what a faction IS, and it belongs in §D.5 as a
design claim, not in PART B as a derivation.

**(b) The collapse property is NOT free, and the chain retracts it in the sentence it comes from.**
*"A faction collapses when people leave… there is nothing left to be the faction"* is immediately
followed by *"⚠ THAT SENTENCE IS NOT YET TRUE"* — a Proposition may be a `hold` subject and is never
destroyed, **so a memberless faction leaves territory held by a banner nobody carries**,
uncontestable because the holder can never appear at a venue. This document reproduces that
retraction in §D.5 and still presented the property as free here. **It is a debt, not a dividend** —
and under `AX-6` it is the same defect as §E.1.2's: a state nobody can end.

### **T-i · No container gets a clock.**
> **From AX-5** (a container is not on the list) **plus the nesting rule** (a nesting form needs a
> caller-supplied depth cap; a container that schedules itself has no caller).

### **T-j · WITNESS never touches a belief.**
> **From AX-3.** WITNESS is where evidence lands. Evidence moves what is held true. A belief is what
> is held right. **Therefore WITNESS has nothing to say to it.**

### **T-k · One resolver, one degree ladder.** *(methodological)*
> **From the repository invariant that a rule lives once** — not from AX-1..AX-5.

⚠ **Marked separately and honestly: this is the one the chain says is enforced by a person
noticing.** It has no mechanism and no cheap test, and its violation is *locally reasonable* every
time. Naming it as the weak point is worth more than claiming a guarantee.

### **T-l · A cohort is a `Person` at weight > 1, never a subclass.**
> **From AX-1 + T-k.** A cohort acts, so it is a person-shaped thing. A second type means every
> mechanism has two code paths, and two code paths drift.

---

# PART C · THE IDIOMS

**An axiom says what is true. An idiom says how you SAY a thing so that the axioms stay true when
somebody who has not read them writes the next line.** Each carries the defect it prevents.

## §C.1 · The structural idioms

| | idiom | say it this way | the defect it prevents |
|---|---|---|---|
| **ID-1** | **Ask, don't store.** | an aggregate is a function of live edges, computed on demand, cached only at a barrier | dead state that reads as mechanism — a value initialised once, never written, cited for seasons |
| **ID-2** | **Relate, don't nest.** | a relationship is an **edge owned by its subject**; the reverse index is owned by Nobody and stored nowhere | two homes for one value, which can disagree with itself |
| **ID-3** | **Emit, don't apply.** | a crossing emits; the step that owns the write class applies | a band crossing with no antecedent — every crossing a causal orphan |
| **ID-4** | **Declare, don't route.** | bind a case to what it exercises by an authored declaration, never by matching words in it | **six recurrences in this chain**, ending in `age\w*` matching *agent / agency / agenda* and manufacturing the corpus's only PLAYABLE |
| **ID-7** | **One type, many kinds.** | eight rung kinds, one `Rung` type; refuse the subclass | a mechanism written for elites that is not automatically available to populations |
| **ID-8** | **Store the edge, derive the label.** | `contain` is stored; *scale* is read off it | ⚠ **a label cannot be WALKED.** This is the whole reason `under_purview` works and a `scale:` column does not |

## §C.2 · The epistemic idioms

| | idiom | say it this way | the defect it prevents |
|---|---|---|---|
| **ID-5** | **Refuse, don't default.** | zero evidence maps to the verdict **against** the thing measured; an absent roster raises rather than returning empty | a wear table that answers `20` for an unregistered kind — **plausibly and wrongly, forever** |
| **ID-6** | **Inject, declare, sweep.** | where the shape is ruled and only a value is open: inject it, name the site, sweep three points | a fabricated constant that is later cited as though it were measured |
| **ID-11** | **Ship the falsifier with the claim.** | a result claim carries, in the same commit, the test that would have shown it wrong, and that test's outcome | *"adversarially reviewed"* as an unfalsifiable assertion |
| **ID-12** | **A closed set lives in data.** | a roster, taxonomy, axis set or kind list is read at runtime; changing one is a data edit | ⚠ the strongest argument for this rule is that **`question_sources` was declared closed at three members and was missing a fourth** — without `Q4` an NPC with a standing ambition and a quiet season forms no candidates at all |

## §C.3 · The two idioms that exist to close the defect class — §0.2's acceptance test

**These are not general good practice. They are aimed at the measured defect class, and if the rest
of this document were deleted these two would still have earned their place.**

### **ID-9 · THE GATE APPLIES THE WRITE.**

> A gate that validates, logs, and returns `true` while the mutation happens beside it is **worse
> than no gate**: the logged value and the applied value diverge, and *"enforced by construction"*
> becomes false while continuing to look true. **Either the gate applies the write, or direct
> assignment is made impossible.**

**The measured instances.** `move` published `travel.moved` while changing nothing. `work` emits
`site.worked` while accumulating no delta, which makes site condition a **one-way ratchet** — wear
falls it every season and neither verb that could raise it can. `claim_decay` bypassed the counter
that proved it was registered. `term.matured` marks nothing.

**Every one is the same shape: a success report for something that did not happen.**

### **ID-10 · ASSERT ONLY WHAT YOU CAN OBSERVE.**

> A check that cannot see the failure it excludes is **absent**, not weak. A loop that asserts
> conditionally must assert that it asserted.

**The measured instances.** `_check_office` validated three axes and discarded the result. A
falsifier guarded on `hasattr(HL, "load_case")`, which does not exist, so half its reason never
asserted. `matrix_rows_without_a_field` tested `is_dataclass` against a plain class and filed five
rows *"uncheckable"* while the class carried exactly the declaration needed to check them. A verb
table extractor's `len == 8` filter **silently dropped four rows** whose cells contained an escaped
pipe. And in the instrument as it stood at PR #351, **15 of 20 PASS probes contained no assertion at
all** — a PASS meant *did not crash*. ⚠ That last figure is **of that version** (the honesty suite is
143 tests now, was 20); it is cited as the worked example of the shape, never as current state.

### **ID-13 · A DECLARED FIELD MUST REACH A READER, OR IT IS NOT DECLARED.**

> A column, flag or axis that no resolver consults is **not a weak mechanism — it is a mechanism
> that does not exist**, wearing a schema's clothes. And it fails silently in the one direction that
> flatters: everything it would have refused is permitted.

⚠ **ADDED AFTER `ID-9` AND `ID-10` FAILED §0.2's ACCEPTANCE TEST.** An adversarial pass found that
the chain's **most frequent** instance of the defect class is neither a bad write nor a blind
assertion: it is a **declared axis that decides nothing** — a stratum column that reached no
resolver, a `scale:` column that reaches none (*"the third instance of this defect in one session"*),
a `contests:` field transcribed where nothing reads it so a kill executed as a direct write, two
witness-channel predicates that can never return true, and a rank function whose only caller was its
own test. **`ID-9` needs a write and none of these writes; `ID-10` is satisfied by them and still
misses them** — a test asserting *every channel has a predicate* passes while two predicates admit
nobody. **`ID-10` says assert what you can observe; it does not say assert the property that
matters. `ID-13` is that property.**

### **ID-14 · WHAT AN ACT CAN OPEN, AN ACT MUST BE ABLE TO CLOSE — AND BOTH HALVES ARE DECLARED.**

> Otherwise the vocabulary contains a ratchet, and `AX-6` is violated by the grammar rather than by
> any particular rule.

⚠ **THE OPENER HALF WAS MISSING, AND THE CLOSER HALF ALONE IS THE WEAKER ONE (added 2026-09-03).**
The check as first written asks, for every kind, *which verb closes it*. **It never asks which verbs
may OPEN it** — so a hold opened by an undeclared verb passes every gate, and `Seat.conferral`
(*"which ACT fills the seat"*) sits on the schema carrying nothing.

> **State it as one map, load-checked in both directions:** for every `tenure_kind`, the declared set
> of **openers** and the declared set of **closers**. A verb writing `(Tenure, since)` for a kind
> whose opener set does not name it **fails the load**, exactly as a kind with no closer does.

**What this buys immediately:** `Seat.conferral` becomes `hold-kind → {confer | determine | succeed}`
and stops being a field nobody reads — which is `ID-13` closed at the site `§E.2.5` says has *"been
on the Office since #353 carrying nothing."*

**Measured, and it is not an edge case: four of seven relations are open-only** (§E.1.2). A duty
cannot be discharged, a bond cannot be broken, a succession pointer cannot be changed. **The check
is one line — for every verb that writes `(Tenure, since)`, name the verb that writes `(Tenure,
until)` for the same kind** — and it is the check that would have found all four at once.

### **ID-15 · FIRST-CLASS FOR CONSUMERS ≠ FIRST-CLASS FOR STATE.**

> Ask two questions, never one. **What does code need to HOLD?** and **what WRITES it?** When the
> second answer is *nothing*, the thing is a **view** — resolved at a barrier, deployed freely, owning
> nothing.

⚠ **ADDED 2026-09-03. The defect it prevents is one this document committed**: §D.10 listed the
faction under *what has no entity*, which was true of ownership and false of deployment, and left
every consumer to recompute a roster nobody had named. **The single question *"should X be an
object?"* cannot be answered, because it conflates the two.**

**It cuts the other way just as hard**, which is why it is an idiom rather than a permission: a thing
that owns nothing may **never** acquire a field, appear as an actor, or be the subject of an edge.
**A view that starts owning is a carrier nobody declared.**

### **ID-16 · A DESIGN ENUMERATES ITS LOOPS AND SIGNS EACH ONE.**

> Every feedback path appears in the register with a direction. **A model in which every loop is
> negative CONVERGES** — season 40 resembles season 30 — and convergence is not a design goal, it is
> what happens when a design has no other ideas.

⚠ **ADDED 2026-09-03 from an independent governance design (#359 `TL-7`), and the FIRST DRAFT OF THIS
IDIOM SHIPPED A FALSIFIER THAT IS ITSELF THE DEFECT IT NAMES.** It proposed *"count the damping terms,
count the amplifying terms, and a zero in the second column is the finding"* — **a term-grep over
prose**, which is the exact error corrected two sections earlier in this document's own reading of
`amplif*`. A count of words is not a measurement of a model.

> ### **THE REPRESENTATION IS A CYCLE ENUMERATION OVER THE WRITE/READ GRAPH, AND IT IS BLOCKED.**
> A loop is a cycle in *what a verb writes* × *what a verb's precondition reads*. The first half is
> data today (`write_matrix.yaml`). **The second half is a prose string in all 32 rows** — `F.24` —
> so the graph cannot be built and the enumeration cannot be derived. **`ID-16` is therefore stated
> with its blocker named: it is unbuildable until `requires` is typed**, and that is the honest form
> rather than a hand-listed table that would be reference under `§0.05`.

**Why it is worth stating anyway.** This design is made almost entirely of refusals — `T-a` refuses
the stored aggregate, `AX-6` the ratchet, `T-b` the deciding threshold, `ID-5` the silent default —
**and every one of them is a damping term.** A design that can name every way a quantity may be
written, and cannot say which way a loop points across seasons, is missing an axis rather than a rule.
Reading 07 and `F.28` both admit the hole; neither names what would close it.

### **ID-17 · A SUSPENSION IS A UNIFORM RULE, AND ITS LICENSED FORM IS A BAND ON A QUERY.**

> Where a limit lifts, **the lifting is itself a rule applying identically to every entity of a
> kind** — never an exception carved for one.

⚠ **AND THE FORM MATTERS MORE THAN THE PROHIBITION, WHICH THIS DOCUMENT ALREADY HAD THREE TIMES.**
*"A mechanism that special-cases a kind is wrong for every membership"* is stated at `§E.3`, at Stage
2 `§C.2` and at `G.1.6`. **What was missing is what a LAWFUL exception looks like** — and a
prohibition with no licensed alternative is broken quietly by the next session that genuinely needs
one.

> **The licensed form is already in the vocabulary: `T-b`.** A band on a Query **changes what may be
> chosen and never produces an outcome**, and it applies to whoever crosses it. `§D.3`'s site bands
> are the worked instance — damage removes an option rather than adding difficulty. **A suspension is
> a band, or it is a special case wearing a rule's clothes.**

⚠ **The imported version said "attached to a named regime", and `regime` is refused** under `§4`'s
word rule: it is a coinage for a thing `band` already covers, and it arrives carrying a governance
model this design does not have.

### **ID-18 · A PERMANENCE THE SCHEMA GRANTS IS ENUMERATED WHERE A READER WILL MEET IT.**

> `AX-6` binds **game state**. The schema's own permanences — `Tenure`'s no-deletion, `Proposition`'s
> immutability, the append-only log — are authored by the designer and are **listed**, because an
> axiom that quantifies over irreversibilities while its own document lists none is `ID-13` at the
> level of the axiom set.

**The evidence it is needed:** this chain discovered **four ratchets in its own relation vocabulary
by adversarial pass** rather than by reading a register. **A list would have found all four at
once**, which is what `ID-14` says about its own one-line check and what nothing said about the rest.

> ⚠ **NOT a loader invariant.** None of the three is a data row — they are language-level guarantees
> a loader cannot see. **The home is `PART D`**, beside the impossibilities, which is where a reader
> already goes to ask what cannot be spelled.

> ### **THE JOINT STATEMENT, AND IT IS THE POINT OF PART C**
> **ID-9 is about the thing under test; ID-10 is about the instrument.** The defect class the
> handoff names spans both, which is why closing only one reroutes rather than terminates —
> the same result the repository already measured when it closed the guard channel and the
> finding channel opened.

---

# PART D · THE SCHEMA

**Each entry is a DEFINING PREDICATE and an ADMISSION TEST, not a field list.** The field list is
what the predicate produces; the predicate is what answers the next requirement. §0.3 is the reason:
a schema that lists fields can only grow.

**The form is fixed for every entry:**
> **IS** — the one sentence. **OWNS** — what it is the single writer of.
> **ADMITS** — the test a proposed new field must pass. **NEVER** — what may not be on it, with why.

---

## §D.1 · `Person` — **the only thing that can be wrong**

> **IS.** The only carrier of interiority, and therefore the only thing that decides. Everything on a
> Person is one of four things: what they can do, what they hold true, what they hold right, or what
> they are taken to be.
>
> **OWNS.** Everything interior. **Every Tenure whose subject they are.** The Propositions they have
> uttered.
>
> **ADMITS.** *Is it interior to exactly one person, and does something that person decides READ
> it?* **Both halves are required.** A field nothing reads is dead state — which is not a stylistic
> complaint, it is the §22.1 defect: a value initialised once and cited for seasons.
>
> **NEVER.** Anything about another person. Any aggregate. The reverse index of its own ties — that
> is Nobody's.

### §D.1.1 · The fifth category, and the reader clause split in two

The four categories above are all things a person **holds**. `weight` and `capability` are not held —
they are **read off**, by the world, without asking. A cohort's headcount and a practitioner's rank
are facts about a person that the person does not consult in order to decide.

> **FIFTH CATEGORY — what the world reads off a person without asking them.**
> `weight`, `capability`. **And the boundary is already named in the design**: `standing` is defined
> as *the gap between what everyone reads off you and what you hold*. That sentence presupposes both
> sides. **The fifth category is the other side of the design's own most-quoted definition**, so it
> is derived rather than invented to save the test.

**The reader clause therefore splits, and the split is what makes it decidable:**

| category | admitted when |
|---|---|
| what a person **holds** (1–4) | **a decision reads it.** If nothing they decide consults it, it is dead state |
| what the world **reads off** them (5) | **a resolver reads it.** It never enters `choose`, and by `T-f` it cannot |

⚠ **The two clauses are not interchangeable, and using the first on a fifth-category field is what
made this test over-refuse.** `capability` supplies dice at RESOLVE and gates nothing — correct under
the second clause, dead under the first. **A schema test that cannot say which side of `standing` a
field sits on will refuse half the person.**

⚠ **CORRECTED — THIS SECTION SHIPPED A STALE FACT, AND AN ADVERSARIAL PASS CAUGHT IT.** It read
*"`convictions`, `beliefs` and `stance` are declared and **no formula reads any of them**"*. **That
was true of `#353` and false at HEAD:** `W5` landed the scoring function, `score()` sums
`convictions × alignment` inside `choose`, `stance_toward` reads `stance`, and the register row this
was cited to — `H-03` — is marked **DISCHARGED**. Two of the three are consumed.

**What survives is narrower and sharper: `beliefs` is not read — and §D.1's test says a field nothing
reads is not a field. So the schema refuses it, and the resolution is to DELETE it rather than find
it a reader.**

> ### **A BELIEF IS NOT A FIELD. IT IS A `commit` TO AN `OUGHT`.**
> §D.5 already establishes that *a Proposition of mood `OUGHT` is an uttered Belief*, and `commit`
> already binds a person to a Proposition. **So what a person holds RIGHT is the set of `OUGHT`
> Propositions they have committed to** — a Query over edges they already own, stored nowhere.
>
> **Everything the field was for survives, and three things improve.** A belief becomes **utterable**,
> so somebody said it first and can be named. It becomes **shareable**, because two people commit to
> one Proposition and are thereby known to agree. And it becomes **abandonable** by `repudiate`,
> which is `T-m` — where a `strong | wavering | revised` enum on a private field was a state nobody
> could contest.

**`convictions` stays a field and `beliefs` does not, and the asymmetry is the point:** convictions
are the closed axes a person is scored on, which `choose` reads; beliefs are commitments to specific
propositions, which are edges. **The chain had them as two shapes of one thing, and the field was the
wrong one to keep.**

⚠ **AND THE LESSON IS THE DOCUMENT'S OWN `ID-11`, BROKEN BY ITS AUTHOR:** the claim carried no
command, so it could not be re-checked, and it aged into falsehood between two revisions of the
chain. **A schema claim about what code reads must ship the way to re-run it.**

## §D.2 · `Rung` — **the address, never the occupant**

> **IS.** *Where* a decision happens. A Rung owns **arrangements**; a Person makes **choices**. The
> `person` kind is the address slot and the `Person` is who stands in it — and that sentence
> generalises to all eight kinds, which is the container rule.
>
> **OWNS.** Matter (stores, its Sites, its Records, the transmission pointer), dates, envelope, and
> ⚠ `stake` — **which the chain RETIRED as a dead row**, along with `Site.drawers`, `Person.marks`
> and `Person.capability`, because their declared `emits:` name kinds no verb produces. Listing it
> here re-admitted it silently. **It is named as retired, and the reader clause §D.1 carries should
> be on every entry rather than only on `Person` — its absence here is what let this through.**
>
> **ADMITS.** *Is it an arrangement of a place, rather than a choice, a mood, or a reputation?*
>
> **NEVER.** Any social aggregate — no norms, no unrest, no legitimacy, no reputation, no
> discipline-as-a-stored-value. **This is the row the whole ownership table exists to protect.**

⚠ **`judging_set_rule` IS THE LIVE THREAT TO THIS PREDICATE AND IT IS UNSPECIFIED.** If it selects
*who decides*, it is decision-shaped state on a container, and either the predicate needs a third
term or the field belongs elsewhere. **Do not cite "arrangements, not choices" as settled until it
is specified** — and note that this is the same hole (`H-32`, `D11`) that means *nothing is decided
at a sitting*.

## §D.3 · `Site` — **the material particular that accumulates**

> **IS.** A thing in the world whose condition reads its own previous value, and which **gates verbs
> by band**. That is how damage removes an option rather than adding difficulty.
>
> **OWNS.** `condition`, `kind`, and ⚠ `drawers` — **retired as a dead row with `Rung.stake`; see
> §D.2.**
>
> **ADMITS.** *Does it accumulate from its own prior value, and is it physical?*
>
> **NEVER.** Anything social. **And never node-keyed** — a settlement holding a silted harbour at
> `0.1` and a healthy seam at `0.9` collapses to `~0.5`, which keeps the shipping verbs the harbour
> should have closed and closes the mining verbs the seam should have kept: **two wrong answers at
> once.**

## §D.4 · `Record` — **the fact that can leave the head that holds it**

> **IS.** The only way knowledge becomes portable, forgeable, custodial and destroyable. Everything
> a Record does follows from that one property: it can be **held** by someone other than its maker,
> and therefore **taken**, **burned**, or **forged**.
>
> **OWNS.** Its kind, forgery quality, subject matter, ttl, and its act-declared stages.
>
> **ADMITS.** *Does this make a fact transferable, gateable or destroyable?*
>
> **NEVER.** A stage that MATTER advances. **This is the worked lesson:** a case ripening while the
> accused does nothing looks like it wants a MATTER-driven stage. It does not — that is a fourth
> clock, forbidden by AX-5, and *"the fiction of a case advancing is not weather; it is clerks
> filing."* Act-declared terms cost less, keep the capability, and **fix a bug the clock version
> has**: a half-made copy correctly stops if the copyist is jailed, where a MATTER-advanced copy
> finishes itself.

## §D.5 · `Proposition` — **an utterance, fixed at speaking**

> **IS.** What somebody said, immutable from the moment they said it. A `HOLDS` Proposition is a
> claim about the world; an `OUGHT` Proposition **is an uttered Belief** — which is what grounds the
> political layer in a person rather than in a banner.
>
> **OWNS.** Nothing. **It is unowned because nothing may change it**, and it is never destroyed.
>
> **ADMITS.** Nothing. Adding a mutable field to a Proposition is a category error, not an extension.

⚠ **A memberless faction leaves territory held by a banner nobody carries** — uncontestable, because
the holder can never appear at a venue. That is a live defect of immutability, not a reason to
abandon it.

## §D.6 · `Office` — **a seat in a body, carrying a remit**

> **IS.** A standing permission attached to a **seat**, not to a person. It makes **ordinary** acts
> eligible where they otherwise are not, and substitutes the pool source. **It adds no verb and no
> modifier.**
>
> **OWNS.** `post`, `remit`, `conferral`, `revocation`, `establishment`, `dates`, `upkeep`.
>
> **ADMITS.** *Is it a property of the seat that survives the holder leaving it?*
>
> **NEVER.** **Who holds it.** That is a `hold` Tenure, owned by the holder — because an office that
> knows its holder has two homes for one fact.

## §D.7 · `Title` — ⚠ **NOT AN ENTITY. AND THAT IS THE FINDING, NOT A GAP TO FILL BY ADDING ONE.**

> **JORDAN'S RULING, carried in the chain** (2026-09-02, `rosters.yaml: titles`): **three things
> that are not the same, and the chain had modelled none of them.**
>
> | | | |
> |---|---|---|
> | **GOVERNING AUTHORITY** | what a title gives you over a domain | a walk **up** the containment edge from the thing governed to the seat |
> | **HOLDINGS** | what you actually own — **disjoint from what you govern** | a `hold` Tenure whose object is a Rung |
> | **SOVEREIGN POWER** | *"uncontested and absolute"*, and deliberately **not** monopolised | ❌ **no representation at all** (`H-90`) |
>
> **A Title IS a rank whose domain is a rung kind**, so rank is the ordinal position in `rung_kinds`
> and needs no second scale. `Lord` is the row to read twice: a Lord governs territories *not
> assembled into a province*, so a Lord may govern several while a Count governs one — **rank is not
> headcount.**

### §D.7.1 The conflation, stated precisely enough to act on

**Today a Title is an `Office` whose `post` happens to appear on a roster.** `titles_held` finds
`hold` Tenures whose object is in `w.offices` and whose office's `post` has a `title_domain`. So the
model has **one class doing two jobs** — a rank on the governance ladder, and a seat in an institution
— and `Office.__post_init__` patches the collision by refusing a `post` that is both a title and a
body.

⚠ **That refusal blocks a real error** (a King seated in a Church chair) **by asserting the two are
MUTUALLY EXCLUSIVE CATEGORIES, which Jordan's ruling contradicts** — offices *confer* titles, so they
are different kinds of thing that stand in a relation, not two values of one kind. **It is a symptom
marker. Decide the entity model, then keep or drop it on purpose.**

### §D.7.2 **Why the title ladder has a REVOKE path and no CONFERRAL path — the actual cause**

This is the handoff's *"clearest single piece of evidence that the entity model is wrong rather than
merely incomplete"*, and the cause is narrower and more fixable than that framing suggests.

> **THERE ARE TWO ELIGIBILITY MODELS IN THE TREE, AND ONLY THE REVOKE SIDE GOT THE SECOND ONE.**
>
> | | model | where |
> |---|---|---|
> | Part E's | **`remit:<act>`** on the particular office | every verb row in `verb_table.yaml` |
> | Jordan's governance canon | **RANK + CONTAINMENT** — *"a Duke can revoke office from any individual in that office so long as that office is for a holding under their purview"* | `under_purview`, read by `_req_revoke` |
>
> `revoke` was rebuilt on the second model. `confer` was not. **So conferral is not missing a
> mechanism — it is running the wrong one**, and the asymmetry is a half-landed ruling rather than a
> hole in the ontology. `shape.py` says so itself: the difference is *"registered rather than
> resolved here (`H-90`)."*

**The schema question this leaves is real and is not that one:** whether `hold : Person → Rung`
should carry **governing** or **owning**, given Jordan ruled them disjoint. See §E.2.

## §D.8 · `Tenure` — **the one edge**

> **IS.** Every relation in the game, in one shape, **owned by its subject**. One home, one writer,
> no reach-through; the object side is a derived index, never stored.
>
> **ADMITS.** A new `kind` only where no existing kind carries the meaning. *(H-101 is exactly this
> question, and §E.1 argues the answer is no new kind.)*
>
> **NEVER.** Deletion. `until?` is what makes an ended relation a **fact** — argued over, read for
> entrenchment. Delete the row and `entrenchment = min(1, seasons_held/60)` has nothing to read.

⚠ **AND THAT IS ALSO THE HAZARD:** because ended Tenures persist, any count over live *and* ended
edges is monotone — a ratchet built entirely from structural edges. Under **T-a** this needs no
special clause: such a count has no owner.

## §D.9 · `Event` · `Act` · `Claim` — **the three tenses of a happening**

> **`Act` IS what one person chose.** **`Event` IS what happened** — carrying no actor and no target
> (T-d, T-e), with `causes[]` required and non-empty, `[ROOT]` where there is genuinely no
> antecedent. **`Claim` IS what one person concluded** — with its provenance, its confidence, and its
> capacity to be wrong.
>
> **The three are the same occurrence at three distances**, and the distance is the design: an Act is
> certain to its actor, an Event is neutral, a Claim is one person's version. **Collapsing any two of
> them deletes a mechanism** — collapse Act and Event and attribution becomes certain; collapse Event
> and Claim and everyone witnesses identically.

## §D.10 · What has no entity, and correctly so

| the thing | what it actually is |
|---|---|
| a **faction** | ⚠ **AMENDED — see §D.11.** A `Proposition` plus its `commit` edges is what it OWNS; it *does* exist as an object, as a **resolved view** |
| an **address** | a `contain` Tenure |
| a **need** | a `Sensation` plus a Query |
| **annexation** | a `hold` at distance — **not a verb** |
| **secession** | the `commit` edges moving — **not a verb** |
| every **aggregate** | a Query, owned by Nobody (T-a) |

## §D.11 · `Faction` — **a resolved view. First-class for consumers, never for state**

⚠ **AMENDED 2026-09-03, Jordan-directed.** Verbatim: *"factions can't act by themselves, but they
should be available as an abstraction for all the people who belong to that faction such that the
game code can actually deploy it."*

**§D.10 above was correct about OWNERSHIP and wrong about DEPLOYMENT.** Saying a faction *has no
entity* left every consumer — the battle seam, the port, the decision policy — to recompute a set
nobody had named.

```
Faction := ( proposition : PropositionId   -- identity. Immutable, uttered by a named person
           , members     : PersonId[]      -- live `commit` edges
           , holdings    : RungId[]        -- the union of its members' holds
           , seats       : SeatId[]        -- the seats its members hold
           , head?       : PersonId        -- by the proposition's own rule
           )
```

**Built at a barrier, handed to whatever needs it, discarded there.**

> **IS.** The people committed to one uttered proposition, resolved on demand.
> **OWNS.** ⛔ **NOTHING.** Every field above is a Query over edges other things own.
> **ADMITS.** ⛔ **No field, ever.** A field needs an owner and a faction has none.
> **NEVER.** `Act.actor` · a `contest` claimant · a `hold` subject · a parameter of `resolve`.

| `AX-1` still holds because | code gets what it needs because |
|---|---|
| it has **no verbs** | it is a real object with real rosters |
| it is never `Act.actor` | the battle seam iterates `members` |
| `resolve` has **no faction parameter** | the port and the UI take one |

⚠ **AND THE RESOLVED FORM BEATS A STORED ONE ON ITS OWN TERMS: IT CANNOT GO STALE.** A stored roster
drifts from the commit edges and needs a reconciliation pass; a resolved one **is** the edges. The
`hold`-subject prohibition stays exactly as it was — it is what prevents **territory held by a banner
nobody carries**, uncontestable because the holder can never appear at a venue.

> ### **THE GENERAL RULE, AND IT IS WORTH MORE THAN THIS ENTRY**
> **AN ABSTRACTION MAY BE FIRST-CLASS FOR CONSUMERS WITHOUT BEING FIRST-CLASS FOR STATE.**
> *"Should a faction exist as an object?"* was the wrong question, because it conflated **deploying**
> with **owning**. Ask instead: *what does code need to HOLD?* and *what WRITES it?* — **and when the
> second answer is nothing, you have a view, not a carrier.** `ID-15` states it as an idiom.

---

# PART E · THE OPEN QUESTIONS, DERIVED

**Scope, and it is the rule this document broke once and now states at the top of the Part that
broke it:** the admissible sources are **the axioms above and the PR chain #337 → #357**. Nothing
under `canon/`, `systems/` or `research/` is authority here. We are designing an idealized system;
**prior work is not a constraint on it.**

⚠ **A FIRST DRAFT OF THIS PART WAS BUILT ON A SWEEP OF `canon/` AND `systems/`, AND IS WITHDRAWN IN
FULL.** Not because what it found was wrong, but because *evidence that something is already so* is
not an argument that it *should* be so — and an idealized shape argued from the existing tree is the
existing tree with better prose. **Every claim below is derived from PART A or from a Jordan ruling
carried in the chain, and nothing else.**

---

## §E.1 · `H-101` — subordination. **It IS storable, and the reason it looked otherwise is a ratchet in the vocabulary**

⚠ **THIS SECTION IS A CORRECTION. Its first published answer was wrong, and the wrongness is
recorded rather than overwritten**, because a superseded derivation that stays legible is how the
next session avoids re-deriving it.

> **WHAT IT SAID:** subordination *cannot* be stored — an edge between two immutable Propositions has
> no owner, `AX-4` forbids it, therefore it is a Query at every scale.
>
> **WHAT WAS WRONG:** the step is locally sound — no `tenure_kind` takes a Proposition as **subject**
> — but **it never established that the edge is Proposition→Proposition.** That premise was smuggled.
> And the alternatives table refuted a strawman: *a new `under` kind **with a stage field***, where
> the whole refutation lands on the stage field and none of it on the edge.

### §E.1.1 The candidate the register already names, and the derivation that was missed

`H-101`'s own text: *"the candidates are `tenure_kinds` members **already rostered** (`oblige`, `tie`)
rather than a ninth rung or a second ladder."*

`oblige : Person → Person | Office`, many, **owned by its Person subject** — and it survives every
axiom the Query version was invented to satisfy, better:

| | the Query version | **an `oblige` edge** |
|---|---|---|
| `AX-4` — one owner | Nobody owns it | **the person who swore it owns it** |
| `AX-1` — a person acts | ⚠ **nobody authored it** | **a named person swore it, at a venue, paying budget** |
| new `tenure_kind`? | none | **none** — it is rostered |
| detachment | people drift, and a number falls | **a named person forswears.** The event has an author |

> **THE SECOND ROW IS THE ONE THAT DECIDES IT.** A Query is a fact about a population that nobody
> chose. An `oblige` edge is a promise somebody made. **`AX-1` says the second is what this game is
> made of** — and it is the difference between *the Löwenritter drifted* and *the Grandmaster
> forswore the King*, which are not the same story.

### §E.1.2 · **CLOSURE IS NOT A VERB. IT IS A CONSEQUENCE OF OWNERSHIP.**

Asking *which verb ends an `oblige`* is the wrong question, and the four-relation table below is
what asking it wrongly looks like. **The design question is: what must be true of a relation so that
open-without-close cannot be expressed?**

> ### **T-m · AN OWNER MAY ALWAYS END WHAT THEY OWN.**
> **From `AX-4` + `AX-1`.** A Tenure is owned by its subject and the owner is its only writer.
> `until` is a field of the Tenure. **Therefore writing `until` is already within the owner's
> authority, and needs no separate grant.** Ending a relation you hold is not a capability the
> vocabulary confers on you — it is the same authority by which you hold it.

**This is the whole repair, and it is one sentence rather than four verbs.** A vocabulary that gates
`(Tenure, until)` per-verb has made closure a privilege to be remembered. A vocabulary that gates it
per-owner cannot forget, because there is nothing to remember: **the writer is already established
by who the subject is.**

> ### **T-n · AN END THAT IS NOT THE OWNER'S DISCRETION IS DECLARED BY THE ACT THAT OPENED IT.**
> **From `AX-6` + `T-c`.** Some relations should not end at the holder's whim — a term of service, a
> wardship that lapses at majority. But an end condition nobody declared is **a clock nobody wound**,
> which `T-c` forbids. **So the opening act declares the terms**, exactly as §13.1 has an
> Inquisitor's `open_case` declare its stages rather than letting MATTER advance them.

⚠ **CORRECTED 2026-09-03 (F3). THE FIRST WORDING SAID `T-m` AND `T-n` ARE EXHAUSTIVE AND THAT
*"THERE IS NO THIRD WAY"*. THE TREE HAS TWO INSTANCES OF THE THIRD WAY AND HAS HAD THEM ALL ALONG.**

`verb_table.yaml` carries **`revoke`** (eligibility `remit:revoke`, `writes: [Tenure.until]`) and
**`confer`** (eligibility `remit:confer`, `writes: [Tenure.until, Tenure.since]`). **In both, a
person who is not the Tenure's subject writes its `until`.** That is neither the owner's discretion
nor a term the opening act declared.

> ### **THERE ARE THREE WAYS, AND THE THIRD IS NOT A DEFECT — IT IS WHAT AN OFFICE IS FOR.**
>
> | | authority | who |
> |---|---|---|
> | **`T-m`** the owner's discretion | `subject == actor` | the holder |
> | **`T-n`** a declared term | the Tenure's own `term`, set by the opening act | MATTER, or the term's `closer` |
> | **`T-o`** ⚠ **NEW · a REVOCATION declared on the seat** | the **Seat's** `revocation` basis, exercised through `Act.via` | a superior, at a venue, paying an act |
>
> ### **T-o · A SEAT MAY END WHAT ITS REMIT REACHES, AND THE SEAT DECLARES THE REACH.**
> **From `AX-1` + `§E.2.2`.** Authority is a property of the seat being exercised. A revocation is
> therefore not a person overriding an owner — **it is the seat's declared remit, exercised by
> whoever currently occupies it**, and it is refused the instant the occupant is not seated.

**Why this is a repair and not a widening.** The exhaustiveness claim was doing real work — it is
what makes open-without-close unspellable — and `T-o` preserves it, because **a revocation is still
DECLARED, on the Seat, at `establish` time.** What changes is *where* the declaration lives: `T-n`
puts it on the Tenure, `T-o` puts it on the Seat. **Three declared ways is still a closed set; two
ways plus an undeclared verb that quietly does a third thing is not.**

⚠ **AND IT NAMES A REAL DEFECT THE FIRST WORDING HID: `Seat.revocation` and `Tenure.term.closer`
are two homes for *who may end this hold*.** That is `G.2.1`'s own *"you can name two"* test firing
inside the schema. **The Seat's is authoritative** — a term's closer names a *basis*, and the basis
resolves against the seat. Say so at both sites or the next session will write the third.

⚠ **THE PRICE, NAMED BECAUSE IT IS REAL.** Under `T-m` a duty can always be forsworn, which sounds
like duties stop binding. **They bind by cost, not by impossibility.** Forswearing spends an act from
a budget of ~5, it emits, and witnesses mint claims about it — so what a person cannot do is forswear
*unnoticed*. **That is the same shape as `T-g`: the design does not prevent the move, it makes the
move visible and expensive.** A duty nobody may leave is a duty no drama can attach to.

### §E.1.3 · What `T-m` forces, which is where the shape actually changes

Applying it is not a tidy-up. **Two of the seven relations cannot satisfy `T-m` as they are shaped,
and in both cases the shape is what has to move.**

**`tie` and `knot` — a symmetric relation cannot have a single owner.** They are stored once, on the
lower-id endpoint, so under `AX-4` the *other* person owns nothing and by `T-m` cannot end a
relation they are inside. **Whether you can walk away from a bond would depend on an id comparison**,
which is not a thing the fiction can express.

> **The shape that satisfies both rules: two directed edges, each owned by its subject.** A tie is a
> **regard**, and regard was never symmetric — which is the epistemic posture the rest of the design
> already takes. It also buys the most interesting case for free: **I have cut you off and you do not
> know it**, which is `AX-2` at the level of relationships.
>
> **The counter-argument the chain gives is real and survives**: a shared `strain` on two directed
> records has two homes and can disagree with itself. **The resolution is that they are two different
> things.** Regard is owned per endpoint; strain is the *interaction* of the two regards, and by
> `T-a` an interaction of two owners' values is a **Query**, stored nowhere. The chain reached for
> one storage location because it was storing an aggregate.

**`succeed` — its subject is a `Rung`, and a Rung cannot act.** By `AX-4` the rung owns the edge; by
`AX-1` the rung can never write anything. **So it has an owner that cannot author**, and `T-m` has no
one to name. This is not a missing verb — **it is the only Tenure whose subject is not a person, and
that is why it is the only one nothing can end.**

> **The shape that satisfies `T-m`: succession is a disposition of the holder, not a property of the
> place.** The person who holds the rung declares who follows them — owned by the holder, endable by
> the holder, and lapsing on their death through the same causation rule §15.3 already gives death
> over `until`. **A pointer the place owns is a pointer nobody can change; a pointer the holder owns
> is an act of politics**, which is what succession is.

**The general result, which is the part worth carrying into Stage 2:**

> ### **AN EDGE WHOSE SUBJECT CANNOT ACT IS NOT A RELATION. IT IS A FIELD WEARING A RELATION'S SHAPE.**
> `contain` is the honest case — `Rung → Rung`, subject cannot act, and it is correctly not something
> anybody ends by choice; it moves when a person moves. **Every other edge whose subject cannot act
> should be re-subjected onto the person whose act maintains it, or admitted to be a field.**

**The evidence this was worth doing, stated once and not dwelt on:** of seven relation kinds, four
have no closing verb today — `oblige`, `succeed`, `tie`, `knot`. `T-m` and `T-n` account for all
four, and the two schema corrections above are what applying them costs.

### §E.1.4 What survives from the withdrawn version — the *de jure* / *de facto* gap

**The gap survives, and the correction makes it better.** The old version put *de jure* in an
immutable Proposition, which had no un-utter and no arbiter — **a permanent ratchet, and the same
defect this section just found in the vocabulary.** An `oblige` edge with a closable `until` is
revocable, authored on both sides, and owned.

> **`de jure` is the sworn edge. `de facto` is the commitment overlap, a Query.** `AX-2` guarantees
> they can disagree and that nobody has privileged access to which is real; **`T-b` makes a band on
> their gap change what may be chosen and never produce an outcome.**
>
> **The general result stands and is the part worth carrying: where the chain reaches for a TRACK,
> look for two things that can disagree and band their gap.** A track is a stored aggregate wearing
> a stage's clothes.

### §E.1.5 The office scale — **RESOLVED, and `T-m` is what un-splits it**

An earlier pass split `H-101`: the faction half derived, the office half not. **The split was an
artifact of framing office subordination as a containment of REMIT SCOPES** — under which the only
thing that could change the relation is the superior's own `establish` act, requiring an institution
to voluntarily record its own involuntary loss. That is the one thing a detachment never is, so the
falsifier fired correctly against that framing.

> ### **`T-m` DISSOLVES IT: SUBORDINATION IS SWORN BY A PERSON, AT BOTH SCALES.**
> A scope containment has no author and no owner. **An `oblige` has both.** The Cardinal obliges to
> the Confessor exactly as the Grandmaster obliges to the King — `Person → Office` and
> `Person → Person` are the **same rostered edge**, and `oblige`'s domain already admits both.
>
> **So `H-101` keeps its one-row justification, for a better reason than it had:** not *"two scales
> happen to share a shape"* but *"there is one relation, and it was never institutional."*

**What this buys, each being something the scope framing could not say:**

- **A body's subordination is exactly as strong as the people currently seated in it.** A Cardinal
  who forswears takes the See's hold on him with him, and his successor starts unbound.
- **Detachment has an author and a date.** Somebody forswore, at a venue, and witnesses minted claims
  about it — so it can be denied, misreported, or not yet known.
- **Two arms of one body may differ.** One Cardinal loyal and one not is the ordinary case rather
  than an unrepresentable one, because there is no single institutional edge to hold one state.
- **Nothing institutional needs a write.** `(Office, rung)` having no write-matrix row stops being a
  blocker, because the relation was never on the office.

### §E.1.6 · **WAR IS THE SECOND INSTANCE OF THIS PATTERN — added 2026-09-03**

Jordan: *"it should be possible for factions to be flagged at war with another one."*

⚠ **AND THE COMMITMENT-ONLY MODEL HAS A REAL GAP HERE, WHICH THIS SECTION DID NOT SEE.** It cannot
express **a war that outlives its supporters** — the normal historical case. Under commitments alone
a war evaporates the moment enthusiasm does, which is wrong.

> **The fix is the shape this section already found. A declaration of war is a Proposition somebody
> UTTERED, plus an owned edge; peace is `until` written on it.**
>
> | | |
> |---|---|
> | **de jure** | the uttered war, persisting until somebody makes peace |
> | **de facto** | the commitment share, which may be near zero |
> | **the gap** | *"we are still at war, and nobody will muster"* |

**Why not a boolean between two faction objects:** a boolean has **no owner**, so nothing could end
it and nobody declared it — and no duke could refuse to fight a war his king declared.

> ### ⚠ **TWO INSTANCES MAKE IT THE PATTERN, NOT A SPECIAL CASE FOR `H-101`.**
> **Subordination and war are the same shape: an uttered Proposition · an owned edge · a gap between
> the sworn and the actual.** Expect a third. **When the design next reaches for a relation between
> two things that cannot act, this is the shape to reach for first.**

### §E.1.7 · **WHAT IS OWED — the pattern's third slot, which this section had and did not use**

⚠ **ADDED 2026-09-03, and it closes an over-refusal committed against this document by its own
evaluator.** An external design (#359) attaches a `contract : { levy, tax, obligations, autonomy }`
to its subordination relation, and a cross-read graded that *"a real question #358 leaves open"* on
the ground that `oblige` carries a subject, an object, dates and a term, and **what is owed is
nowhere.** That grade was wrong, and the derivation is one step:

> ### **AN OATH IS AN UTTERANCE. WHAT IS OWED IS THE `OUGHT` PROPOSITION IT UTTERS.**
> `§D.5` already establishes that *a Proposition of mood `OUGHT` is an uttered Belief*, and `commit`
> already binds a person to a Proposition. **An `oblige` whose terms are an `OUGHT` Proposition is
> the pattern this section just named, with its third slot filled** — the utterance carries the
> terms, the edge carries the swearing, and the gap between them is the Query.

**And it is better than a field of four columns**, for the reasons the pattern is worth having:

- **The terms were SAID by somebody**, at a venue, and can be quoted, disputed and misreported.
- **Two people may swear to the same terms** by committing to one Proposition, and are thereby known
  to have sworn the same thing — where four columns on two edges can silently differ.
- **The terms are immutable**, so *renegotiation* is a new utterance and a new edge, which is what
  renegotiation is. A mutable `contract` field would be a treaty nobody signed.
- **Breach is the sworn/performed gap** — a Query, banded under `T-b` — rather than a boolean nobody
  authored.

> **The lesson is the evaluator's, not the design's: an error AGAINST the design looks like rigour.**
> The cross-read had `§E.1.6`'s pattern in front of it, had already banked it as the section's best
> result, and still graded the slot empty. **`G.4.3` names this direction and it fired anyway.**

> ### **THE GENERAL RESULT, AND STAGE 2 INHERITS IT**
> **THERE ARE NO INSTITUTIONAL RELATIONS. THERE ARE ONLY PEOPLE'S RELATIONS, READ IN AGGREGATE.**
> A faction under a faction, an office under an office, a chain of command, a body's loyalty — each
> is a Query over the sworn edges of the persons currently seated. **`AX-1` said only a person ACTS;
> this says only a person RELATES**, and the second follows from the first the moment `T-m` makes
> ownership the source of authority.

## §E.2 · Delegation — **RULED BY JORDAN, 2026-09-03: regency and puppet rulers MUST be possible**

> **Verbatim: *"Regency and puppet rulers must be possible."***

**This was the one question §F.3 sent to Jordan, and the answer does not pick either option that was
offered. It dissolves them** — because deriving what regency actually *requires* shows that the
blocker was never the one named.

### §E.2.1 What regency requires, derived

**A regency is: the title stays with one person; another governs the domain.** A puppet ruler is the
same shape read the other way — one person holds the title, another exercises the authority.

> **So the requirement is exactly: THE TITLE AND THE GOVERNING MUST BE SEPARABLE.**

Now ask what makes a governance act eligible. The chain carries **two answers**, and §D.7.2 already
found that only `revoke` was rebuilt on the second:

| model | conferrable? |
|---|---|
| **`remit:<act>`** on an office | ✅ **yes — `confer` is the verb that does it** |
| **RANK + CONTAINMENT** — the actor holds a title whose domain contains the holding | ❌ **no.** It reads the actor's **own** title-holds and walks containment. **There is no seam by which a delegate enters** |

> ### **THE BLOCKER IS NOT THE `hold` OVERLOAD. IT IS THAT RANK+CONTAINMENT IS NOT CONFERRABLE.**
> A regent has no title over the domain — that is what makes them a regent. Under rank+containment
> they are ineligible, and no amount of conferring changes it, because the check never looks at
> anything that can be conferred. **Delegation is unbuildable under that model by construction**,
> which is why `H-90` records it as unbuilt rather than as merely unwritten.

### §E.2.2 The axiom this forces, stated as one sentence

> ## **AUTHORITY IS A PROPERTY OF THE SEAT BEING EXERCISED, NEVER OF THE PERSON EXERCISING IT.**

**Everything Jordan named falls out of that sentence and nothing else is needed:**

| | is |
|---|---|
| a **title** | a seat on the governance ladder, whose scope is a rung kind and everything it contains |
| an **office** | a seat in a body, whose scope is its `remit.scope_rung` |
| **delegation** | **conferring a seat.** `establish` the seat, `confer` it, `revoke` it — three verbs the table already carries |
| a **regency** | a seat conferred over the domain **while the title stays put.** The child keeps the crown; the regent governs; `revoke` at majority |
| a **puppet ruler** | the mirror — the puppet holds the title, and the seat carrying its remit has been conferred elsewhere. **Nobody had to write a "puppet" mechanism** |
| **rank + containment** | **the special case** where the seat being exercised is the actor's own title |

⚠ **AND THIS IS WHY THE CONFERRAL PATH WAS THE HALF THAT WENT MISSING** (§D.7.2). Under
"authority belongs to the person" you only ever need to check it — which is `revoke`. Under
"authority belongs to the seat" you must also be able to **hand it over**, which is `confer`. **The
tree built the model that does not need conferral, and then found conferral missing.** The asymmetry
was the symptom; this is the cause.

### §E.2.3 What it settles about `hold`, and it is the reading that was NOT the delegation lever

**`hold` on a Rung means OWNING — holdings — and governing authority is a seat.** Jordan's own
earlier ruling already says so operationally: *"King/Queen cannot revoke title of Duke/Duchess if
they do not have duchy is in their holdings."* **Holdings GATE the act; they are not the authority.**
Two distinct terms in one predicate, which is what `_req_revoke` computes and what its three-term
conjunction is.

⚠ **A CORRECTION TO THIS DOCUMENT'S OWN EARLIER FRAMING, RECORDED RATHER THAN OVERWRITTEN.** An
earlier §E.2 posed this as *"`hold` means owning"* **versus** *"`hold` means governing, and only the
second makes delegation expressible."* **That was wrong.** Delegation is expressible under the
*first* reading, once authority is a property of the seat — and the second reading would have made
governance authority a `hold` on a Rung, which is **not conferrable to someone who does not hold the
rung**, i.e. it would have failed the very requirement it was offered to satisfy. **The menu was
false and the derivation is what caught it.**

### §E.2.4 The cost, and the falsifier

**Cost: one unification, not one addition.** Governance acts must evaluate eligibility through the
conferrable channel. `tenure_kinds` does not move; no new carrier; `establish`/`confer`/`revoke`
already exist. **What must change is the check, and `_req_revoke` is the site.**

⚠ **And a real consequence, named rather than discovered later:** if a regent's authority is a
conferred seat, then **purview must be asked of the SEAT being exercised, not of the actor** (§E.1.3).
A regent exercising a conferred remit has the *office's* purview, not their own — and a Query that
reads the actor's own title-holds gives the wrong answer for every delegate.

### §E.2.5 Delegation's three shapes — **RULED THE SAME DAY, and the third one earns its place**

> **Jordan, 2026-09-03: *"Same with delegation."*** And the chain's own statement of what delegation
> covers: *"All of Kings, Dukes, Counts and Lords can assign others of lesser rank to govern any of
> their holdings in their stead"* — **a governor for a duchy, a council for a province, mayoral
> elections for a settlement.**

**All three are the same sentence, and none needs a new primitive:**

| shape | is | mechanism |
|---|---|---|
| **a governor** | one person conferred a seat over the holding | `establish` → `confer`. The title never moves |
| **a council** | **one seat, many holders** | ⚠ **not N seats.** `hold` is **1-per-object** (§D.8), so a council is one Office whose **`establishment[]`** is its membership — *"the named persons the office employs. Finite, contested, durable"* — and §D.6's pool substitution already reads it |
| **a mayoral election** | ⚠ **a seat filled by a PROCESS, not by a superior** | a Date fires; the judging set decides; the decision opens the `hold`. **`determine`, not `confer`** |

> ### **THE THIRD SHAPE IS THE ONE THAT TEACHES SOMETHING: CONFERRAL IS NOT THE ONLY WAY A SEAT IS
> FILLED, AND THE SCHEMA ALREADY SAID SO.**
> §D.6 gives an Office a **`conferral`** field — *"the basis, **per office**"* — which is exactly the
> slot that distinguishes *the Duke names him* from *the burghers elect him* from *it passes to the
> eldest*. **Delegation does not need a delegation mechanism. It needs the `conferral` basis to be
> specified**, and that field has been on the Office since #353 carrying nothing.

⚠ **AND THIS IS WHY "AUTHORITY BELONGS TO THE SEAT" IS LOAD-BEARING RATHER THAN TIDY.** If authority
belonged to the *person*, an election would have to *transfer* something from the electors — who
have nothing to give, because they were never governing. **It is only because the seat carries the
authority that a body with no authority of its own can decide who occupies it**, which is what an
election is and what a regency council is.

**And the political consequence, which is the point of doing this top-down:** a seat that can be
filled three different ways is a seat worth **fighting over three different ways**. Conferral is
bought and owed; an election is canvassed; succession is bred for. **One primitive, three genres of
play, no branch in the resolver** — which is `T-g`'s shape (obstruction needs no verb) at the
institutional scale.

> **FALSIFIER.** *Find an authority in the chain that must be exercisable by a person to whom no seat
> could be conferred.* If one exists, authority is not purely a property of the seat and this
> section needs a second term. **Sovereign power is the candidate** — `H-90` records it as having no
> representation at all, and *"uncontested and absolute"* may be precisely the thing that cannot be
> handed over.

## §E.3 · The ladder — what is architectural, and what is merely content

The chain ships `rung_kinds` as eight ordered values and treats the roster as settled. **The axioms
say almost none of that is an architectural question.**

> **ARCHITECTURAL, and fixed by the axioms:** one `Rung` type, many kinds (**ID-7**); the kinds are
> **ORDERED**, because a title's rank is its domain's ordinal and that needs no second scale; the
> parent relation is a **stored edge, not a label**, because **ID-8** — *a label cannot be walked*,
> and every purview question in §E.1.3 is a walk.
>
> **NOT ARCHITECTURAL:** **which** kinds exist, and how many. That is content, and by **ID-12** it
> lives in data and is changed by editing a list.

⚠ **AND THE FALSIFIER FIRES THREE TIMES TODAY, SO THIS IS A PRESCRIPTION, NOT A DESCRIPTION.** The
chain contains `here.kind == "person"` inside a resolver precondition — literally the shape named
below as scripting drift; the verb table hard-names four rung kinds in its `scale:` column and is
validated against the roster **at load**, so removing a kind fails the load rather than editing
data; and the titles table is declared **total** over `rung_kinds`. **The coupling is already known
to be silent and load-bearing** — the chain records an office silently *becoming a title* on a
one-line roster addition, flipping its revocation rule, with the suite green.

**So `rosters.yaml`'s own promise — that changing a definition "touches no other system" — is false
today.** The architectural claim stands as a claim about what the shape SHOULD be; it is not a
description of what it IS, and the difference is `ID-13`: a roster is only data if nothing branches
on its members.

**The consequence for an idealized shape:** do not spend design effort ruling the roster's
membership. **Spend it on the two properties that are load-bearing** — that the ladder is ordered,
and that it is walked rather than labelled — **because a mechanism that reads the ordinal and walks
the edge is correct for any membership, and a mechanism that special-cases a kind is wrong for
every membership.** ⚠ If you find yourself writing `if kind == "duchy"`, that is scripting drift and
the ladder has stopped being data.

---

# PART F · WHAT STAGE 2 INHERITS, AND HOW TO FALSIFY THIS

## §F.1 · The seed question, answered as far as Stage 1 reaches

> *"what comprises a person, faction, office, site, etc?"*

| | answer | derived from |
|---|---|---|
| a **person** | the only thing that can be wrong | AX-2 · §D.1 — ⚠ its own admission test **fails today** on `convictions`/`beliefs`/`stance` (`D21`) |
| a **faction** | a Proposition plus its `commit` edges | **T-h**, derived from AX-1, not stipulated |
| an **office** | a seat in a body carrying a remit; adds no verb and no modifier | §D.6 |
| a **title** | a rank whose domain is a rung kind — **not an entity, and not an Office** | §D.7; the conflation is a half-landed ruling, §D.7.2 |
| a **site** | the material particular that accumulates and gates | §D.3 |
| **subordination** | ⚠ **CORRECTED: an `oblige` edge, owned by the person who swore it** — not a Query. The first answer was wrong and §E.1 records why | §E.1.1 |
| **authority** | **a property of the SEAT being exercised, never of the person** | §E.2.2 — forced by Jordan's 2026-09-03 ruling |
| **a regency · a puppet · a delegation** | **a conferred seat.** No mechanism for any of the three | §E.2.2 · §E.2.5 |

## §F.2 · Stage 2, and the two things it must not do

Jordan's ordering: **axioms/idioms/schema → hierarchies, dependencies, nests, scales → verbs,
consequences, slices, season loops.** Stage 2 takes the second, and inherits four results:

1. **Two topologies, kept apart** — a containment tree governed by R-1/R-2, and a lateral graph that
   is not. Subordination is lateral (§E.1.4).
2. **Purview is a Query over several edge kinds**, not a relation to be stored (§E.1.1 step 3).
3. **Where the chain reaches for a TRACK, look for two things that can disagree and band their
   gap** (§E.1.3). This is the general form, and the arc corpus is full of tracks.
4. **The ladder's membership is content; its ordering and its walkability are architecture** (§E.3).
5. **Authority belongs to the seat, so purview must be asked of the SEAT being exercised, not of the
   actor** (§E.2.4) — a Query that reads the actor's own title-holds gives the wrong answer for
   every delegate, and delegation is now ruled in.
6. ⚠ **The relation vocabulary contains four ratchets** (§E.1.2). Four of seven tenure kinds can be
   opened and never closed. **Stage 2 cannot reason about hierarchies while the edges that make them
   are irreversible**, so this is a precondition of Stage 2 rather than a finding beside it.
7. **A declared field that reaches no reader is not a mechanism** (`ID-13`) — and the `scale:`
   column, which Stage 2 is precisely about, is the chain's own third instance of that defect.
8. ⚠ **First-class for consumers is not first-class for state** (`ID-15`, §D.11). Stage 2 decomposes,
   and **the unit of decomposition is an owner — so a thing that owns nothing is never a unit**, however
   freely code deploys it.
9. ⚠ **The uttered-declaration pattern has two instances** (§E.1.6) — subordination and war. **Stage 2
   should expect the third rather than model it as a special case.**

> ⛔ **Do not build a second ladder.** ⛔ **Do not index code by scale** — a module is registered
> against a role and runs at whatever rungs the step hands it. Scale-indexed code is scale-divergent
> code, invisible until something composes across a boundary, and it deletes the one property that
> makes eight kinds of one type worth having.

## §F.3 · Open — and only one is Jordan's

> ### ✅ **THE ONE QUESTION THIS DOCUMENT SENT TO JORDAN IS RULED, AND THE QUEUE IS EMPTY.**
> *"Regency and puppet rulers must be possible."* · *"Same with delegation."* (2026-09-03, §E.2)
> **It did not pick either option offered — it showed the menu was false**, and the answer is
> `AUTHORITY IS A PROPERTY OF THE SEAT BEING EXERCISED` (§E.2.2).

| still open | who answers it |
|---|---|
| **`Office.conferral`'s VOCABULARY** — *named · elected · inherited · …* | **content, not architecture** (§E.3's rule). The architecture is settled: the basis names **which act fills the seat**, and an election is `determine`, not `confer` |
| **What a particular ending COSTS** in standing, matter or Momentum | **Stage 3.** `T-m` settles that the price is *an act* and the binding is *the consequence*; per-verb pricing is the verb table's business |

**Everything else this document touches was closed by derivation, and each closure names its ground.**

## §F.4 · Falsifiers

| claim | what would show it wrong |
|---|---|
| **the six axioms are independent** | derive any one from the other five. **`AX-5` is the standing candidate** — if the three-item list is itself derivable, the set is five. ⚠ **`AX-6` was found by this falsifier firing on the first publication**, so the falsifier is live and has a hit rate |
| **`AX-6` is not itself two axioms** | show a permanence the *relation* case needs and the *ratchet* case does not, or the reverse — that would split it |
| **T-a: L3 is a theorem of AX-4** | an aggregate with exactly one owner that AX-4 permits and L3 refuses |
| **§E.1: subordination is a Query, not an edge** | a subordination whose de facto state is not recoverable from `commit` edges and remit scopes |
| **§E.3: roster membership is not architectural** | a mechanism that is correct only for one particular set of rung kinds |
| **the admission tests decide real cases** | a field the test admits that should be refused, or refuses that should be admitted. ⚠ `(Person, convictions)` is currently **refused by §D.1 and mandated by the design** — which is `D21`, and is the test working |
| **PART C closes the defect class** | a new instance of *"reports success for something that did not happen"* that neither `ID-9` nor `ID-10` catches |
| **`ID-15` — a view may own nothing and still be deployed** | a consumer that genuinely needs a faction to hold state of its own, which no owner elsewhere can carry. ⚠ **The battle seam is the live candidate and has not been tested** |
| **§E.1.6 — war is an uttered declaration, not a flag** | a war whose beginning no person authored, that the design nonetheless needs. If one exists, the pattern is wrong and a flag is right |

## §F.5 · What this document is not

- **Not ratified. Merging it ratifies nothing.**
- **It does not run, and is not meant to.** Under §0.1 that is the stage, not a debt.
- **It changes no code, no register row, no roster and no plan.** `PLAN.md` stands paused.
- **It proposes no guard, validator, tool or dashboard.**
- **It is not a second architecture.** #353's Parts I–VI stand; this states what they rest on.
- ⚠ **It is not an argument from the existing tree.** Where it cites the chain it cites a *ruling* or
  a *derivation*, never *"this is how it is built"* — because for an idealized shape that is not a
  reason.
