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
> clock.

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

**The consequence is that `T-c` and §D.4's NEVER are both quantified over MATTER, so a
CENSUS-advanced quantity evades them verbatim.** Either CENSUS's individuation is a fourth licensed
motion and `AX-5` says *four*, or it is demand-driven and therefore authored — **and nothing states
which.** The word CENSUS did not appear in the first publication of this document at all.

---

### **AX-6 · NOTHING BECOMES PERMANENT WITHOUT AN AUTHOR.**

> A state that no act can undo is a state nobody chose to make final. **Every irreversibility in the
> game was made by somebody**, and is therefore itself contestable.

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

### **ID-14 · WHAT AN ACT CAN OPEN, AN ACT MUST BE ABLE TO CLOSE.**

> Otherwise the vocabulary contains a ratchet, and `AX-6` is violated by the grammar rather than by
> any particular rule.

**Measured, and it is not an edge case: four of seven relations are open-only** (§E.1.2). A duty
cannot be discharged, a bond cannot be broken, a succession pointer cannot be changed. **The check
is one line — for every verb that writes `(Tenure, since)`, name the verb that writes `(Tenure,
until)` for the same kind** — and it is the check that would have found all four at once.

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

⚠ **THE FOUR-WAY CLAIM IS NOT EXHAUSTIVE, AND THE TEST OVER-REFUSES TWICE.** `weight` is none of the
four — a cohort headcount is not what a person can do, holds true, holds right, or is taken to be —
and it is **the field `T-l` is stated over**. `capability` is read at RESOLVE for dice and by no
decision, so the reader clause refuses it too, yet the design mandates both. **A fifth category is
needed — *what the person IS, as a quantity the world reads off them* — or the test refuses two
fields the shape requires.** Recorded rather than patched, because inventing the fifth category to
save the test is how a schema starts growing again.

⚠ **CORRECTED — THIS SECTION SHIPPED A STALE FACT, AND AN ADVERSARIAL PASS CAUGHT IT.** It read
*"`convictions`, `beliefs` and `stance` are declared and **no formula reads any of them**"*. **That
was true of `#353` and false at HEAD:** `W5` landed the scoring function, `score()` sums
`convictions × alignment` inside `choose`, `stance_toward` reads `stance`, and the register row this
was cited to — `H-03` — is marked **DISCHARGED**. Two of the three are consumed.

**What survives is narrower and sharper. `beliefs` IS dead**, and worse than the original claim:
the only function in the chain whose *name* points at it reads the **claim ledger** instead — so the
one place a later reader would go to check the `AX-3` boundary is a name pointing at the wrong
layer. **That is the admission test earning its place**, and it is one field, not three.

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
| a **faction** | a `Proposition` plus its `commit` edges (T-h) |
| an **address** | a `contain` Tenure |
| a **need** | a `Sensation` plus a Query |
| **annexation** | a `hold` at distance — **not a verb** |
| **secession** | the `commit` edges moving — **not a verb** |
| every **aggregate** | a Query, owned by Nobody (T-a) |

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

### §E.1.2 ⚠ **AND THE REPLACEMENT INHERITS A RATCHET, WHICH IS THE REAL FINDING**

**`oblige` opens a Tenure and NO VERB CLOSES IT.** `repudiate` reads *"a live **`commit`** exists"* —
it ends a commitment, never a duty. **Swear once and you are bound forever.**

**Measured over the whole vocabulary, because one instance is an anecdote:**

| tenure kind | opened by | closed by |
|---|---|---|
| `hold` | `confer` | `confer`, `revoke` |
| `contain` | `move` | `move` |
| `commit` | `commit`, `confer` | `confer`, `repudiate` |
| **`oblige`** | `oblige` | ⛔ **NOTHING** |
| **`succeed`** | `succeed` | ⛔ **NOTHING** |
| **`tie`** | `tie / knot` | ⛔ **NOTHING** |
| **`knot`** | `tie / knot` | ⛔ **NOTHING** |

> ### **FOUR OF SEVEN RELATIONS CAN BE OPENED AND NEVER CLOSED.**
> **You cannot discharge a duty, break a bond, or change a succession pointer.** §D.8 says
> *"`until?` is what makes an ended relation a fact"* — the design gives every Tenure that field and
> then supplies no verb to write it for four of the seven kinds.

**This is `T-c`'s shape one step over.** `T-c` forbids a quantity that advances with no author. Here
the state does not advance — **it becomes permanent** with no author, and no act can unwind it. A
bond nobody can break is exactly as unbuyable, undelayable and unkillable as a clock nobody wound.

⚠ **AND IT IS WHY THE FIRST ANSWER LOOKED RIGHT.** Facing an irreversible edge, "make it a Query" is
the reachable repair — a Query can go down. **The reversibility was real and the diagnosis was
wrong:** the defect is not that the relation is stored, it is that the vocabulary has no verb to end
it.

### §E.1.3 The repair, and it is a data edit rather than a mechanism

**`(Tenure, until)` is already a write-matrix row.** `repudiate` already writes it. What scopes it to
`commit` is **one phrase in one `requires:` cell.** Widen the domain and four ratchets close at once.

> **Nothing new is built. No `tenure_kind` moves. No carrier is added.** The seat of the defect is a
> precondition string, and that is the whole of it.

⚠ **What is NOT a data edit, and must be ruled rather than assumed: what ending each one COSTS.**
Forswearing a duty, cutting a knot and breaking a succession are three different acts with three
different prices, and pricing them is design work. **The register carries `H-100` — *what a
revocation costs* — for exactly this, and this finding widens it from titles to four relations.**

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

### §E.1.5 The office scale — **SPLIT, by this section's own falsifier**

The withdrawn version claimed one relation answers both scales. **Its own falsifier fires.** Office
subordination under it is a function of the superior's remit scope and the subordinate's seat;
`Office.remit` is written only by `establish`, and **`(Office, rung)` has no write-matrix row at
all**, so the seat cannot move. **De facto office subordination could then change only by the
superior's own act — requiring an institution to voluntarily record its own involuntary loss**,
which is the one thing a detachment never is.

**So the honest disposition is the one the falsifier prescribes: SPLIT.** Faction subordination is an
`oblige` edge between persons. Office subordination is not yet derived, and **`H-101` loses its
one-row justification** — which is a cost, stated rather than absorbed.

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
| **`Office.conferral` is unspecified** — the basis per office | ⚠ **new, and created by the ruling.** §E.2.5: delegation needs no mechanism, it needs this field to carry *named / elected / inherited*. Answerable in the chain |
| **What ending each relation COSTS** (§E.1.3) | ⚠ **new.** Closing the four ratchets is a data edit; **pricing** forswearing a duty, cutting a knot and breaking a succession is design work. Widens `H-100` from titles to four relations |
| **Is CENSUS's individuation a FOURTH licensed motion?** (`AX-5`) | ⚠ **new.** Either `AX-5` says four, or individuation is authored. Nothing states which |
| **Office subordination** — `H-101` is now SPLIT (§E.1.5) | the faction half is derived; the office half is not, and `H-101` loses its one-row justification |
| **sovereign power has no representation** (`H-90`) | it is §E.2.4's own falsifier — *"uncontested and absolute"* may be exactly what cannot be conferred. **Jordan's, if the falsifier fires** |
| office subordination's **parallel** mode (§E.1.4) | falsifies or splits §E.1; answerable inside the chain |
| `judging_set_rule` (§D.2) | already `H-32` — and it now gates more than it did: **an election is a sitting**, so §E.2.5's third shape runs through it |

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

## §F.5 · What this document is not

- **Not ratified. Merging it ratifies nothing.**
- **It does not run, and is not meant to.** Under §0.1 that is the stage, not a debt.
- **It changes no code, no register row, no roster and no plan.** `PLAN.md` stands paused.
- **It proposes no guard, validator, tool or dashboard.**
- **It is not a second architecture.** #353's Parts I–VI stand; this states what they rest on.
- ⚠ **It is not an argument from the existing tree.** Where it cites the chain it cites a *ruling* or
  a *derivation*, never *"this is how it is built"* — because for an idealized shape that is not a
  reason.
