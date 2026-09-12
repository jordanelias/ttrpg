# What survives R2 — the refusals that earn their place, argued

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

**This document exists because `R2` demands it.** Having struck every `A` and `I` disposal, the opposite
failure is now available: declaring everything open. `R2` forecloses that too
(`references/design_rulings_2026-09-06.md:44-50`):

> ⚠ *"**But most of them were derived to serve exactly these properties**, so a naive reading reduces what
> it means to increase: no target on an Event exists because misattribution is a feature (that IS
> emergence); only a person acts is why obstruction and deception need no verbs (capability per unit of
> machinery); no stored aggregate is why a resolved view cannot go stale (dynamism).
> **The null result — "examined, this refusal earns its place" — is a real finding, and must be argued
> rather than deferred to.**"*

**So each refusal below is argued against the five terminal properties — dynamic · capable · flexible ·
emergent · persistent — and none is merely cited.** Where the argument only reaches part of a mechanic,
the lawful remainder is named, because a refusal that does not say what survives it is an unargued one.

⚠ **R2 names one `A` that has a `G` argument behind it**, and honesty requires reporting it: *"no stored
aggregate is why a resolved view cannot go stale (dynamism)."* That is a real claim — but it is a claim
about **staleness of a cached read**, and `T-a` restricts itself to exactly that scope
(`architecture/meta/01_AXIOMS.md:279-282`): *"a barrier cache is discarded at the next barrier and
therefore **cannot go stale**… Say **cannot be a field**, never **cannot be stored**."* So the dynamism
argument reaches a **stale cache**, not a **gameplay quantity**. The `A` still carries no veto over an
idea; what it carries is a constraint on the implementation that idea eventually gets.

---

## 1 · A SCHEDULER, STORYTELLER, DIRECTOR OR BEAT MANAGER THAT MAKES THE WORLD ACT ON A PERSON

**The line.** `AX-1`, `architecture/meta/01_AXIOMS.md:71-74` — *"**ONLY A PERSON ACTS.** No institution,
no faction, no threshold, no clock, no container, and no engine is ever the subject of a decision."*

**Argued against the five.** **Capable** and **emergent** are the two this buys, and it buys them by
subtraction. A storyteller is a second author competing with the player for causation: every event it
produces is an event no person chose, so the world's drama becomes a *schedule* rather than a
*consequence*. **Flexible**: an authored scheduler must enumerate its situations, so the space of what can
happen is the size of its table; persons acting on beliefs enumerate nothing. **Dynamic**: a scheduled
event is the same event in every campaign. And the one that is decisive — **persistent**: a scheduled
event has **no antecedent a player can reach**. `T-c` states the yield exactly: an authored clock can be
*"bribed, delayed, burned, or killed"*, and an unwound one *"is unbuyable, undelayable and unkillable,
which is what a GM is."*

**What survives it, and it is most of what the corpus wanted.** ED-IN-0011 ratified a **subtract-only**
director — one that *rations* rather than *shapes* — and that half has zero `.py`. So *pacing as a concern*
is not refused; **pacing done TO the player** is. A band crossing that **raises a Question** for whoever
is present ships today (`loop/matter.py:260-277` → `queries/world_q.py:234-238`).

**VERDICT: EARNS ITS PLACE.** The attack that failed: *"a subtract-only director is still a director."* It
is — and it is ratified in that form, so the idea survives where the pushed form dies.

---

## 2 · A THRESHOLD THAT PRODUCES AN OUTCOME

**The line.** `T-b`, `01_AXIOMS.md:284-290` — *"A threshold may change what can be chosen; it may never
produce an outcome… a threshold that produced an outcome would be an actor."*

**Argued against the five.** **Emergent**: a firing threshold is a deterministic branch, and the surveyed
corpus of arcs says so — `:288-290` records that **19 of 50** surveyed arcs wanted a crossing *to force a
moment and then have a person choose*, which is what the design supplies. **Capable**: one mechanism
(crossing → question) serves every quantity, where a firing threshold needs an outcome authored per
quantity. **Persistent**: a person's choice at a forced moment has an author and can be resented,
appealed, or avenged; a threshold's firing cannot.

**What survives it.** Everything the corpus actually wanted. Approval slopes, immigration pressure,
resolve, patience — each may be a quantity whose **crossing raises a Question**. That is a
one-substitution transfer, not a refusal, and the substitution executes.

**VERDICT: EARNS ITS PLACE.** The attack that failed: *"the corpus wants the crossing to force a
moment."* It does, and the design gives exactly that.

---

## 3 · AN AUTOMATIC BOARD WIPE AFTER A SCORING EVENT

**The line.** `AX-6`, `01_AXIOMS.md:185-188` — nothing becomes permanent without an author.

**Argued against the five.** **Persistent** is the whole argument, and it runs the way the word suggests:
a wipe *deletes* history, so a game with periodic wipes is less persistent by construction. **Emergent**:
consequences that expire on a schedule cannot compound, and compounding is where unplanned stories come
from. **Dynamic**: a wipe resets the state space to the same starting point every cycle.

**What survives it.** A **convened** sitting at which a person decides — `H-32`/`W7`'s shape
(`loop/effects.py:181-183`), unbuilt. So *the reckoning* survives; *the automatic* wipe does not. Proposal
2 is built on exactly that distinction.

**VERDICT: EARNS ITS PLACE, on the automatic half only.** ⚠ v1 grounded this on `AX-3` as well; `AX-3`'s
carve-out governs **claim confidence**, a different quantity, and that citation was a pattern-match.

---

## 4 · META-PROGRESSION ACROSS RUNS

**The line.** Not an axiom — the project's shape: one persistent campaign.

**Argued against the five.** **Persistent**, trivially and completely: there is no second run for a
carry-over to reach. This is the one refusal that is a statement about the object rather than a judgment.

**What survives it.** Dynastic succession is the same appetite satisfied *inside* one campaign, and
`succeed` + `heir.designated` is declared for it (proposal 10).

**VERDICT: EARNS ITS PLACE — INAPPLICABLE rather than refused.** The attack that failed: *"dynastic
succession is a soft reset."* It is, and it is already in the vocabulary.

---

## 5 · SALIENCE-RANKED MEMORY RETENTION

**The line.** `architecture/meta/07_DYNAMICS.md:182-184` — *"the correct bound is **who could have
perceived this**, never **how important it is**. Bound it by importance and you have built salience-ranked
memory, which is a narrator deciding what matters — **the actor the design exists to refuse.**"*

**Argued against the five.** **Emergent**: forgetting is load-bearing fiction here, not a defect —
`:171-175`, *"influence is not taken away; **it lapses**. He loses the town by being forgotten is not a
mechanic anyone wrote — it is what happens when nobody spends a scene renewing the claim."* A ledger that
protects important claims **deletes that mechanic**. **Capable**: the same comparator serves every claim
kind, and importance would need authoring per kind. **Flexible**: an importance function is a second place
the designer's hand shows.

⚠ **And the scope is narrower than v1 claimed.** v1 wrote *"salience-ranked selection, **anywhere**"*.
That is false of this tree: **questions are ranked** before a budget-bounded person answers them — across
sources by an order `rosters.yaml` itself calls **semantic**, and within a source by lexicographic order
over content hashes, measured deciding `qs[0]` in **801 of 1,068 deliberations**
(`queries/world_q.py:250-269`, `H-54`). Ranking a **question** is shipped; its within-source half is
**undeclared**, which is a live hole and not a design property.

**What survives it.** A person's **own convictions** shaping what they retain is characterisation, not
narration, and the quoted line does not reach it. Recorded as an observation, not proposed.

**VERDICT: EARNS ITS PLACE, scoped to the ledger comparator.** ⚠ The *"enforced by signature"* half of
v1's argument is `A` and adds nothing to the case.

---

## 6 · A WORLD-TRUTH READOUT ON THE MAIN VIEW

**The line.** §C.11, `04_CODE_ARCHITECTURE.md:751-765` — *"there is no referee, so the engine inherits the
referee's SECOND job"*, and *"the engine owes the **ARITHMETIC of what the character already holds**, and
nothing else."* R7 makes it structural: *"the player sees their character's **ESTIMATE**, never the true
aggregate."*

**Argued against the five.** **Emergent**: a true readout collapses every misunderstanding, and
misunderstanding is where the corpus's rarest drama comes from — R7's own consequence 3 is *"a ruler can
be wrong about their own standing"*, written as a **yield**, not a cost. **Dynamic**: two players with
different information make different decisions from the same world. **Capable**: one epistemic rule
replaces a per-quantity decision about what to reveal.

**What survives it, and v1 refused this half too.** §C.11's **first** obligation is that the engine *owes*
the arithmetic of what the character **does** hold. So a rival's state **learned by an act** may be shown
(proposal 7), and a `Date` the character convened is a fact they hold and must be rendered (proposal 1).
**§C.11 is a mandate as much as a limit, and v1 used only the limit.**

**VERDICT: EARNS ITS PLACE — and obliges two of the ten proposals.**

---

## 7 · ANY GM-ARBITRATED ELEMENT

**The line.** `ARCHITECTURE_V2.md:94`; and `CLAUDE.md`'s own head — **there is no GM; the engine resolves
everything.**

**Argued against the five.** This is the premise the other four properties are instrumental to. A GM is
maximally **flexible** and minimally everything else: nothing a GM adjudicates is **persistent** (it is
re-decided each time), **dynamic** (it is one person's judgment) or **emergent** (it is authored at the
moment of use). The whole design is the wager that removing the GM and keeping the consequences buys more
than it costs.

**What survives it.** Nothing needs to. But the consequence v1 under-reported: **parts of the canonical
prose layer cannot be lifted**, because several of their mechanisms name a GM as the resolver. That is a
porting cost on the *existing corpus*, not a refusal of any new idea.

**VERDICT: EARNS ITS PLACE — terminal for this project.**

---

## 8 · AUTO-ALLOCATING LABOUR TO ZONES

**The line.** `AX-1` — *"a zone that allocates persons is nobody deciding."*

**Argued against the five.** **Emergent** and **persistent**: an auto-allocator produces no refusals, and
a refusal is the only thing that makes a labour order a *story*. **Capable**: the allocator must encode a
priority scheme that the design otherwise gets for free from persons with their own reasons.

⚠ **What survives it is large, and v1 refused the whole family.** `AX-1` refuses **the container
deciding**. It does not refuse **a steward directing labour and labour deciding whether to comply** —
which is this tree's own declared S-DOWN channel, and it is entirely unbuilt: `issue`
(`verb_table.yaml:245-256`, `grade: ruled`), `comply` (`:119-123`), `evade / defy` (`:209-213`), `oblige`,
`repudiate`. **Five verbs, no effect body between them** — the management corpus's richest family, and
this tree's largest declared-and-silent surface. The cited prior cut says so itself: *"the lawful
crowd-labour is a cohort's `work`."*

**VERDICT: EARNS ITS PLACE, on the container-decides shape only.** The refusal buys the one improvement
the corpus's version lacks — **labour that can refuse** — and the improved form is unbuilt, not refused.

---

## 9 · ANTICIPATION SURFACES — PROGRESS CLOCKS, TENSION METERS, COUNTDOWNS, ACT LABELS

**The line.** **RATIFIED, ED-IN-0011**; the NOT-list at
`audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md:130-133`, and
`…v2_churn.md:393-402` — *"never a meter… no quantized horizon ever surfaces"*, *"on every anticipation
surface"*.

**Argued against the five.** **Emergent**: a visible countdown converts an open situation into a solved
one — the player optimises against the number instead of acting on belief. **Flexible**: a surfaced
horizon commits the design to knowing *when*, which forecloses every outcome that arrives early or not at
all.

⚠ **What survives it is the proposal ranked first in this suite.** The ruling binds **anticipation**. A
**retrospective** walk forecasts nothing, and the same NOT-list licenses it in the sentence after the
veto: *"**What the engine CAN produce:** … retrospective coherence (chronicle + `causes[]` walk) —
experienced forwards as pressure and choices, **recognized backwards as story**."* And a `Date` a person
convened is a fact **that character holds**, which §C.11 obliges the engine to show — the narrator-readout
half is refused, the character-held half is ruled in and unrendered.

**VERDICT: EARNS ITS PLACE, on anticipation only.** ⚠ v1 refused both halves and cited the licensing
document as the veto.

---

## §S · THE NINE, AND WHAT EACH LEAVES STANDING

| the refusal | earns its place because | what survives it |
|---|---|---|
| a scheduler that acts on a person | a scheduled event has no antecedent a player can reach | a **subtract-only** rationing director (ratified); a crossing that raises a Question |
| a threshold that produces an outcome | 19 of 50 arcs wanted the crossing to force a moment, not decide it | every corpus meter, as a quantity whose crossing asks |
| an automatic board wipe | a wipe deletes history, so it is anti-persistent by construction | a **convened** reckoning at which a person decides |
| meta-progression across runs | there is no second run | dynastic succession, inside the one campaign |
| salience-ranked memory | *"he loses the town by being forgotten"* is the mechanic it would delete | question ranking (shipped); convictions shaping retention |
| a world-truth readout | misunderstanding is R7's stated **yield** | §C.11's mandate — the arithmetic the character **does** hold |
| a GM | the project's premise; a GM is flexible and nothing else | — (a porting cost on existing prose) |
| auto-allocating labour | an allocator produces no refusals | **a steward ordering and labour refusing** — five declared verbs, no effect bodies |
| anticipation surfaces | a countdown turns an open situation into an optimisation | **the retrospective chronicle** — ranked first in this suite |

**Nine refusals hold. Eight of the nine leave a lawful remainder that is unbuilt** — which is the finding
this document exists to produce: **the design's closures are narrow, and what they leave standing is
mostly not built yet.** That is a very different statement from v1's, and it is the one the evidence
supports.
