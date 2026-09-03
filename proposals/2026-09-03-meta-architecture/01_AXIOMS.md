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

There are **five**.

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

⚠ **THE FIGURE USUALLY QUOTED HERE IS `22`, AND IT IS ROUTER-ERA.** `W10` deleted the regex router,
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

---

## §A.1 · What is NOT an axiom, and why the demotion matters

| stated in the chain as | actually | derived in |
|---|---|---|
| **L3** — every aggregate is a function, never a field | **a theorem of AX-4** | `T-a` |
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
> no single owner. AX-4 says every value has exactly one owner. **Therefore an aggregate is not a
> value that can be written — it can only be computed.**

**What the derivation buys that L3 does not.** L3's clause 2 (*no resolver-side Query may aggregate
per-person tallies across holders*) was added because clause 1 did not bind, and clause 3 because
clause 2 did not either. **Under AX-4 all three collapse into one question — *what owns this?* —**
and the ratchet cases fall out directly: `count{commit edges, live and ended}` has no owner, so it
is refused without needing a third clause about ended edges.

⚠ **This does not mean delete the clauses.** It means they are *checks*, not *laws*, and a fourth
evasion should be expected and answered the same way rather than by a fourth clause.

### **T-b · A threshold may change what can be chosen; it may never produce an outcome.** *(L5, first half)*
> **From AX-1.** An outcome is what a decision produces. Only persons decide. A threshold is not a
> person. **Therefore a threshold that produced an outcome would be an actor.**

**And the corpus agrees with the theorem rather than with the fear.** In the 50-arc in-chain survey,
**19** wanted a crossing to *force a moment* and then have a person choose; only **8** wanted the
crossing to act. **The design refuses the 8 and supplies the 19 exactly.**

⚠ **CARRY THE CONDITION, NOT THE LITERAL.** `PLAN.md` `W20` measures that **11** of those 19 are
reachable today — the other 8 are `faction`/`world`-scaled and unrepresentable until `W28`
re-scales them. **19 is the post-`W28` figure**, and the first draft that published it without that
condition is the error this note exists to not repeat.

### **T-c · Every clock outside the three was wound by a nameable act, and therefore has handles.** *(L5, second half)*
> **From AX-1 + AX-5.** AX-5 lists what moves by itself. AX-1 forbids a non-person actor. A quantity
> advancing outside AX-5's list, with no author, is an actor arriving through a side door.

**The consequence is the design's best single property and it is a THEOREM, not a preference:** a
wound clock can be **bribed, delayed, burned, or killed** — bribe the clerk who set the term, burn
the Record that carries it, kill the man who must renew it. **An unwound clock is unbuyable,
undelayable and unkillable, which is what a GM is.**

### **T-d · An `Event` carries no actor.**
> **From AX-2.** A field on the Event is read identically by every observer. Attribution as a field
> is therefore privileged access to who did it. **Attribution must be a per-witness `Claim`.**

**This is why covert action and false attribution are expressible without a mechanism for either.**

### **T-e · An `Event` carries no target.**
> **From AX-1.** A target field presumes delivery. Delivery without an act is transport by nobody.
> **The only transport is a person telling another person.**

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
> **From AX-1 + AX-4.** A stranger takes the seat. The seat's state changed, written by its one
> owner. The ambition-holder reads the seat and finds it filled. **No `obstruct` verb, no knowledge
> of her in the stranger's decision, no branch in the resolver.**

**This is the worked example of what "emergent" means here** — and it is a proof that the axioms
carry weight, because obstruction is a mechanic the design never implements and always has.

### **T-h · A faction is not a thing that acts; it is what people are committed to.**
> **From AX-1.** If a faction cannot act, it cannot be an actor-shaped object. What remains that can
> carry its identity across time is an utterance — a `Proposition` — plus the edges of the people
> who signed it.

**And it yields the collapse property for free:** a faction ends when people leave, with no
dissolution mechanism, because there is nothing left to be the faction.

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

⚠ **THE SECOND HALF OF THE ADMISSION TEST FAILS TODAY, AND IT IS `D21`.** `convictions`, `beliefs`
and `stance` are declared as fields and **no formula reads any of them**. Until §F2's scoring
function exists they are exactly the dead state the test is written to catch. **The schema does not
absolve the model here; it convicts it.**

## §D.2 · `Rung` — **the address, never the occupant**

> **IS.** *Where* a decision happens. A Rung owns **arrangements**; a Person makes **choices**. The
> `person` kind is the address slot and the `Person` is who stands in it — and that sentence
> generalises to all eight kinds, which is the container rule.
>
> **OWNS.** Matter (stores, its Sites, its Records, the transmission pointer), dates, envelope, stake.
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
> **OWNS.** `condition`, `drawers`, `kind`.
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

## §E.1 · `H-101` — subordination. **It cannot be stored, and that answers it.**

`H-101` is tier 0 and `absent`: *nothing can be under anything, at either institutional scale.*
Jordan asked it twice — *"do our factions have the ability to be under larger factions?"*, then
*"same applies to nesting offices"* — and the register's own note says the two have **the same
shape**, which is why it is one row: *"building two mechanisms for one relation is the §8 violation."*

### §E.1.1 The derivation, in three steps

> **STEP 1 — a subordination edge between factions has no owner, so AX-4 forbids it.**
> By **T-h** a faction is a `Proposition` plus its `commit` edges. By §D.5 a Proposition is
> **immutable and unowned** — unowned precisely *because* nothing may change it. By §D.8 a Tenure is
> owned by its **subject**. So an edge whose subject is a Proposition has no owner and no writer.
> **There is nothing that could legally hold "the Löwenritter is under the Crown."**

> **STEP 2 — what CAN be stored is already stored, and it is enough.**
> `commit : Person → Proposition` is owned by the person who made it. **A faction is under another
> exactly to the degree that the people committed to the first are also committed to the second.**
> That is a function over live edges — by **T-a**, a Query, owned by Nobody.

> **STEP 3 — the same move answers the office scale, which is why it is one row and not two.**
> An Office owns its `remit` and its scope (§D.6). **One office is under another exactly when the
> superior's remit scope reaches the subordinate's seat.** Also a function over data each office
> already owns. **One rule — *subordination is computed, never stored* — asked at two scales. The
> §8 unit is the RULE, and the rule lives once.**

### §E.1.2 What the derivation buys, and it is more than it costs

| property | why it falls out |
|---|---|
| **it is contested** | a Query over other people's commitments is exactly what no single actor controls |
| **it is reversible** | ⚠ **a Query can go DOWN. A stored counter cannot.** §22.4 clause 3 refuses a monotone count over structural edges as a ratchet — so a stored autonomy track is refused by the architecture, and the computed one is not |
| **detachment needs no verb** | people repudiate a commitment, one at a time, each paying budget. **The faction detaches because nobody is holding it, which is T-h's collapse property at one remove** |
| **nobody can read it truly** | a Query over commitments is **resolver-side**, so by **T-f** it is unreachable from `choose`. A person acts on `leaders_as_claimed`, never on the real number |
| **it needs no new `Tenure` kind** | `tenure_kinds` does not move, which §D.8's admission test requires |

### §E.1.3 *De jure* and *de facto* are both derivable, and their gap is the mechanism

**An office-holder may `utter` a Proposition of mood `HOLDS` asserting the subordination.** That is
storable — immutable, unowned, never destroyed (§D.5). **It is the *de jure* claim.** The commitment
Query is the *de facto* state.

> **AX-2 GUARANTEES THEY CAN DISAGREE, AND NOBODY HAS PRIVILEGED ACCESS TO WHICH IS REAL.** A banner
> that still flies over people who have stopped carrying it is not a modelling failure — **it is the
> only thing AX-2 permits.** By **T-b** a band on that gap may change what may be chosen and by
> whom, and may never produce an outcome. **So the gap is playable without a single new primitive.**

**This is the general result, and it is worth more than the instance:** where the chain reaches for a
*track* — a stored stage that advances — the axioms say look for **two things that can disagree, and
band their difference.** A track is a stored aggregate wearing a stage's clothes.

### §E.1.4 Alternatives, and the falsifier

| alternative | why it is refused |
|---|---|
| a new `under` Tenure kind with a stage field | the stage field **is** the stored aggregate T-a refuses, and it ratchets |
| extend `contain` to factions and offices | ⛔ **breaks the single-parent tree and R-1's subtree aggregation.** Both are lateral: a faction spans rungs freely, an Office may have `rung? = null` |
| two mechanisms, one per scale | the §8 violation `H-101` names in its own text |

> **FALSIFIER.** *Name a subordination whose de facto state is not recoverable from `commit` edges
> and remit scopes.* The candidate the chain itself supplies is an order whose chain of command is
> **parallel** rather than subordinate — reporting through its own head even while serving under
> another's. If that needs its own edge, **§E.1 is right at the faction scale and wrong at the
> office scale, and should be SPLIT rather than patched** — which would also cost `H-101` its
> one-row justification.

## §E.2 · `hold` is overloaded, and Jordan's ruling makes two of its objects disjoint

`hold : Person → Office | Rung | Record | Proposition`, one per object, glossed *"office-holding,
tenancy, custody"*. Jordan then ruled, in the chain: **governing authority and holdings are
different things** — *"they do not necessarily have all territories/provinces/duchies in their
holdings"* — and made the difference operational: *"King/Queen cannot revoke title of Duke/Duchess if
they do not have duchy is in their holdings."*

> **So `hold : Person → Rung` is carrying both meanings, and by AX-4 a value with two meanings has
> two owners' worth of writers.** Today only the coincidence that a Title is an `Office` keeps
> governing and owning apart — and §D.7.1 shows that coincidence is itself the conflation.

**This is genuinely `absent` in §G's sense — two readings, materially different games:**

| reading | what it makes expressible |
|---|---|
| **`hold` means OWNING; governing is the title** | holdings and governance are cleanly disjoint, and a title is the only route to authority |
| **`hold` means GOVERNING; owning needs its own kind** | **delegation becomes expressible** — *"Kings, Dukes, Counts and Lords can assign others of lesser rank to govern any of their holdings in their stead"*, which is how **regency and puppet rulers** arise |

⚠ **The second is the one the chain will need and does not have** — delegation is registered unbuilt
under `H-90`. But it costs a new `tenure_kind`, which §D.8's admission test resists. **That is a real
trade and it is Jordan's.**

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
| **subordination** | **not a thing at all — a Query** | §E.1, from AX-4 + T-h |

## §F.2 · Stage 2, and the two things it must not do

Jordan's ordering: **axioms/idioms/schema → hierarchies, dependencies, nests, scales → verbs,
consequences, slices, season loops.** Stage 2 takes the second, and inherits four results:

1. **Two topologies, kept apart** — a containment tree governed by R-1/R-2, and a lateral graph that
   is not. Subordination is lateral (§E.1.4).
2. **Purview is a Query over several edge kinds**, not a relation to be stored (§E.1.1 step 3).
3. **Where the chain reaches for a TRACK, look for two things that can disagree and band their
   gap** (§E.1.3). This is the general form, and the arc corpus is full of tracks.
4. **The ladder's membership is content; its ordering and its walkability are architecture** (§E.3).

> ⛔ **Do not build a second ladder.** ⛔ **Do not index code by scale** — a module is registered
> against a role and runs at whatever rungs the step hands it. Scale-indexed code is scale-divergent
> code, invisible until something composes across a boundary, and it deletes the one property that
> makes eight kinds of one type worth having.

## §F.3 · Open — and only one is Jordan's

| | who answers it |
|---|---|
| **`hold` on a Rung: governing or owning?** (§E.2) | ⚠ **Jordan.** Two defensible readings, materially different games — **delegation, regency and puppet rulers are expressible in one and not the other** |
| office subordination's **parallel** mode (§E.1.4) | falsifies or splits §E.1; answerable inside the chain |
| `judging_set_rule` (§D.2) | already `H-32` — and it also gates §D.2's own predicate |

**Everything else this document touches was closed by derivation, and each closure names its ground.**

## §F.4 · Falsifiers

| claim | what would show it wrong |
|---|---|
| **the five axioms are independent** | derive any one from the other four. **AX-5 is the candidate**: if the three-item list is itself derivable, the set is four |
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
