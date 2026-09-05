# `03-design-v2.md` evaluated against the meta-architecture

## Status: **EVALUATION. PROPOSED. NOTHING RATIFIES ON MERGE.**
## Subjects: **#358** `architecture/meta/` (12 files) · **#359**
## `proposals/2026-09-03-governance-corpus-rebuild/03-design-v2.md`
## Question, Jordan-directed 2026-09-03: *to what extent can v2 improve on #358 for
## meta-architecture and code shape?*

---

# THE VERDICT, FIRST

> **v2 is admissible to #358 as a FALSIFIER, not as a source — and used that way it is worth a great
> deal in two places and a line each in about eleven more.** Of twenty-six candidate contributions at
> or above the domain level: **two fill holes #358 names in itself and cannot close from its own
> axioms**; **eleven transfer as an idiom, a test or a corpse**; **seven corroborate a result #358
> derived from disjoint sources**; **nine are structural proposals that collide with #358, of which
> #358 wins eight outright and one SPLITS**; the remainder is domain content #358 pre-emptively rules
> out of architecture.

⚠ **THIS VERDICT WAS ATTACKED BY AN INDEPENDENT READ-ONLY CRITIC AND SURVIVED ONLY AFTER REVISION.**
Its charter was `G.4.3`'s two questions — *did the producer invent?* and *did the producer refuse what
the design permits?* — and the result is lopsided in the way `G.4.3` predicts: **the invention rate was
low and the OVER-REFUSAL rate was high.** Six findings changed this document, one of them reversing a
whole collision, one adding a thirteenth improvement, and one catching an evidence sentence that was a
term-grep standing in for a concept. **Every change is marked in place rather than overwritten**, and
one critic ruling was itself refused, on `AX-3`, at §4.8. The pre-critique draft would have been
confident and wrong in four places.

**The two that matter:**

| | what v2 supplies | the hole in #358 |
|---|---|---|
| **1** | **Every feedback loop is named and signed** (`TL-7`) — and a design with only negative loops **converges** | #358's entire vocabulary for feedback sign is **two lines, both admissions of absence**: `07_DYNAMICS.md:89` (*"nothing bounds a spiral … no stage pretends otherwise"*) and `04_CODE_ARCHITECTURE.md:628` (`F.28`, *"nothing bounds a spiral, and nothing here pretends to"*). Zero occurrences of `amplif*`, `damping`, `positive feedback`, `snowball` |
| **2** | **The engine owes an explanation** (`TL-13`) — no referee means the engine inherits the referee's *second* job | `preview`, `explanation`, `inspectable` occur **zero times** across all twelve files of #358. It has `causes[]` as *"the narrative layer"* and never asks whether the **player** can see the chain |

**And the one sentence that decides how to read the rest:** v2 is a **domain design** and #358 is a
**meta-architecture**. Where v2 proposes a *shape* it is competing with #358 on #358's own ground and
losing, because #358's shapes are derived and v2's are taken from precedent. Where v2 proposes a
*discipline* — a test, a sign, an obligation, a corpse — it is operating at #358's altitude and
frequently arriving with something #358 does not have.

---

# §1 · THE ADMISSIBILITY QUESTION, WHICH GATES EVERYTHING BELOW

This has to be settled before any content transfers, because both documents carry a scope rule and
the two rules do not compose.

| | #358 | #359 |
|---|---|---|
| **admissible sources** | *"the axioms themselves and the PR chain #337 → #357"* — `canon/`, `systems/`, `research/`, `engine/` are **not authority** | a **33-document zip uploaded to a session**. *"No repository file was read as a source"* |
| **relation to `main`** | derived with the tree **closed**; a whole PART E was **withdrawn in full** for breaking that rule | **unverified.** Overlapping filenames are *"not verified to be identical and no comparison was performed"* |
| **numbers** | three carry provenance conditions rather than literals | *"unvalidated"*, by its own closing section |

**So v2 is neither the tree nor the chain. It is a third thing**, and the honest reading is narrow:

> ### **v2 IS NOT AN ADMISSIBLE SOURCE FOR #358'S DERIVATION, AND IT IS THE BEST AVAILABLE TEST OF IT.**
> #358's `G.4.6` prescribes two artifacts: the derivation with the tree closed, then **the
> comparison**, in which prior work is *"read between the two, as evidence at its own strength."* v2
> belongs in the second artifact. Its own strength as evidence is low — unverified against `main`,
> self-declared unvalidated numbers, and a central critique measured as a lexical count over a
> document that is not in this repository — **but its independence is total**, which is exactly the
> property #358's `PART F.4` falsifier table is asking for and cannot generate from inside itself.

⚠ **The failure mode to refuse by name.** Reading v2 as a source imports a rooted liege tree, a
`Title` entity, an `Echo` carrier, stored interest-group approval and a five-clock influence graph —
**five things #358 derives its way out of.** ⚠ *(An earlier draft of this paragraph added "one of them
by withdrawing a Part". That is unsupported: #358's PART E was withdrawn for being built on a
repository sweep, and what its withdrawn draft contained is not recoverable from the published text.
Corrected in place rather than overwritten, per `G.3.2`.)* That is `G.4.6`'s
hazard exactly: *deferring to what exists instead of deriving from what is true*, with an uploaded
corpus standing in for the tree. The corpus is not the tree, but it is **enumerable**, which is the
property that makes the hazard fire.

---

# §2 · WHAT TRANSFERS — thirteen, ranked by what each is worth

## §2.1 · **`TL-7` — every loop is named and signed.** The largest, and it closes a self-named hole

v2's measurement of its own predecessor: **≈245 damping devices** (`clamp` 92, `cap` 95, `floor` 43,
`saturating` 6, `ceiling` 4, `bounded` 3, `mean-revert` 2) against **zero** amplifying ones, with
`runaway` appearing twice and both times to say runaway is prevented. Its conclusion is the
transferable part: **a system in which every quantity is bounded and every loop is negative
converges** — season 40 resembles season 30 — *"and that is not stability; it is inertia."*

**Why #358 needs this and cannot reach it.** #358 is, by construction, a design of refusals. `T-a`
refuses the stored aggregate, `AX-6` and `ID-14` refuse the ratchet, `T-b` refuses the deciding
threshold, `ID-5` refuses the silent default. **Every one is a damping device.**

⚠ **CORRECTED — the first draft's evidence sentence was a term-grep standing in for the concept, and
an independent critic broke it.** It read *"#358 has no term in its vocabulary for the other sign"*,
which is **false**. #358 reasons about feedback sign constantly, under its own word — **ratchet**:
*"any Query monotone in the ENDED-edge set is a ratchet and is refused"* (`01_AXIOMS.md:181`); `AX-6`,
whose denial-cost is *"counters that only climb"* (`:172-193`); `ID-14`; and *"the banned ratchet"* at
`09_WORKED_EXAMPLES.md:82`. **Searching for `amplif*` and finding zero is the failure this whole
comparison is grading v2's predecessor for**, committed by the author of the grade.

> **The claim that survives is narrower and is still the largest transfer.** #358 has a
> **monotonicity doctrine**, which refuses a ratchet built out of structural edges **within** the
> model's ownership rules. It has **no cross-season loop bound**, and no way to say that a design of
> nothing but refusals converges. **It names that hole twice and closes it nowhere.** A
> meta-architecture that can say every way a quantity may be written, and cannot say which way a loop
> points across seasons, is missing an axis rather than a rule.

⚠ **What does NOT transfer, and the distinction matters.** `R-1`/`R-2`/`R-3` are governance content
for a model #358 does not share, and `Π_world`'s terms are made of objects #358 refuses. **What
transfers is the discipline and the diagnosis, which is an idiom, not a mechanism** — and under
#358's own `G.4.1` an idiom without a representation is *"work the stage has handed forward without
saying so."* So the honest form of the transfer is:

> **ID-16 (proposed) · A DESIGN MUST BE ABLE TO NAME EVERY LOOP IN IT AND SAY WHICH WAY IT POINTS.**
> The representation is a signed list; the falsifier is v2's own measurement, run as a command —
> count the damping terms, count the amplifying terms, and a zero in the second column is the
> finding. **A design that cannot list its loops cannot tune them, and one with only negative loops
> cannot surprise anyone.**

## §2.2 · **`TL-13` — the engine owes an explanation.** Second largest, and it is a consequence of repo canon that #358 never draws

`CLAUDE.md` opens with *"There is no GM — the engine resolves everything."* #358 treats that as a
**constraint on authoring** — every rule must be evaluable, nothing may be adjudicated. v2 points out
that it is also an **obligation**: the referee's other job was answering *why did that happen*, and
removing the referee does not remove the question.

**This is compatible with `AX-2` only once a distinction neither document states is made — and the
obvious form of that distinction is wrong, so it has to be stated carefully.**

⚠ **The tempting split is *the person in the fiction* against *the player at the console*, on the
ground that the player is not an actor and `AX-2` does not quantify over them. That will not hold
here, because the player CONTROLS a person** — v2's own tick has *"every polity and PC declares"* —
so anything shown to the player is available to a character bound by `AX-2`. **A split on WHO is
looking breaches the axiom immediately.**

> ### **THE SPLIT THAT SURVIVES IS ON WHAT IS SHOWN, NOT ON WHO IS LOOKING.**
>
> | | |
> |---|---|
> | **WHAT the person holds** | `AX-2` governs it absolutely. Their `View` is `ClaimId[]`; nothing is added, and no Query they cannot reach becomes visible |
> | **WHY what they hold says what it says** | ⛔ **not information about the world.** It is the derivation of a value the character already has, and showing it adds no world-truth |

⚠ **A critic proposed softening this, and the softening is DECLINED with its reason recorded.** The
argument was that `AX-2` is already scoped *"inside a decision"* (`01_AXIOMS.md:103`) and enforced by
`T-f`'s parameter list, so a preview sits outside its reach and the import is cheap. **That holds for
an NPC and fails for the player.** `choose` is the NPC decision procedure; **for a player character
the player IS the decision procedure**, so a preview shown before they declare is shown *inside a
decision* in the only sense `AX-2` cares about. The scoping does not make this cheap — **it makes the
preview precisely the hard case**, because a preview is by definition what you look at before
deciding.

**So the obligation is narrow and it is real: the engine owes the ARITHMETIC of everything it has
already shown, and nothing else.** v2's bound states it exactly — **hidden actors are hidden in their
EXISTENCE, never in their ARITHMETIC.** *"Order −1 from an unknown source"* is admissible because the
character can already see the −1; what they are additionally given is that it has a cause they cannot
name, which is what makes investigation worth a scene. **A preview that revealed the source would be
a breach; one that says the effect is unattributed is not.**

⚠ **And the promise must shrink where #358's loop is stronger than v2's tick.** v2 offers *"the full
consequence chain of that action under the current snapshot."* Under #358, `DELIBERATE` is a
simultaneous pure map and `RESOLVE` is an ordered fold whose order is `(stratum, actor-hash,
intra-person position)` — so no preview can know which acts fold first. **The honest form is: the
chain against the FROZEN world, never against the folded one**, and the gap between the two is the
strategic uncertainty. v2 concedes exactly this for other agents' declarations; under #358 the
concession is larger and is structural rather than a design choice.

## §2.3 · **`F.24`'s missing grammar gets a worked instance** — and `F.24` is one of two gaps #358 says block the build

#358: *"every verb's `requires` is a **prose string**, so evaluating it needs a body per verb, and
`the resolver has no body` returns as **the resolver has thirty**."* Its assumption is *"a small typed
predicate grammar"*, and it supplies none.

v2's `basis → prosecutable_by` matrix is one:

```
                war  vote  appointment  marriage  purchase  uprising
blood            ●    ●                    ●
conquest         ●
charter               ●        ●                     ●
office                ●        ●
recognition      ●    ●        ●          ●          ●
fabrication      ●                                              ●
```

**Six bespoke eligibility rules collapse into a 6×6 table keyed on two enums.**

⚠ **CORRECTED — the first draft cited the weaker of v2's two artifacts.** An enum→enum eligibility
table has **no operands and no world-state predicates**, and #358 already has that shape as loader
invariant 3 (`04_CODE_ARCHITECTURE.md:345`). **The matrix demonstrates only *a table, not a
sentence*** — real, but not `F.24`'s grammar.

> **v2's actual near-instance of the grammar is one page later:** `∃ inst : presence(inst) ≥ 2 ∧
> hostile(inst, holder)` (`03-design-v2.md:1098`) — **a quantifier, a comparison and a relation, and
> nothing else.** That is the shape `F.24` is asking for, in three terms, and it is what a `requires`
> column would have to hold to stop being prose.

**Both matter, for different reasons.** The matrix says the *eligibility basis* is data — and under
#358 the slot is already named: `Seat.conferral`, *"the basis, per office"*, which §E.2.5 says *"has
been on the Office since #353 carrying nothing."* The predicate says the *precondition* is a typed
expression rather than a body. **`F.24` needs the second; `conferral` needs the first.**

## §2.4 · **`granted_by` supplies a reader for `Tenure.conferrer`, which is #358's own `ID-13` defect inside #358's own type**

`conferrer? : SeatId` occurs **exactly once in all twelve files of #358** — `04_CODE_ARCHITECTURE.md:257`,
in the `Tenure` type declaration — and is read nowhere. By `ID-13` (*a declared field must reach a
reader, or it is not declared*) that is **not a weak mechanism; it is a mechanism that does not
exist**, wearing a schema's clothes. #358 flags `Tenure.degree` for exactly this (`F.4`) and misses
the field one line above it.

⚠ **And #358 caught the identical defect ONE FIELD TO THE LEFT.** `degree?` sits on the **same line**
and **is** in the hole register — `F.4`, *"a field with a writer and no reader … which under `ID-13` is
a field that does not exist"* (`04_CODE_ARCHITECTURE.md:604`). `conferrer?` is in neither `PART F` nor
`§F.32`'s not-a-gap list. **The register works; it was not run across the line it was written on.**

**v2 supplies the reader, and it is a good one.** `granted_by` makes patronage a graph — *who raised
whom* — and gives defection a shape: **when a patron falls their clients are exposed; when a patron
defects, the question is which clients follow.**

⚠ **The obvious fix is wrong, and this is the correction a critic supplied.** #358's field is
`conferrer? : SeatId`; v2's `granted_by` is a `CharacterId`, and patronage cascades are
**person→person**. **Hanging a person-relation off a seat pointer is what `§E.2.2` forbids** —
authority belongs to the seat, patronage does not. So the reader belongs on the **lateral web**
(`07_DYNAMICS.md:35`) as an `oblige` edge between the raiser and the raised, and `Tenure.conferrer`
either finds a *seat*-shaped reader or, under `ID-13`, is deleted. **`ID-13` admits no third state,
and "supply a reader" is not a licence to supply the wrong one.**

## §2.5 · **`TL-5`'s test scans the CONTENT layer, and #358's scans do not**

#358 has the rule three times over — `ID-4` (*declare, don't route*), Stage 2 `§C.2` (*branch on the
ordinal or the relation, never on the member*), `G.2.2`. Its enforcement is `D-27` (a scan of `loop/`,
`seam/`, `decision/` for roster literals) and `D-28` (re-run the seeded season with `rung_kinds`
permuted). **Both scan CODE.**

v2's finding is that the code-level claim can be **true while the content-level claim is false** — its
predecessor claimed *"no subsystem names another"*, which held of its code and failed on its own
exemplar card carrying `settlement.has_subnational(RM)` and a directive generator mapping
`Counter-threat → Suppress(RM|Church)`. Its test is one line: **grep the content layer for proper
nouns; every hit is a scenario declaration or a defect, and there is no third case.**

⚠ **This binds HARDER under #358 than under v2, which is the part worth carrying.** v2 manufactures
factions at runtime through a promotion pipeline. **Under #358 a faction is any uttered `Proposition`
plus its `commit` edges** — so every faction that will ever exist is manufactured at runtime, and a
rule naming one is a promise the ontology cannot keep for any of them.

## §2.6 · **`TL-6` — a suspension must itself be uniform.** A missing idiom, with its own corpse

v2: *"Where a limit is suspended, the suspension is itself a uniform rule attached to a named regime
— never an exception carved for one entity."* Its corpse is its own draft (`V-2`), which raised a cap
from ±5 to ±8 for one faction **and admitted in its own margin that this broke its uniformity rule**.
The repair generalises the suspension instead of exempting the entity: *an armed regime raises the cap
on its own driving track by 60% for its duration*, so ±8 **falls out** rather than being asserted.

⚠ **SOFTENED — the first draft searched the idiom list rather than #358.** *"No idiom covers
exception-carving"* is true of `ID-1`..`ID-15` and **false of #358**, which carries the prohibition in
three places: *"a mechanism that special-cases a kind is wrong for every membership … if you find
yourself writing `if kind == 'duchy'`, that is scripting drift"* (`01_AXIOMS.md:1135`), Stage 2
`§C.2`, and `G.1.6`.

> **What #358 has nowhere is `TL-6`'s POSITIVE half — the licensed FORM of a suspension.** #358 says
> *do not carve an exception*; it never says **what a lawful exception looks like**, so a session that
> genuinely needs one has no shape to reach for and will carve. **v2 supplies the form:** *an armed
> regime raises the cap on its own driving track by 60% for its duration — one rule, identical for
> every regime, present and future.* A prohibition with no licensed alternative is a rule that gets
> broken quietly; **that asymmetry is the transfer**, and it is smaller and more defensible than what
> the first draft claimed.

## §2.7 · **v2's corpses for `§E.2.2` are of a kind #358's are not — a player would notice them**

⚠ **CORRECTED — the first draft said `§E.2.2` *"has an argument and no corpse"*, and that is
checkably false.** #358 carries at least four: the missing conferral path it quotes its own handoff
calling *"the clearest single piece of evidence that the entity model is wrong"* (`01_AXIOMS.md:687`);
*"delegation is unbuildable under that model by construction"* (`:1012`); the false regency menu,
**explicitly filed in `G.3.2`'s corpse table** (`04_CODE_ARCHITECTURE.md:803`); and *"a Query that
reads the actor's own title-holds gives the wrong answer for every delegate"* (`:1061`).

> ### **THE DISTINCTION THAT SURVIVES, AND IT IS THE ACTUAL CONTRIBUTION**
> **All four of #358's corpses are TREE DEFECTS — things the repository failed to build, found by
> reading the repository.** v2's two are **IN-FICTION ABSURDITIES**, found by tracing what the rule
> does when it runs. `G.1.2` prefers a corpse to an argument; **this says a corpse a player would
> notice beats one only a maintainer would**, because it survives a reader who has never seen the
> tree.

v2's two, both behavioural:

1. **`Provincial Authority = controller(province.seat)`**, issuing a directive to *every* settlement
   in the province — so in a fractured province **the seat-holder commands a rival's governor**, who
   accrues suspicion toward and is recalled by a faction they do not serve.
2. **`Accord(p) = 0 → holder := ∅ for every member`**, computed over all members — so **one faction's
   two ruined settlements strip a rival's well-governed one.**

> **Both are the same mistake — treating the geographic container as the chain of command — and both
> disappear the moment authority is asked of the seat rather than of the place.** That is #358's
> `§E.2.4` (*purview must be asked of the SEAT being exercised, not of the actor*) and Stage 2
> `§A.1`'s containment/subordination split, arriving as two bugs instead of as a derivation.

## §2.8 · **`G.4.3`'s critic charter is missing a third direction**

#358 names two: *did the producer invent?* and *did the producer refuse what the design permits?* —
the second with a corpse (a pooled resource refused wholesale, surviving four adversarial passes
because every critic checked for inventions and none for over-refusals).

v2 supplies a third, and it is distinct from both: **the self-audit recorded a defect as a virtue.**
Its mean-reversion loop — under which *a settlement governed above its realm's average loses Popular
Support every season until it sinks back* — was listed among *"the negative loops that are correct"*.
Neither *invented* nor *over-refused*: **misclassified in sign, by the author, inside the section
built to catch exactly that.**

⚠ **CITE THE AUDIT, NOT THE LOOP TABLE.** v2's live loop table (`03-design-v2.md:868-877`) does **not**
list mean-reversion, because `:879` heads the correction — *"the one negative loop that was signed
wrong"*. **That is post-correction text and a reader checking it will overturn the finding.** The
evidence is v2's own audit: *"**The self-audit recorded this loop as a virtue**"* (`:1463`) and *"the
self-audit listed this in the *negative loops that are correct* table"* (`:1476`). A critic nearly
overturned this on the wrong citation, which is `ID-11` in miniature — **the claim was true and its
pointer was not.**

## §2.9 · **The method result, which is a real constraint on `G.4.1`**

> **"Principles catch contradiction; only tracing the mechanics catches error. A design that is
> internally consistent and does the wrong thing passes every test it can write about itself."**

v2's evidence is the split between its two passes: the self-audit's seven findings are **all local
inconsistencies between two passages** (a proper noun, an un-uniform suspension, an incomplete list,
an untagged field, a double home, a skipped claim, a resolution outside the ladder) — every one
findable by turning a statement into a grep. The independent critic's nine include **three
behavioural bugs**, and every one of those reads perfectly as text.

**#358 already owns the answer and does not connect it to its audit method.** `§0.2` — *done means it
runs* — build step 8 (*one NPC's season runs end to end from Q1–Q4 with zero authored acts*), and
`G.4.7` (`04_CODE_ARCHITECTURE.md:909`, *"a session closes on the artifact the milestone names"*) are
the trace v2 says is required. ⚠ **But `G.4.7` binds MILESTONES and `G.4.1` binds STAGE BOUNDARIES,
and only the second is the gate under discussion** — so the connection is genuinely missing rather
than merely unstated. What `G.4.1` says is that a stage closes **on representations**; what
v2 adds is that **a representation can be internally consistent and behaviourally wrong, and the
falsifier for a design claim is therefore a trace, not a grep.**

## §2.10 · **`TL-1`'s field tag is an admission dimension orthogonal to `IS · OWNS · ADMITS · NEVER`**

v2 requires every territorial field to carry `dejure | defacto | civic`, and states that **an
untaggable field is mis-modelled.** Applied (`V-4`) it fired twice: the vacuum and stabilisation
windows moved off the province onto the title as `contested_since`/`held_since` (*"they are timers
about a de facto transition, and they were sitting on the province as though they were facts about
the land"*), and `L`/`PS` gained a qualifier that turned out to be content (*acceptance is a property
of a place **under someone**, which is why conquest does not inherit it*).

**#358's admission tests ask who owns a field and who reads it. They do not ask what KIND of assertion
it is** — and the two questions are independent. A demonstrated hit rate of two on a table of about
thirty is worth the line it costs.

## §2.11 · **`TL-9`'s falsifier is a positive observable, where #358's is structural absence**

#358's simultaneity is stronger: *no token exists in `DELIBERATE`'s scope, and the gate cannot be
called without one* — **STRUCTURAL**. But its check is that a defect **cannot be written**, which by
`ID-10` is a check that never observes anything.

⚠ **CORRECTED — v2's observable does not transfer as written, and a critic caught it.** *Mutual
destruction must be reachable* belongs to **snapshot-then-apply**. #358's `RESOLVE` is an **ordered
fold** — *"each act sees the world its predecessors left"* — so mutual destruction is unreachable
there **by construction**, and #358 names the price rather than hiding it (`F.26`: *"a hash decides
who eats when two people reach one larder, and the design has no better answer, which should be said
aloud rather than discovered"*). **Importing the observable would fail against a correct
implementation**, which is the worst kind of test.

> **The transferable form, restated onto the claim #358 actually makes.** #358's order-independence
> lives on `DELIBERATE` — *"a pure map, parallel, order-independent"* — and **has no observable at
> all**: `D-28` permutes the **roster**, not the act set. **So the falsifier is
> permutation-invariance of the SCENE SET: shuffle the order in which persons are deliberated and
> the resulting `Scene[]` and the season hash must be identical.** That is cheap, it can see the
> failure it excludes, and it is aimed at the one #358 property that is asserted rather than
> observed.

## §2.12 · **The procedural / graph criterion**

v2: *"A procedure is required wherever the ORDER of sub-steps changes the outcome"* — sieges,
successions, votes stay procedures; everything that is a rate or an equilibrium is an edge.

#358 has both forms — the ordered fold where order is the mechanism, and the pure map where it is
not — and **never states the criterion that decides which a thing is.** The rule is small, it is
correct under #358, and it is the kind of sentence `G.2.2`'s level/axis test is made of.

⚠ **AND IT SITS TWELVE LINES INSIDE THE SECTION §4.5 DISMISSED**, which is how the first draft came to
bank a rule and refuse its neighbourhood in one document. **See §4.5, which now splits.**

## §2.13 · **`TL-12` — the ratchets are ENUMERATED.** Added after the critique; the first draft filed this as a #358 win and was wrong

**The first draft ranked this a collision — *#358 makes the ratchet unspellable, which beats
enumerating it* — and that is true of exactly one class of ratchet and false of the rest.**

`ID-14` plus loader invariant 6 (*`release`'s kind domain **equals** `tenure_kinds`*) makes
open-without-close unspellable **for Tenures**. #358 has no register for any other authored
permanence, and the evidence that it needs one is #358's own:

| the permanence | #358's own words | enumerated anywhere? |
|---|---|---|
| four of seven relation kinds open-only | *"a duty cannot be discharged, a bond cannot be broken, a succession pointer cannot be changed"* (`01_AXIOMS.md:1172`) | ⛔ **found by an adversarial pass, not by a list** |
| `Proposition` immutability | *"no setter and no delete"* (`05_ONTOLOGY.md:108`) — and its consequence is named a **live defect**: *"a memberless faction leaves territory held by a banner nobody carries"* (`01_AXIOMS.md:641`) | ⛔ **never listed as an authored irreversibility** |
| ended Tenures never deleted | *"NEVER: deletion"* (`04_CODE_ARCHITECTURE.md:258`) — deliberate, and the source of the ratchet hazard `T-a` then has to patch | ⛔ |
| the log, append-only | `state/log` *"itself, append-only"* | ⛔ |

> **`AX-6` says every irreversibility was made by somebody. `TL-12` asks for the LIST OF THEM, and
> #358 does not have one** — which is why it discovered four ratchets in its own vocabulary by
> adversarial pass rather than by reading a register. **An axiom quantifying over irreversibilities
> and no enumeration of them is `ID-13` at the level of the axiom set.**

---

# §3 · WHAT CORROBORATES — seven, and independence is what makes them worth banking

**These are not improvements and must not be filed as such.** They are the same result reached twice
from disjoint sources, which under `G.4.3` is the most bankable signature available and is worth more
than either derivation alone.

| | #358, derived | v2, from precedent and corpus |
|---|---|---|
| **authority is not the container** ⚠ **PARTIAL** | `§E.2.2` *authority is a property of the seat being exercised* + Stage 2 `§A.1`'s three shapes (containment tree · subordination graph · rank ordering) called by one word | *"authority runs along the liege chain of the holder, never along the container"* — reached by tracing a bug. ⚠ **v2 reaches only the NEGATIVE half.** Its positive half — the chain of *the holder's own title* — is what #358 files as **the special case** *"where the seat being exercised is the actor's own title"* (`01_AXIOMS.md:1031`), i.e. the case that excludes every delegate. **Bank as convergence on the refusal, not as arrival at `§E.2.2`** |
| **one owner per quantity** | `AX-4`, and the four-value taxonomy `field · edge · Query · barrier cache` | `TL-2`, with the sharper diagnosis of how the slogan rots: *"one writable tier" is a stronger, wrong version of a correct rule* |
| **one outcome type** | `T-k` + Stage 3 `§E.3` — one ladder, a subsystem returns a **margin**, a veto may only demote | `TL-3` — every consequence table keyed by `Degree` and nothing else; the generator private to its scale |
| **roles, never identities** | `ID-4` · Stage 2 `§C.2` · `G.2.2` | `TL-5` |
| **capability, never kind** | `ID-7` + `§D.3`'s `Site` gating verbs **by band** — *"damage removes an option rather than adding difficulty"* | `TL-10` + `Holding.confers : [Capability]` |
| **de jure / de facto** | `§E.1.4` — *the sworn edge* against *the commitment overlap*, and the general form: **where the design reaches for a TRACK, find two things that can disagree and band their gap** (`G.1.5`) | `TL-1`, restricted to territory |
| **a settlement's holdings differentiate it** | `§D.3` `Site`, with a `NEVER` v2 does not have: **never node-keyed**, because a settlement holding a silted harbour at `0.1` and a healthy seam at `0.9` collapses to `~0.5` and gives **two wrong answers at once** | v2's `Holding`, without that refusal |

## §3.1 · The best of them — **v2's claim-on-a-title is the third instance of a pattern #358 predicted and asked for**

#358 `§E.1.6`, having found the shape twice:

> **"Subordination and war are the same shape: an uttered Proposition · an owned edge · a gap between
> the sworn and the actual. EXPECT A THIRD. When the design next reaches for a relation between two
> things that cannot act, this is the shape to reach for first."**

v2, with no knowledge of that sentence, built its central object as an assertion of right by a
claimant over a title, prosecuted by one of several routes, persisting after the thing claimed is
lost.

⚠ **DOWNGRADED FROM *INSTANCE* TO *CANDIDATE* AFTER CRITIQUE, and the downgrade is right.** `§E.1.6`
scopes the pattern to *"a relation between two things that cannot act"* — and v2's `claimant` admits
`CharacterId`, **who can act**. (It also admits `PolityId`, who cannot, so half of v2's claimants fit
and half do not.) v2 also supplies **neither** an uttered Proposition **nor** a gap Query; it supplies
the object those would decompose into. **So this is a candidate third instance, not a confirmed one.**

> **The decomposition below survives the downgrade intact, and it is the substance.** Whether or not
> the label *third instance* is earned, the exercise is the same and so is its result: **decompose v2's
> central object by #358's question 1 and see what #358's axioms do with each field.**

| v2's `Claim` field | in #358 |
|---|---|
| `subject : TitleId` + `claimant` | the **uttered `Proposition`** — *"X is rightfully mine"*, immutable, with an author who can be named |
| the assertion itself | the **owned edge** — a `commit`, owned by the claimant |
| `expires : season \| never` | **`Tenure.term`** — `T-n`, the opening act declares the terms |
| `strength : Clamped<0,5>` | ⚠ **refused as a field by `T-a`** — it is a value over many owners. It is the **commitment share**, a Query, and the better object |
| `secrecy : public \| private` | ⚠ **needs no field.** Under `AX-2` a claim nobody witnessed is simply unknown; secrecy is the **empty observer set**, which is `T-d`'s covert-action result |
| `basis → prosecutable_by` | **`Seat.conferral`** — *"which act fills the seat"* (`§E.2.5`) |
| the de jure / de facto gap | the **Query** that bands the gap, `T-b` |

⚠ **And v2's best `Scheme` property falls out of #358 emergently rather than as a field.** v2 gives a
scheme `secrecy : Clamped<0,5>` that **decays as progress rises** — *"the closer a plot is to firing,
the more people know"* — so the window in which a scheme is both dangerous and invisible closes on its
own. **Under #358 that is not a decaying counter; it is arithmetic.** Progressing a scheme costs acts,
acts happen at venues, and WITNESS computes the observer set of each. **More progress means more acts
means more witnesses**, with no `secrecy` field, no decay rate and no tuning — and `ID-5`'s polarity
holds, because zero acts means zero observers rather than a default. **v2 authored a curve; #358's
mechanism produces it.**

> ### **THIS IS THE STRONGEST SINGLE RESULT OF THE COMPARISON, AND IT RUNS IN #358'S FAVOUR.**
> A design built from a disjoint corpus, by precedent, in a domain #358 never examined, produced an
> object that **derives cleanly in #358's shape** — and in the two places it does not derive, #358's
> axioms **refuse the field and hand back a better mechanism**. That is the axiom set doing the work
> an axiom set is for, tested against material it could not have been fitted to.

---

# §4 · WHERE THEY COLLIDE — nine: #358 wins eight, and one SPLITS

**Ranked by how much damage importing v2's version would do.**

## §4.1 · `Echo` — a magnitude that travels between scales. **#358 refuses it, and the refusal is load-bearing**

`TL-4`: *"Nothing reaches from one scale to another except an Echo: a magnitude derived from a Degree,
gated by scope, clamped, **targeted at a scale**, applied at a commit."*

⚠ **The precise grounds matter, and an earlier draft of this section stated them too quickly.** `T-e` forbids a
*target on an Event*, and an Echo aimed at a **scale** is not obviously a target aimed at a
**recipient**. The refusal is nonetheless firm, and it comes from three other places:

- **Reading 07 `§5`** — ***"An Event does not travel. A Claim does."*** What crosses is per-person
  belief, not magnitude.
- **Reading 07 `§8`** — *no pushed aggregate · no broadcast · **no cascade***. An Echo applied at a
  commit is a push.
- **`AX-4`, and this is the ground the first draft missed and the strongest of the four.** **Ask what
  an Echo WRITES and who owns it.** A magnitude *applied at a commit* at another scale writes a value
  that thing owns. Either it goes through that owner's write path — in which case it is not a carrier
  at all, it is an ordinary effect of an act — **or it writes what it does not own, which `AX-4`
  forbids outright.** There is no third reading, and it needs no theorem about Events.

⚠ **AND ONE GROUND THE FIRST DRAFT USED IS WITHDRAWN.** It leaned on `T-e`, and on Reading 08 `§5`'s
*"an Event that knows who it is for CANNOT BE MISATTRIBUTED"*. **#358 softens `T-e` in place** —
*"the theorem survives on the narrow ground (`Event` names no recipient); the strong gloss does not"*
(`01_AXIOMS.md:304`) — and a clamped, actor-free, scale-targeted magnitude does not touch
misattribution. **Refusing on a gloss the source had already withdrawn is the error this section is
about**, committed one document over.

**What #358 has instead, and it is not a substitute so much as a different design:** upward influence
is an aggregate **computed on demand over the containment subtree**, and downward influence is
**refraction** — a dispensation *"travels by being NOTICED, not down a chain of posts"*, and lands as
**a compliance contest per executor**, so *never received* stays distinct from *received and refused*.
**v2's own excommunication case wants exactly that**, and an Echo cannot express it: a clamped
magnitude applied at a commit has already been delivered.

## §4.2 · The rooted liege tree — **and v2's own best end-state is the one it cannot express**

v2 gives every title a `liege : TitleId`, forming a tree from realm downward. #358's Stage 2 `§A.3`:

> **"THE SUBORDINATION GRAPH HAS NO ROOT AND MUST NEVER BE GIVEN ONE. A root would be a sovereign
> nobody swore to — an institutional relation by the back door. The absence of a root is what makes a
> contested realm expressible: two people each claiming the top, with neither position being a node
> in a tree that could adjudicate between them."**

**v2 names a state very close to that as the game's most interesting terminal condition** — *"a
faction can hold eleven provinces de facto while another holds the Kingdom title de jure. That is not
a bug to be tie-broken — it is the Investiture Controversy, which is what this game is about."*

⚠ **CORRECTED IN PLACE, because an earlier draft of this section over-refused and the over-refusal is
the failure `G.4.3` names as the one that looks like rigour.** It claimed the rooted tree *forecloses
v2's own best end-state*. **It does not.** v2 expresses that state fine: one polity holds the realm
title, another holds provinces de facto, and rival assertions live in the `Claim` registry, which is
orthogonal to the liege tree. **Two claimants to one title is a pair of `Claim` rows and v2 has them.**

**The difference that survives is narrower and it is still real.** `Title.holder : PolityId |
CharacterId | ∅` is a **single field**, so at every moment there is an authoritative answer to *who
holds the realm* — possibly nobody, but always exactly one answer, written somewhere. Under #358
there is **no such field and therefore no such answer**: subordination is per-person sworn edges,
rootless, and *"two people each claiming the top"* means two people who each genuinely have others
sworn to them, **with no fact of the matter about which is king.** v2 can express *contested*; #358
can express *undetermined*. **The Investiture Controversy is the second one** — the whole content of
that quarrel was that no authority existed above the two disputants to settle it — and a design whose
schema always has an answer has quietly supplied the adjudicator the fiction says is missing.

**A second ground, independent of the first and cleaner.** `liege` is a **stored authority pointer**,
title→title. #358's `§E.1.5` is categorical: ***"THERE ARE NO INSTITUTIONAL RELATIONS. THERE ARE ONLY
PEOPLE'S RELATIONS, READ IN AGGREGATE."*** Subordination is `oblige`, sworn by a named person, owned
by the swearer, closable under `T-m` — which buys *"two arms of one body may differ"* (`:952`), the
ordinary historical case that a single title→title pointer cannot represent at all. **The tree is not
refused for being a tree; it is refused for being stored on institutions.**

⚠ **The half #358 does not win.** v2's `contract : { levy, tax, obligations, autonomy }` is a
**standing, negotiated, breachable set of terms attached to the relation**, and #358 has no equivalent.
Its `oblige` edge carries a subject, an object, dates and an optional term — **what is owed is
nowhere.** `F.17` half-notices this (*how a person joins an establishment*) and routes it to the
seat's `binds`; nothing says what `binds` contains. **v2's `contract` is a real question #358 leaves
open, and it should be asked of the `oblige` edge rather than answered with a liege pointer.**

## §4.3 · `Title` as an entity — #358 refuses it, and calls the refusal the finding

`§D.7`: ***"NOT AN ENTITY. AND THAT IS THE FINDING, NOT A GAP TO FILL BY ADDING ONE."*** A title is a
**rank whose domain is a rung kind**, so rank is the ordinal position in `rung_kinds` and needs no
second scale; `§B.7` carries no `Title` type and **no `is_title` branch anywhere**, which dissolves the
`__post_init__` collision #358 calls *a symptom marker*.

v2 makes `Title` the central object because CK3 does. Under #358's scope rule **precedent is evidence
at its own strength, never authority**, and the strength here is low: the argument offered is
*"the structure is nearly free at this scale"*, which is a cost claim, not a shape claim.

## §4.4 · `Office { holder }` — two homes for one fact, and v2's own audit fired on a weaker version

#358 `§D.6` `NEVER`: ***"Who holds it. That is a `hold` Tenure, owned by the holder — because an
office that knows its holder has two homes for one fact."*** `§B.7` goes further and makes
`establishment` a **Query over `oblige`**, not a field.

v2's `V-5` found offices filed in two places (polity and title) and resolved to **the title**. **#358
resolves to neither** — the holder owns the Tenure — which is the same audit run one step further.
v2 stopped at the first consistent answer; #358's is the one `AX-4` forces.

> ### ⚠ **AND #358 COMMITS THE SAME DEFECT ONE SECTION LATER, IN A SURFACE THIS EVALUATION HAD NOT CITED.**
> `§E.2.5`: *"a council is one Office whose **`establishment[]`** is its membership — the named
> persons the office employs"* (`01_AXIOMS.md:1078`). Its own ontology reading rules that exact shape a
> defect: *"a list of persons on a seat is **a set of edges pretending to be a field** — two homes for
> one fact; each person `oblige`s to the seat, and the roster is a Query"* (`05_ONTOLOGY.md:91`).
>
> **Stage 4 `§B.7` fixes it** — *"`establishment` is a Query over `oblige`, not a field"* — and Stage 4
> is later, so under #358's own precedence the fix governs and `§E.2.5` is stale. **But `§E.2.5` is in
> neither `PART F`'s hole register nor `§F.32`'s not-a-gap list**, so a reader arriving at Stage 1 gets
> the superseded shape with no marker. **The collision against v2 stands; #358 should fix its own
> instance in the same edit.**

## §4.5 · ⚠ **THE ONE THAT SPLITS — and the first draft's wholesale dismissal was its worst over-refusal**

**v2's `## The clock layer is a graph` section (`03-design-v2.md:1111-1138`) contains THREE separable
proposals, and the first draft refused all three on the ground that damns only the first.** An
independent critic found it, and the giveaway was internal: **this evaluation banked improvement #2
(`TL-13`) from `:1124` and improvement #12 from `:1136` — both inside the region it dismissed.**

| | the proposal | verdict |
|---|---|---|
| **(a)** | **five peninsula clocks that advance per season**, and *"an evaluator with a fixed cap per node **per season**"*, with `lag: seasons` on the edge | ⛔ **REFUSED, and the refusal is firm.** See below |
| **(b)** | **authoring the dependency network AS DATA** — `Edge { from, to, sign, weight, condition }`, *"the whole clock layer is a data file, and adding a track is adding rows"* | ✅ **ADMISSIBLE, and it is #358's own top-ranked form.** `G.3.1` ranks *"data a loader validates"* first because *"a contradiction fails the load, with the row named"* — and #358's write matrix and verb table **are already this shape** |
| **(c)** | ***"the game can show the player the path"*** | ✅ **This IS `TL-13`** (§2.2). Refusing it here while banking it there was incoherent |

> ### **THE BOUNDARY, STATED PRECISELY, BECAUSE IT IS WHERE THE WHOLE SECTION TURNS**
> **Declaring a dependency network in data is lawful. Evaluating it on a clock is not.** The same
> `Edge` rows read by a Query, on demand, at a barrier, are `ID-1` (*ask, don't store*) and `G.3.1` in
> one artifact. The same rows advanced once per season by an evaluator, with a `lag` measured in
> seasons, are **a quantity moving with no author** — and that is the whole of the objection.

**What (a) breaks.** `AX-5` licenses exactly three self-moving things: **matter, bodies, and the
fading of memory.** `T-c`: *every clock outside the three was wound by a nameable act, and therefore
has handles* — bribe the clerk who set the term, burn the record that carries it, reach the man who
must renew it. **An unwound clock is unbuyable, undelayable and unkillable, which is what a GM is.**
Loader invariant 5 (`act_only ⇒ steps ⊆ {RES}`; `MAT ⇒ world_or_act`) is the refusal at load, and
`§D.4` supplies the corpse: *a case ripening while the accused does nothing looks like it wants a
MATTER-driven stage. It does not* — **act-declared terms cost less and fix a bug the clock version
has**, because a half-made copy correctly stops if the copyist is jailed where a MATTER-advanced copy
finishes itself.

## §4.5.1 · The superseded text, kept legible rather than overwritten

`AX-5` licenses exactly three self-moving things: **matter, bodies, and the fading of memory.** `T-c`:
*every clock outside the three was wound by a nameable act, and therefore has handles* — bribe the
clerk who set the term, burn the record that carries it, reach the man who must renew it. **An
unwound clock is unbuyable, undelayable and unkillable, which is what a GM is.** Loader invariant 5
(`act_only ⇒ steps ⊆ {RES}`; `MAT ⇒ world_or_act`) is the refusal at load.

> **The first draft read:** *"v2's `Edge {…}` evaluating a five-clock layer per season is precisely
> the thing that has no author … **the graph is the wrong mechanism for a right requirement**, and
> #358's `causes[]` chain is the mechanism it already has for it."*
>
> **The last clause is still true and the sentence around it was too wide.** `causes[]` is indeed
> #358's explanation mechanism (`07_DYNAMICS.md:52`, *"the NARRATIVE LAYER, not an audit trail"*), and
> it explains **what an act caused**. It does **not** explain **why a derived quantity has the value
> it has**, which is what an inspectable dependency network gives and what a player asking *why did
> that happen* is usually asking. **The two are complementary, and #358 has only the first.**

## §4.6 · Stored `interest_groups[].approval` — ⚠ **#358 wins the ownership question and has an unstated gap on the other half**

`§D.2`'s `NEVER` exists for this exact row: ***"Any social aggregate — no norms, no unrest, no
legitimacy, no reputation. This is the row the whole ownership table exists to protect."*** And
Reading 09 `§2` answers v2's own question — *a settlement at risk of revolting* — without one:

> **risk of revolt = the share of persons at and under that rung whose LIVE commitments are to a
> proposition incompatible with the holder's.** Reversible, because a Query can fall; over live edges
> only, so it is **not a ratchet**; and *"a revolt is ORGANISED, literally — somebody uttered the
> proposition, somebody spent scenes recruiting. There is no ambient anger."*

**That is a better answer than v2's on every axis except one, and the exception is real.** #358's
Query is resolver-side and therefore **unreadable by any person, by design** (`§2.2`: *"the mayor does
not know how bad it is"*). v2's Π decomposes into named terms so that *"when Π is 8 the player can
read who is angry, which is the difference between a warning light and a political situation."*

> ⚠ **#358 never says whether the PLAYER can read it, and §2.2's tightened rule does NOT simply grant
> it.** Under that rule the engine owes the **arithmetic of what the character already holds** — so a
> mayor who holds claims about three angry guilds is owed the sum, and one who holds nothing is owed
> nothing. **Decomposing `Π` into named groups is admissible exactly to the extent the character's own
> ledger already names them**, which is a narrower promise than v2 makes and a real one #358 does not
> make at all. Until #358 states it, its answer to the hardest case it sets itself is a number nobody
> is allowed to look at — and the repair is one paragraph, not a stored field.

## §4.7 · `Claim.strength` — ⚠ **RE-GROUNDED. `T-a` does not reach it; `T-c` does**

⚠ **The first draft refused this under `T-a` and a critic overturned that, correctly.** `T-a` is about
**a value over many owners** — *"an aggregate is by definition a value over many owners … therefore an
aggregate cannot be a FIELD"* (`01_AXIOMS.md:225`). v2's `strength : Clamped<0,5>` is **a scalar on one
Claim with one writer**, which #358's own four-way taxonomy sorts to a lawful FIELD: *"one writer,
about **one** thing → **FIELD**, owned by that thing"* (`05_ONTOLOGY.md:14`). **Reading 05 names this
exact error class one line down:** *"using the wrong one is what makes a schema over- or
under-refuse."*

> ### **THE REFUSAL SURVIVES ON A DIFFERENT AXIOM, AND v2'S OWN TEXT SUPPLIES IT.**
> `R-3`: ***"their claims against the leader gain +1 strength per season"*** (`03-design-v2.md:976`).
> **That is a counter incremented by the calendar with no act behind it** — `T-c`'s fourth clock, and
> `AX-6`'s *"counters that only climb"*, in one line. `expires` bounds how long a claim lives; it does
> **not** supply an author for each increment.
>
> **So the field is lawful and the writer is not.** Under #358 the increment is an act — somebody
> pressed the claim, at a venue, paying a scene — or it is the **commitment share**, a Query that can
> fall. **What must go is the per-season write, not the field**, and stating it the first way would
> have refused a shape #358 permits.

## §4.8 · The word `Claim` — a `CLAUDE.md` §4 idempotence hazard, and the cheapest of the eight to fix

#358's `Claim` is **epistemic**: *"what one person concluded — with its provenance, its confidence,
and its capacity to be wrong"*, deposited per-witness into ledgers, and load-bearing on `AX-2`, `T-d`,
WITNESS and eviction. v2's `Claim` is **jural**: an assertion of right over a title.

**Two referents, one token, both first-class.** `CLAUDE.md` §4's test — *would a reader with no memory
of this repo land on your meaning?* — fails, and the corpse is on file: `evacuate` cost three surfaces
and two PR bodies.

> ### ⚠ **A CRITIC PROPOSED DISSOLVING THIS COLLISION BY COMPOSITION. THE PROPOSAL IS REFUSED, AND THE
> ### GROUND IS `AX-3`.**
> The suggestion was that §3.1's decomposition reconciles the two — map a jural claim's `strength` onto
> #358's `Claim.confidence` and let the epistemic `Claim` carry both jobs. **That is precisely the
> collapse `AX-3` exists to prevent**, and #358 calls it *"the single most dangerous in the design"*:
>
> > *"**Evidence** moves what is held **true**. **Argument and consequence** move what is held
> > **right**."* — `01_AXIOMS.md:111`
>
> A jural claim is an assertion of **right**; `Claim.confidence` is how sure you are of a **truth**.
> Merge them and finding a document strengthens your title, *"and the moral layer collapses into a
> second epistemic layer"* — the exact consequence `AX-3`'s own justification names. **The two objects
> must stay in different homes, which is what makes the shared token a defect rather than a
> coincidence.** They are dangerous *because they look alike from any distance*, which is `AX-3`'s
> other sentence and the reason a shared name is the worst possible outcome.

**So it is a rename, not a merge.** The jural object is an uttered `OUGHT` `Proposition` plus a commit
edge, and a distinct word — *pretension*, *pretence of right*, or simply naming it by its
decomposition — costs nothing today. **Decide before either word is written into a loader.**

## §4.9 · The tick — **three scale-indexed resolution phases, which is the one thing Stage 2 forbids by name**

This is the collision most directly on *code shape*, and it is the one a porter would walk into first.

| | #358 | v2 |
|---|---|---|
| steps | **six**, four barriers | **twelve** phases |
| resolution | **ONE ordered fold** over every act, at every scale, keyed `(stratum, actor-hash, intra-person position)` | **three phases** — `PH-04 PERSONAL` · `PH-05 SETTLEMENT` · `PH-06 PROVINCE` |
| where a contest enters | **exactly one place** — RESOLVE, *"the same call with different vocabularies"* for a battle, a hearing, an examination and two siblings arguing over a barn | per phase, per scale |
| self-advancing state | none. `AX-5`'s three motions | `PH-09 CLOCKS` + `PH-10 PIPELINES`, with `Pipeline.advance_rate` |
| epistemic layer | `PH`-less: **WITNESS** fans out globally, five declared channels, per-witness deposits into per-person ledgers | ⛔ **none. v2 has no equivalent at all** |

**Stage 2 `§C.3` refuses the middle row in terms:**

> ***"A module is not 'a settlement-scale module'. It is registered against a role and runs at
> whatever rungs the step hands it. Indexing code by scale deletes the property that makes the ladder
> worth having** — a mechanism written once for one rung type is automatically available at every rung.
> **Scale-indexed code is scale-divergent code**, and it is invisible until something composes across
> a boundary, which is the worst failure signature available."*

Stage 4 acts on it: difference **#4** of fifteen is *"`scale:` on modules and on seven verb rows →
**deleted**; the loader rejects the key"* (invariant 10). **v2's tick is three scale-indexed phases and
a fourth clock in each of two more** — `PH-09`'s influence graph (§4.5) and `PH-10`'s
`Pipeline.advance_rate`, which advances a state machine on a schedule nobody wound. `§D.4` rules on
the second directly: *a case ripening while the accused does nothing looks like it wants a
MATTER-driven stage. It does not* — **act-declared terms cost less and fix a bug the clock version
has**, because a half-made copy correctly stops if the copyist is jailed where a MATTER-advanced copy
finishes itself.

> ### ⚠ **AND THE LAST ROW BOUNDS THE WHOLE EVALUATION, SO IT IS STATED HERE RATHER THAN BURIED.**
> **v2 has no epistemic layer.** No per-person ledgers, no per-witness attribution, no channel
> predicates, no eviction on confidence × recency, no distortion in transit. Under #358 that layer is
> not a feature — it is `AX-2` and `AX-3` made mechanical, and it is where `T-d`, `T-e`, WITNESS and
> half of PART D's impossibility table live. **So on roughly a third of #358's code shape v2 is silent
> rather than wrong**, and no amount of reading it will improve that third.

⚠ **One thing in v2's tick #358 should not dismiss:** `PH-12 CHECK`'s **state hash** and v2's insistence
that derived state be rebuilt **after every commit point** rather than twice a tick. #358 has both
(the seeded golden and the barrier cache's driver-local lifetime), so this is corroboration — but v2's
corpse for it is one #358 lacks and would recognise: *"a realm that partitions in the pipeline phase
has both halves' settlements pulled toward its pre-partition Legitimacy in the very next phase."*
**A stale derived read that is invisible because the derivation is pure** is exactly `ID-13`'s
silent-in-the-flattering-direction failure, one layer down.

---

# §5 · WHAT IS OUT OF SCOPE — and #358 says so before being asked

**Most of v2's Part I and nearly all of its Part V numbers are content**, and #358 rules on the
category pre-emptively rather than case by case:

> **Stage 1 `§E.3`** — *"**NOT ARCHITECTURAL:** which kinds exist, and how many. That is content, and
> by `ID-12` it lives in data and is changed by editing a list … **do not spend design effort ruling
> the roster's membership.** Spend it on the two properties that are load-bearing — that the ladder is
> **ordered**, and that it is **walked** rather than labelled — because a mechanism that reads the
> ordinal and walks the edge is correct for any membership, and a mechanism that special-cases a kind
> is wrong for every membership."*
>
> **Stage 2 `§E.1`** — *"Whether the containment roster carries a sub-settlement tier: **content**. The
> architecture is correct for any membership, so this costs nothing to defer and nothing to change
> later."*

**So v2's headline restoration — the duchy and holding tiers — is a data edit under #358, not a
finding.** The same applies to the fourteen provinces and thirty-seven settlements, the victory
denominator of fifteen, Himmelenger/Askeheim/Schoenland, `R-1`/`R-2`/`R-3`'s **entry conditions**,
`Π_world`'s **band edges**, and the `force_limit`/`votes`/`income`/`strain` formulas — all of which v2
itself declares **unvalidated**.

## §5.1 · ⚠ **BUT THE FIRST DRAFT DISMISSED FORM ALONG WITH CONTENT, WHICH IS §4.5's DEFECT AGAIN**

#358's rule quantifies over **roster membership.** *A regime is not a roster member*, and neither is
the mechanism that arms one:

| | verdict |
|---|---|
| *legitimacy collapse* · *confessional cascade* · the numbers on each | **content** |
| **`Pipeline.regime`** — *"a pipeline reaching a state that carries a regime **arms** that regime, and the regime's own exit condition disarms it"* (`03-design-v2.md:1150`) | ⚠ **FORM. This is the operational content of `TL-7`** — the representation §2.1 says the transfer owes and does not supply |
| `Π_world`'s terms (unresolved claims, de jure gaps, armed regimes, grievances) | **content** |
| **`Π_world` as a Query composed over live edges, made of the design's own objects, and readable** (`:1026`) | ⚠ **FORM, and it is `ID-1` exactly** |

**One decidable question the blanket dismissal hid, recorded rather than ruled.** `Π_world`'s first
term is `Σ over polities of unresolved claims × strength` — **a tally summed across holders**, which
is what `L3` clause 2 forbids to a resolver-side Query (`01_AXIOMS.md:241`). Its second term,
`Σ over provinces of (de jure ≠ de facto)`, is **structural and lawful** by the same rule that
licenses Reading 09's commitment share. **The two terms fall on opposite sides of a live #358 rule,
and saying "content" hid a split that decides whether `Π_world` is expressible at all.**

⚠ **This is not a dismissal of v2's argument, which is sound in its own frame.** v2 is right that
dropping the duchy tier cost its predecessor real expressiveness. **It is a statement about where the
cost landed:** under #358 that expressiveness was never at risk, because `Rung` is one type with an
ordered kind roster and adding a kind is editing `rosters.yaml`. **The tier question is only a design
question in a model that branches on the tier** — which is `§C.2`'s scripting drift, and the thing
both documents forbid.

---

# §6 · WHAT TO ACTUALLY DO WITH THIS

**Six things, and none of them is "merge v2's shapes into #358".**

1. **Take `TL-7`, and take `Pipeline.regime` WITH it as its representation (§5.1).** #358 cannot close
   `F.28` by acquiring a vocabulary — `G.4.1` forbids exactly that — and the first draft of this
   evaluation handed `TL-7` forward as an idiom owing a representation **while dismissing the
   representation two sections later as content.** The deliverable is a **signed loop list**, the
   **arm/disarm shape** that a state reaching a threshold carries, and **the command that reproduces
   the damping/amplifying count** — `ID-11` applied to the one property #358 has never stated.
2. **Take `TL-13`, and state the split on WHAT IS SHOWN — never on who is looking (§2.2).** The
   obvious version (*the player is not an actor, so `AX-2` does not reach them*) is wrong, because the
   player controls a person. The version that holds is: **the engine owes the arithmetic of what the
   character already holds, and nothing else.** It resolves `§4.6`'s open half at the same time and
   costs one paragraph. Stated the wrong way it reads as a breach of `AX-2` and will be refused by
   the next session that meets it cold — which is `§4`'s word-choice rule at the level of a doctrine.
3. **Take the four small ones as edits, not as documents** — a second idiom on uniform suspension
   (§2.6), `G.4.3`'s third critic direction (§2.8), `TL-9`'s mutual-destruction falsifier (§2.11), and
   the procedural/graph criterion (§2.12). Under `G.4.4` each is *an edit, a row that needs Jordan, or
   nothing.* **None of the four needs Jordan.**
4. **Resolve `Tenure.conferrer` (§2.4) — but not by pointing it at patronage.** It is #358's own
   `ID-13` defect in #358's own type declaration, sitting beside `degree?`, which **is** in the hole
   register. Either find it a *seat*-shaped reader or delete it; **the person→person patronage graph
   v2 supplies belongs on an `oblige` edge**, because hanging a person-relation off a seat pointer is
   what `§E.2.2` forbids.
5. **Split v2's clock section instead of refusing it (§4.5).** Author the dependency network **as
   data** — `G.3.1`'s top-ranked form, and the shape #358's write matrix already is — and refuse only
   the **per-season evaluator**. That is one boundary sentence, and it turns this evaluation's worst
   over-refusal into `TL-13`'s missing mechanism.
6. **Fix #358's own two instances while you are in there.** `§E.2.5`'s `establishment[]` field
   contradicts `05_ONTOLOGY.md:91` and Stage 4 `§B.7`, and is graded nowhere (§4.4). And #358 has
   **no enumeration of its authored irreversibilities** (§2.13), which is why it found four ratchets
   in its own vocabulary by adversarial pass rather than by reading a register.

**And one thing to decide before either document is built from:** the `Claim` collision (§4.8). It is
free to fix now and expensive to fix after a loader reads either word.

---

# §6A · THE EXACT CHANGE LIST FOR #358 — file, section, edit

**Thirteen edits. Five are ADDITIONS of something #358 does not have; three are CORRECTIONS of
something #358 has wrong; five are SHARPENINGS of something it has under-grounded.** Nothing here
touches #358's axiom set: `AX-1`..`AX-6` and `T-a`..`T-n` are unchanged, and v2 moved none of them.

## ADD — five, and the first two are the whole of v2's positive contribution

| # | file · section | the edit |
|---|---|---|
| **A1** | `01_AXIOMS.md` PART C, after `ID-15` | **`ID-16` · NAME EVERY LOOP AND ITS SIGN.** *Every feedback path in the model appears in a signed list; a design in which every loop is negative converges, and convergence is not a design goal.* Falsifier ships with it: count the damping terms and the amplifying terms, and a zero in the second column is the finding. **This is the only edit that closes a hole #358 names in itself twice and closes nowhere** (`07_DYNAMICS.md:89`, `F.28`) |
| **A2** | `04_CODE_ARCHITECTURE.md` PART C, new `§C.11` | **THE EXPLANATION CONTRACT.** *There is no referee, so the engine inherits the referee's second job.* The split is on **what is shown**, never on who is looking: the engine owes the **arithmetic of what the character already holds**, and nothing else. Hidden actors are hidden in their **existence**, never in their **arithmetic**. **This also closes `09_WORKED_EXAMPLES.md §2.2`'s dangling half** — the revolt Query that is currently a number nobody is allowed to look at |
| **A3** | `01_AXIOMS.md` PART C | **`ID-17` · A SUSPENSION IS ITSELF A UNIFORM RULE**, attached to a named regime, never an exception carved for one entity. #358 has the *prohibition* three times (`01_AXIOMS.md:1135`, Stage 2 `§C.2`, `G.1.6`) and **no licensed form for a lawful exception**, and a prohibition with no alternative is broken quietly |
| **A4** | `04_CODE_ARCHITECTURE.md` `§G.2`, after `G.2.7` | **`G.2.8` · A PROCEDURE IS REQUIRED WHEREVER THE ORDER OF SUB-STEPS CHANGES THE OUTCOME.** #358 has both forms — the ordered fold and the pure map — and never states the criterion that decides which a thing is |
| **A5** | `04_CODE_ARCHITECTURE.md` `§B.13`, as **loader invariant 12** | **THE AUTHORED-IRREVERSIBILITY ENUMERATION.** `AX-6` quantifies over irreversibilities and #358 lists none, which is why it found **four ratchets in its own relation vocabulary by adversarial pass rather than by reading a register**. `Proposition` immutability, ended-Tenure persistence and the append-only log are authored permanences enumerated nowhere. `ID-14`'s check covers `tenure_kinds` and stops there |

## CORRECT — three, all found in #358's own text

| # | file · line | the defect |
|---|---|---|
| **C1** | `04_CODE_ARCHITECTURE.md:257` | **`Tenure.conferrer? : SeatId` occurs exactly once in all twelve files and reaches no reader.** By `ID-13` that is not a weak field, it is one that does not exist. `degree?` sits **on the same line** and *is* in the hole register as `F.4`. Give `conferrer` a **seat-shaped** reader or delete it — ⚠ **not** v2's person→person patronage reader, which belongs on `oblige`, because hanging a person-relation off a seat pointer is what `§E.2.2` forbids |
| **C2** | `01_AXIOMS.md:1078` | **`§E.2.5` puts a council's membership in an `establishment[]` FIELD on the Office**, which `05_ONTOLOGY.md:91` calls *"a set of edges pretending to be a field"* and Stage 4 `§B.7` fixes to a Query over `oblige`. Stage 4 is later and governs — but `§E.2.5` is marked in **neither `PART F` nor `§F.32`**, so a reader arriving at Stage 1 gets the superseded shape with no warning |
| **C3** | `01_AXIOMS.md` `§F.4` falsifier table | The row *"`ID-15` — a consumer that genuinely needs a faction to hold state of its own"* names the battle seam as **untested**. v2 is that test and it **passes**: v2's own battle/squad requirement is satisfied by the resolved view plus `holdings`/`members`/`seats`, with no faction-owned field. **Record the falsifier as fired and survived** rather than leaving it open |

## SHARPEN — five

| # | file · section | what gets stronger |
|---|---|---|
| **S1** | `01_AXIOMS.md §E.2.2` | **Two corpses, and of a kind #358 does not have.** Its four existing ones are *tree defects* found by reading the repository; v2's are **in-fiction absurdities** — a seat-holder commanding a rival's governor, a revolt rule stripping a rival's settlement. `G.1.2` prefers a corpse to an argument; **a corpse a player would notice beats one only a maintainer would** |
| **S2** | `04_CODE_ARCHITECTURE.md §G.4.3` | **A third critic direction.** The charter names *invent* and *over-refuse*; v2 adds **a self-audit that recorded a defect as a virtue** — misclassified in sign, by the author, inside the section built to catch it |
| **S3** | `04_CODE_ARCHITECTURE.md §G.4.1` | **The trace clause.** A stage closing on representations can still be behaviourally wrong; **the falsifier for a design claim is a trace, not a grep.** `G.4.7` binds milestones and `G.4.1` binds stage boundaries, so the connection is genuinely missing rather than merely unstated |
| **S4** | `05_ONTOLOGY.md §3` | **An admission dimension orthogonal to `IS · OWNS · ADMITS · NEVER`** — v2's per-field assertion tag, with a demonstrated hit rate of two (it moved the vacuum/stabilisation timers off the place they were never about, and forced a real semantic qualifier onto acceptance) |
| **S5** | `04_CODE_ARCHITECTURE.md` PART D, beside `D-27` | **A CONTENT-layer proper-noun scan.** `D-27` and `D-28` scan **code**; content is where a rule system rots, and #358's faction ontology — any uttered `Proposition` plus commits — makes **every** faction runtime-manufactured, so the rule binds harder here than in the design it came from |

## AND THE AXIOMS DO NOT MOVE

**No axiom, theorem or schema entry changes.** Nine v2 structural proposals were tested against them
and eight were refused by derivation (§4); the ninth split. **A meta-architecture whose axioms
survive an independent domain design built from a disjoint corpus has been tested rather than
merely asserted** — which is the result, and it is not the one this exercise was looking for.

---

# §6B · WHAT #359 DOES TO THE ACTUAL WORK, WITH #357 IN VIEW

**#357 is where the code shape actually lives**, and it is data, not prose: `verb_table.yaml` (32
verbs), `write_matrix.yaml` (40 rows), `hole_register.yaml` (91 rows), against a tracer whose
`test_tracer_is_honest.py` runs 145 tests green while the corpus reports **89 of 143 runnable, NPC
RUNS = 0, ARC ENDS = 0, and 5 of 32 verbs executed.** Measured against that, v2's effect is small,
sharp, and concentrated in one place.

## §6B.1 · The one thing v2 materially unblocks — `H-94` / `F.24`, and it is tier 0

**All 32 `requires` cells in `verb_table.yaml` are prose strings.** That is `F.24` — *the resolver has
no body returns as the resolver has thirty* — and its live twin `H-94`, graded **tier 0, absent**,
whose `unblocks` column reads *"every verb with operands — measured at 7 of 7."*

**Reading the 32 cells, the grammar they need is FIVE forms and no more:**

| form | live instance |
|---|---|
| existence over an edge kind | `a live commit exists` · `a live hold exists` |
| a computed scalar against a threshold | `stores(hearth(giver), kind) >= amount` · `condition >= floor(verb)` |
| path existence | `a contain path exists` |
| cardinality on an object | `1-per-object: no live hold on the object` |
| a relation between actor and subject | `the teller holds a claim on the subject` |

**v2's `∃ inst : presence(inst) ≥ 2 ∧ hostile(inst, holder)` is the same grammar** — quantifier,
comparison, relation — arrived at independently in a domain that never saw this table. `F.24`
*assumes* the grammar can be small and never demonstrates it; **the verb table demonstrates it and v2
corroborates it from outside.** That is the one place reading #359 changes what a builder does next.

## §6B.2 · The schema change v2 forces, and it is a MECHANISM rather than a doctrine edit

⚠ **THE GRADE IN THIS SECTION'S TITLE AND BLOCKQUOTE IS RETRACTED, 2026-09-04, AND THIS IS THE
SURFACE THAT ORIGINATED IT.** The schema change was taken — `hole_register.yaml` now has a `LOOP`
kind, a `sign` column and a loader (`G13`) — and building it showed the grade was wrong. `G13`
checks a declared row's SHAPE: that a `LOOP` row carries a sign, that the sign is `+` or `-`, that
a non-LOOP row carries none, and that an amplifying loop names its bound. It cannot see whether the
loop is real, whether its sign is right (`H-105` carried `-` on a row whose own first sentence said
it was not damping, and a critic caught that, not the gate), or whether one is missing (`H-106`).
No resolver reads `sign`; delete the column and the season loop is byte-identical. **A loader that
validates a column's shape makes the column WELL-FORMED REFERENCE, not a mechanism** — so
*"the only form in which either transfer is real"* claims more than a shape gate delivers. The
retraction is recorded at `hole_register.yaml`'s `ID-16` header, `01_AXIOMS.md`'s `ID-16`,
`07_DYNAMICS.md` and `register.py`'s `rule_G13`; it is repeated here because a reader following the
`TL-7` trail lands on THIS section first, and a retraction the origin does not carry is half a
retraction. The section below is left as written, as the argument that was made.

⚠ *Row count below is stale: the file held 91 rows when this was written and holds 102 now.*

`hole_register.yaml`'s 91 rows carry `kind ∈ {SCHEMA_ROW, FORMULA, RULING, COLLISION, PRODUCER,
NUMBER, WIRING, ABSENT_RULE, SCHEMA_COLUMN}`. **Every one of those names an ABSENCE.** There is no
row kind for a feedback path and **no `sign` column anywhere in the file.**

> **So `ID-16` (§6A/A1) and `ID-17`'s sibling cannot be taken as prose.** Under `§0.05` the register
> is a mechanism — code reads it — and the doctrine is reference. **Taking `TL-7` means adding a
> `LOOP` row kind and a `sign: +|-` column to `hole_register.yaml`, and taking `TL-12` means a
> `RATCHET` kind or a `reversible:` column.** That is a data-file schema change with a loader behind
> it, which is the only form in which either transfer is real.

⚠ **And it is the shape #358's own `G.4.1` demands:** a stage may state a property only with the
representation that carries it. **The first draft of this evaluation handed `TL-7` forward as an
idiom owing a representation. This is the representation.**

## §6B.3 · The nine tier-0 blockers, scored against v2 — six untouched

| blocker | what it blocks | does v2 help? |
|---|---|---|
| `H-94` act carries no operands | 7 of 7 verbs the decision computes | ✅ **yes — §6B.1** |
| `H-98` subsystem returns a winner, seam wants a degree | every verb declaring `contests:` | ➖ corroborates only (`TL-3` = `T-k`; #358 Stage 3 `§E.3` already answers it) |
| `H-101` nothing can be under anything | whose purview reaches whom | ➖ corroborates only; v2's **liege tree is refused** and #358 `§E.1` already answers it with `oblige` |
| `H-43` Petition/Dispensation bypass `write()` | the write gate's completeness | ⛔ **no** — #358 `§B.5` folds them into `Record` kinds; v2 is silent |
| `H-46` alignment table has no rows | the scoring function | ⛔ **no** |
| `H-49` `(Person, weight)` has no matrix row | cohorts | ⛔ **no** |
| `H-62` no verb writes any Person interior field | every interior consequence | ⛔ **no** |
| `H-71` eligibility person-side vs `remit:` | 9 of 32 verbs | ➖ partial — `TL-11`'s basis→route table is the `Seat.conferral` vocabulary, which is the same slot |
| `H-84` no verb moves a Record to a second person | ***"the whole of NPC…"*** — this is why **ARC ENDS = 0** | ⛔ **no, and this is the one that matters most** |

> ### **THE HONEST SCORE: OF NINE TIER-0 BLOCKERS, v2 MATERIALLY HELPS ONE, CORROBORATES TWO, PARTLY TOUCHES ONE, AND IS SILENT ON FIVE.**
> **`H-84` is the sharpest silence.** #358 already knows it — *"no Event anywhere has a cause that is
> an act by a different person… the clock ticks, the fold folds, the world wears, and no story has
> ever crossed between two people"* (`07_DYNAMICS.md`). v2 **cannot** help, because it has no
> epistemic layer at all: no ledgers, no per-witness attribution, no transport. **The thing standing
> between #357 and a running corpus is the layer #359 does not model.**

## §6B.4 · What v2 changes about #357's INSTRUMENT rather than its model

`test_tracer_is_honest.py` is 145 tests green against a corpus reporting **zero NPC runs**. v2's
method result names that shape exactly — **principles catch contradiction; only tracing the mechanics
catches error** — and its own split is the evidence: seven self-audit findings were all local
inconsistencies findable by grep, while three of the independent critic's nine were behavioural bugs
in text that reads perfectly.

> **So the 145 are a consistency gate, not a behaviour gate**, and #357's own `NPC RUNS = 0` is the
> measurement that says so. That is `§0.2` — *done means it runs* — arriving as an audit finding
> instead of a doctrine, which is the form that survives a reader who has not read `CLAUDE.md`.

## §6B.5 · What v2 does NOT do to the work, said plainly

- **It does not change the season loop.** #357's six-step barrier sequence stands; v2's twelve phases
  include **three scale-indexed resolution phases**, which Stage 2 `§C.3` forbids by name.
- **It does not touch the 54 UNREPRESENTABLE cases** (44 faction · 10 world). Those are `H-101` and
  `H-95`, and #358 already answers the first.
- **It does not move the critical path.** `W18 → W20 → W21 → W22 → W23 → W26 → W27 → W30` is
  unchanged; v2 adds no item to it and removes none.
- **It does not supply a single number that can be used.** v2 declares its own parameters unvalidated
  and names campaign length as the question that must be settled first.

---

# §7 · FALSIFIERS FOR THIS EVALUATION

| claim here | what would show it wrong |
|---|---|
| **v2 is a falsifier, not a source** | a v2 shape that #358's six axioms **permit** and #358 nonetheless lacks, where the shape is not derivable from anything #358 already has. `contract` (§4.2) is the standing candidate and is currently graded **half a win** |
| **`TL-7` fills a hole #358 cannot close from its own axioms** | derive a loop-sign discipline from `AX-1`..`AX-6`. If it comes out, the transfer is a restatement and should be dropped |
| **`TL-13` is compatible with `AX-2` (§2.2)** | a derivation path whose display gives the character a fact they did not already hold. The split is on **what is shown**, not on **who is looking** — so the falsifier is a preview whose arithmetic **names a source the character cannot name**, and `§4.6`'s decomposed `Π` is the live candidate: naming *which group is angry* may already be more than the mayor holds |
| **v2's `Claim` derives in #358's shape (§3.1)** | a property of v2's claim object that survives none of `Proposition` + `commit` + `term` + a gap Query. `secrecy` is the one to attack — if a claim must be **concealable from a witness who was present**, `AX-2`'s empty-observer-set account is insufficient |
| **`Title.holder` as a single field supplies an adjudicator the fiction lacks (§4.2)** | a reading of `holder = ∅` under which the title is genuinely undetermined rather than merely vacant — i.e. one where two claimants each have followers obeying them and the schema records no preference. If `∅` + two `Claim` rows carries that, the difference in §4.2 collapses to presentation |
| **the tier restoration is content (§5)** | a mechanism in v2 that is **correct only for a five-tier roster** and wrong for four or six. `strain`'s `tier_weight` is the candidate |
| **#358 wins §4.6 on ownership** | a consumer that genuinely needs interest-group approval to be **written and read back across seasons**, which the live-commitment-share Query cannot carry. This is `#358 F.4`'s open question about `Tenure.degree` wearing a different hat |
| **§4.5's boundary — data lawful, evaluator not** | an `Edge` set that is *only* read on demand and still smuggles a clock, or a per-season evaluation whose every step cites an act. Either would move the line |
| **§4.8 — the `Claim` collision is a rename, not a merge** | a reading of `AX-3` under which one carrier may hold both *what is held true* and *what is held right* without the moral layer becoming a second epistemic one. #358 calls that collapse *"the single most dangerous in the design"*, so the falsifier is aimed at the axiom, not at the word |
| **§2.13 — #358 has no ratchet enumeration** | a register row, loader invariant or test in #358 that lists its authored irreversibilities as a set. `ID-14`'s loader check covers `tenure_kinds` and nothing else; if a second exists, the improvement shrinks to *extend the list* |
| **the critic's own rate (§ verdict)** | a finding in this document that is an **invention** rather than an over-refusal. The critique found six over-refusals and no inventions, which is either a real asymmetry or a critic reading in one direction — and `G.4.3` says that is the thing to check |

---

# §8 · WHAT THIS DOCUMENT IS NOT

- **Not ratified. Merging it ratifies nothing**, and it moves no `CURRENT.md` row and no subsystem head.
- **It does not run.** Under `§0.05` it is **REFERENCE**, and nothing in it may be cited as evidence
  that any behaviour is correct.
- **It is not an amendment to either subject.** #358's twelve files and #359's seven are unchanged,
  and the scope rule each carries is unchanged.
- **It allocates no `ED` or `PP` identifier**, because it needs none.
- ⚠ **It is not an argument from `main`.** Both subjects were read as written; the working tree was
  consulted only to check three claims about #358's own text — the feedback-sign vocabulary, the
  `conferrer` reader, and the absence of `preview`/`explanation` — each of which is a count over
  `architecture/meta/` reproducible by `grep -rin`.

---

# AUDIT TRAIL

```
[READ: architecture/meta/*.md — all 12 files, in full (3,775 lines / 239,464 bytes)]
[READ: proposals/2026-09-03-governance-corpus-rebuild/03-design-v2.md — in full (1,598 lines)]
[READ: proposals/2026-09-03-governance-corpus-rebuild/02-critique-and-precedents.md — in full]
[READ: both READMEs — in full, for the provenance and scope statements §1 turns on]
[MEASURED: 358's feedback-sign vocabulary = 2 lines, both admissions of absence
          — grep -rin 'positive feedback\|amplif\|snowball\|runaway\|spiral\|compound\|escalat\|damping'
            over architecture/meta/ ; hits at 07_DYNAMICS.md:89 and
            04_CODE_ARCHITECTURE.md:628 are the two; the other two hits are unrelated prose]
[MEASURED: 'conferrer' occurs exactly once — 04_CODE_ARCHITECTURE.md:257, the type declaration.
          No reader. grep -rn 'conferrer' architecture/meta/]
[MEASURED: 'preview|explanation|explain|inspectable' — ZERO hits across all 12 files]
[ASSUMPTION: "twenty-six candidate contributions" counts v2's 13 TL principles + 10 named structural
             objects (incl. the twelve-phase tick) + 3 method results. The four buckets SUM TO MORE
             than 26 because four items split across two — TL-1, TL-5 and TL-11 each corroborate a
             #358 result AND carry a transferable test, and v2's Office collides on `holder` while
             `granted_by` transfers. A different partition gives a different denominator; the
             CLASSIFICATION is the claim, not the count]
[SELF-AUTHORED — bias risk: NO. Neither subject was authored in this session. The bias to watch is
             the opposite one — #358 is the more rigorous document and rewarding rigour over
             correctness is the failure mode here, which is why §4.2 and §4.6 are graded as splits
             rather than as wins]
[ADVERSARIAL PASS: an independent read-only critic (Read/Grep/Glob only — structural independence per
             §10, not a declared one) was dispatched with this document's OUTPUT and not its
             reasoning, under G.4.3's two-direction charter. It opened every file:line cited here.
             Result, stated as measured: SIX findings changed this document, ALL of them
             OVER-REFUSALS, and ZERO inventions were found. That asymmetry is exactly what
             04_CODE_ARCHITECTURE.md:861 predicts and is logged as a falsifier row in §7 rather
             than banked, because a critic that finds only one kind of error may be reading in
             only one direction]
[FIXED: #1 — §4.5 refused three proposals on grounds that damn one. Now splits; the boundary is
             "data lawful, per-season evaluator not". This document had banked TL-13 and the
             procedural criterion FROM THE SECTION IT DISMISSED]
[FIXED: #2 — §2.1's evidence sentence was a term-grep ('amplif*' returns zero) standing in for the
             concept. #358 reasons about feedback sign constantly under its own word, RATCHET. The
             verdict survives on the narrower cross-season claim; the evidence sentence did not]
[FIXED: #3 — §2.7 claimed §E.2.2 has "no corpse". Checkably false — four, one of them in G.3.2's own
             corpse table. Replaced with the distinction that survives: #358's corpses are tree
             defects, v2's are in-fiction absurdities]
[FIXED: #4 — §4.7 refused Claim.strength under T-a, which does not reach a single-owner scalar.
             Re-grounded on T-c, using v2's own "+1 strength per season" as the authorless write]
[FIXED: #5 — §2.11's observable (mutual destruction) cannot transfer: #358's RESOLVE is an ordered
             fold where it is unreachable by construction. Restated as permutation-invariance of the
             scene set under DELIBERATE, which is the #358 claim that actually lacks an observable]
[FIXED: #6 — TL-12 was filed as a #358 win and is a genuine improvement. Added as §2.13]
[CORRECTION: stage §4.2 — an over-refusal CAUGHT BEFORE the critique, not by it. The first draft said
             a rooted liege tree cannot express v2's Investiture end-state. It can. Re-grounded twice]
[REFUSED: the critic proposed dissolving §4.8 by mapping jural strength onto Claim.confidence. That is
             the AX-3 collapse #358 calls "the single most dangerous in the design" — evidence would
             move what is held right. Declined, ground recorded at §4.8]
[REFUSED: the critic proposed softening §2.2 on the ground that AX-2 is scoped "inside a decision" so
             a preview sits outside it. True for an NPC; false for a player character, where the
             player IS the decision procedure. Declined, ground recorded at §2.2]
[VERIFIED: python tools/valoria_local.py --staged — all local gates passed.
           python tools/ci_naming_check.py — exit 0.
           python -m pytest tests/valoria -q — 1775 passed, 2 FAILED, 23 skipped, 15 xfailed.
           THE TWO FAILURES ARE PRE-EXISTING AND UNRELATED: test_forked_status.py asserts every FORK
           row's ref resolves via `git cat-file -e`, and this clone does not carry the fork refs.
           This change is one new untracked markdown file and touches no code, register or ledger]
[ADDED §6A/§6B 2026-09-03, Jordan-directed: "what exactly changes #358?" and "with #357 pulled in
             for the actual code shape, what does #359 do to the work?" §6A is the itemized change
             list — 5 additions, 3 corrections, 5 sharpenings, and NO axiom, theorem or schema entry
             moves. §6B scores v2 against #357's live artifacts rather than against #358's prose]
[MEASURED: engine/season/verb_table.yaml — 32 verbs, ALL 32 with a
             PROSE `requires`, 24 carrying `emits_on_refusal`, grades 20 ruled / 10 assumption /
             2 absent. Reproduce: python3 -c "import yaml;d=yaml.safe_load(open(...))['verbs']"]
[MEASURED: write_matrix.yaml — 40 rows; `social:` takes true(20)/false(18)/n/a(2), which is the
             column #358 §B.13 proposes renaming to `writer:`; `steps` is a LIST on every row,
             confirming Stage 2 §D.2's "phase is a set, not a value"]
[MEASURED: hole_register.yaml — 91 rows; grades assumption 42 / absent 28 / ruled 18 / measured 3;
             tiers 0:37, 1:54; kind ∈ {SCHEMA_ROW, FORMULA, RULING, COLLISION, PRODUCER, NUMBER,
             WIRING, ABSENT_RULE, SCHEMA_COLUMN} — EVERY ONE NAMES AN ABSENCE. No LOOP kind and no
             `sign` column exist, which is why §6B.2 grades TL-7's transfer a SCHEMA CHANGE to a
             loader-read data file rather than a doctrine edit]
[MEASURED: of the 9 tier-0 `absent` rows (H-43, H-46, H-49, H-62, H-71, H-84, H-94, H-98, H-101),
             v2 materially helps ONE (H-94), corroborates two (H-98, H-101), partly touches one
             (H-71), and is silent on five. H-84 — "no verb moves a Record to a second person",
             which is why ARC ENDS = 0 — is the sharpest silence, and v2 CANNOT help because it has
             no epistemic layer to move anything with]
[ASSUMPTION: the five-form predicate grammar in §6B.1 is READ OFF the 32 live `requires` cells, not
             designed. A sixth form may exist in a cell I read as one of the five; the claim is that
             the grammar is SMALL, which is what F.24 assumes and never demonstrates — not that five
             is the exact number]
[CONFIDENCE: high on §6A and §6B.1-§6B.3 — every figure is a reproducible parse of a live file.
             medium on §6B.4 — that the 145 tracer tests are a consistency rather than behaviour
             gate follows from #357's own NPC RUNS = 0, but I did not read all 267KB of that suite.
             high on §1, §3 and §5 — every claim is a citation or a reproducible count.
             high on §2.1's narrowed claim, §2.4, §2.5 and §4.8 after the critique.
             medium on §4.1's grounds — AX-4 is now the primary ground and it is sound, but the
             first draft's T-e citation was withdrawn and a third reader may find a fourth ground.
             medium on §4.2's half-grade — whether `contract` is a genuine gap in #358 or is
             answered by `Seat.remit.binds` turns on what `binds` contains, which #358 does not say.
             LOW on the §5.1 Π_world split — it is recorded as decidable and is NOT decided here]
```
