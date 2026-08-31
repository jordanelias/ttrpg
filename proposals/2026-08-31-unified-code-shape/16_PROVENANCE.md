# 16 · PROVENANCE — how this was made, and what the method could not see

## Status: reference. **This document exists so a later session can CHECK this suite rather than trust
## it, and can see the shape of what it missed.**

---

## §1 · THE METHOD

**Jordan directed:** read PR #345's documents line by line while sweeping its scratchpad; read all
fourteen trace logs and the five prior adjudications, weighted by recency; have **Fable 5 adjudicate
read-only** and reconcile them into one ideal unified code shape; have **Opus 5 write it**; and have an
**adversarial runner** verify it for correctness, fidelity to source, Godot 4.6 logic, single ownership
and NERS compliance with elegance as a ratio.

**Scope was narrowed twice, mid-session, by Jordan**, and both narrowings are load-bearing:

1. **The three deferred subsystems are out of scope except at the seam.** `09_THE_SEAM.md` is four pages
   rather than forty because of this, and says so.
2. **The shape is IDEAL and NOT BOUND TO PRECEDENT** — it takes only the best work — and its focus is
   **the season loop, world churn, emergent narrative, and persons/the player as the throughline.**

**And one design ruling arrived mid-session and changed the ontology:** **a `Belief` is about morals,
not about the veracity of information.** Every earlier draft used *belief* as the ordinary word for what
a person holds true. **That usage is purged**, and `02` §5.5 now carries the moral layer as a first-class
part of the shape rather than as a rename.

### §1.1 The stages, and where independence was structural rather than declared

| stage | who | tools | what it produced |
|---|---|---|---|
| read | the orchestrator | read-only | the eight PR #345 documents, the scratchpad briefs, the head architecture, the play-space and arc measurements, the fixes, the slate, world events |
| **six adjudication lanes** | **Fable 5**, read-only **by agent definition** — no write tools exist for them | Read · Grep · Glob | verdicts over the fourteen trace logs and the five prior adjudications |
| **a code-trace compiler** | Opus, with execution | full | `TRACE_REGISTER.md` — every `path:line` verified this pass, **plus defects found by RUNNING rather than reading** |
| **two later lanes** | **Fable 5**, read-only | Read · Grep · Glob | the Fable-5 review scratchpad; and PR #349, judged for value and applicability |
| write | Opus 5 | full | this suite |
| verify | adversarial runner | full | `ADVERSARIAL.md` |

> **Independence here is STRUCTURAL, not declared.** The adjudicating lanes were dispatched against an
> agent definition carrying **no Write, no Edit and no Bash** — so a lane *cannot* write, whatever its
> prompt says. **Until recently every "critic" in this repository was declared read-only by a sentence
> inside its own prompt, which restricts nothing.**

**The lanes could not see each other**, and each was pointed at **a different object**: three at
different pull-request ranges, two at different halves of the tree, one at the prior adjudications
themselves. **Six of the fourteen source logs read code and registries rather than proposals**, which is
the only reason the central ruling in `15` R-2 could be made at all.

### §1.2 One honest deviation from the directed pipeline

**The reconciliation step was performed by the orchestrator on the six lane digests, rather than by a
seventh Fable agent.** The lanes adjudicated; the reconciliation and the writing were one act.

**Why, and what it costs:** a seventh lane would have re-read six digests it could not verify and
produced a seventh document to reconcile. **The cost is real and is stated rather than hidden — the
reconciliation had no independent check before the adversarial stage**, so the adversarial runner is
carrying more weight here than it would have.

---

## §2 · WHAT THE LANES OVERTURNED — including claims made by this exercise's own sources

**A lane's most valuable output is not agreement.** Ranked by how much each changed the shape:

| # | overturned | by | effect on the shape |
|---|---|---|---|
| 1 | *the constant `0.671` is an arithmetic error* | two lanes — **and both were wrong about the KIND of error** | ⚠ **RETRACTED by the adversarial pass.** It is a **different die**, exact for its own model. Replaced by a declared departure, `15` R-18. **Two lanes finding one model divergence is ONE comparison, not two derivations** |
| 2 | **the five-band degree ladder as shipped** | two lanes, and **neither trace log had recorded the collision** | `15` R-10; a fifth band is an amendment to one owner |
| 3 | **"greenfield" and "already executable"** — opposite headlines from one tree | one lane, verified against the decisive docstring | `15` R-2; **neither headline survives whole** |
| 4 | **the observer-order rule is an unratified PRECONDITION**, not a caveat | one lane | `13` step 0c — **the one blocker no session can code around** |
| 5 | **the fractional-pool defect is FIXED**; two logs are stale | one lane | removed from the execution path |
| 6 | **the project-setting causal story is refuted by the artifact it cites** | one lane | `10` §1.2 |
| 7 | **`Vector2` is float32**, undisclosed in every prior document | one lane | `10` §5.1 — a parity hazard, with the fix |
| 8 | **a "one-line fix" would break the slice's only termination input** | one lane | `10` §10 — **two files, not one line** |
| 9 | **six FALSE N-LINES** | one lane, with the pattern | `02` §9.1, `14` §3 |
| 10 | **`opening_set` returns candidates, not acts** | PR #349 | `08` §2.2 |
| 11 | **the Partition concedes a mixed class over subjects** | PR #349 | `15` R-6 — and keying on the field is what dissolves it |
| 12 | **`destroy` is NOT cleared** against the refusal rows | PR #349 | `02` §10 item 8 — **the hole is inherited, not closed** |

### §2.1 Found by EXECUTION, not by reading

**The trace compiler ran things.** These would not have been found by any amount of careful reading, and
each would have bitten a step of the execution path:

- **A campaign-length parameter is dead** — a default always wins, so a test intending five seasons
  **silently runs fifty.**
- **Four malformed fields in a cooked registry** make two event types **unemittable** — proven by
  emitting one and catching the raise.
- **Fifteen modules annotate a parameter with a type they never import**, so reflecting over any of them
  raises — **which the no-omniscience probe hits on its first run, in the very module that becomes
  `choose`.**
- **2 of 55 registered event types are emitted in a seeded campaign**; one subscriber's **thirteen
  subscriptions are all for types nothing emits**; **71 of 140 non-test modules are never loaded.**

> **That is the argument for an execution stage in a design pipeline.** Six competent read-only lanes
> did not find one of them.

---

## §3 · FINDINGS BY INDEPENDENT REDISCOVERY

**A finding rediscovered by lanes that could not see each other is the strongest signal available** —
and a convergence that was **seeded** by a shared brief is not a convergence at all, so each row below
names why it is not seeded.

| finding | lanes | why it is not seeded |
|---|---|---|
| **the running campaign resolves with zero people in it** | 3 + execution | reached from the ledger, from the tests, and by running a campaign |
| ~~`0.671` vs `0.800`~~ | 2 | ⚠ **discounted on this suite's own pessimistic rule.** Both lanes found the same *difference between two models*, which **one** comparison establishes. It was banked as a convergence and it is not one |
| **the world-substrate hole** | 3 arc lanes | one from a lost arc, one from a **dangling cross-reference**, one from a refusal list that fails to name it |
| **one act per person** | 3 | one from coverage data, one from fiction, one from the establishment argument |
| **iterate people, not factions** | 4 routes with **no citation between them** | the strongest result in the corpus |
| **the claim that does not surface** | **6 of 6** season lanes | independent seats, independent characters |
| **the convener holds the cheapest real power** | 5 | five different rungs |
| **deferred-apply barriers with a class spanning two phases** | design and code, separately | one proposed it; the other had shipped it |

---

## §4 · WHAT THIS METHOD COULD NOT SEE

**A method's limits are part of its result.**

1. **Most of the corpus is still unread.** The sweep instrument, run against current `main` this pass,
   reports **162 documents over 200 lines swept, 24 cited, 138 uncited.** **This suite has not read the
   138 either**, and its *"there is no X"* claims carry that scope limit.
2. ⚠ **AND THE COVERAGE FIGURE IS A MEASUREMENT THAT CHANGED WHAT IT MEASURED.** An earlier published
   ratio no longer reproduces — **because the sweep worked**, and the documents it found uncited were
   then revised to cite what it found. **Both figures are true of their own moment**, and neither may be
   quoted without its date and its instrument.
3. **Nothing was executed of the design.** No campaign was run to test a claim of this shape; no Godot
   project was opened. **Every `[engine]` claim is published semantics, not measurement.**
4. **The port repository is not in this checkout.** Every claim about its project file, its CI pin and
   its compile baseline is **quoted from this repository's records of runs made elsewhere.**
5. **The tracing agents are fallible in a demonstrated way.** One **fabricated** a citation appearing
   nowhere in the repository; it was caught by a blocking gate and **recorded rather than deleted.**
   Others drifted line numbers by copying rather than re-opening.
6. **Two lanes produced opposite headlines from the same tree.** Both were competent and both cited
   code. **The conflict was ruled, not averaged.**
7. **The reconciliation had no independent check** before the adversarial stage (§1.2).
8. **R is not scorable** until someone says which seats are playable (`14` §5).

---

## §5 · HOW TO CHECK THIS SUITE

- **Every factual claim about the repository carries a path. Read the path, not the claim.**
- **Every ruling in `15` carries a falsifier. Run it against the tree.**
- **Where this suite and the code disagree, the code wins** — and the disagreement is a defect in one of
  them, resolved by deciding and then **changing the code.**
- **Where this suite and a status line disagree, neither wins automatically. Ask what executes.**
- **`TRACE_REGISTER.md` is the lookup table.** Every line in it was opened during this pass; prior
  sessions' citations had drifted by 2–20 lines and one was fabricated outright.
- **Nothing here has run.** Under the standard this repository sets, **the grade for this suite is
  paper**, and `13_EXECUTION.md` step 1 is the shortest way out of it.
