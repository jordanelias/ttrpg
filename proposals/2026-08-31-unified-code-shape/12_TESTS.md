# 12 · THE TESTS — every structural claim, with an assertion that can observe its failure

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L5.** **None of these has ever been run.** That is the honest state of every structural
## claim in this suite, and this document exists to make each of them falsifiable rather than argued.

---

## §1 · WHAT A TEST IS FOR HERE

**These are not coverage.** Each exists to make a structural claim **falsifiable**, and each fails
loudly the moment its property is lost.

**Four rules bind every test below, and each is here because its absence cost something real:**

| # | rule | the failure it prevents |
|---|---|---|
| 1 | **An assertion must be able to OBSERVE the failure it excludes.** `approx` on an exactness claim is not a weak test — **it is an absent one** | a one-ulp aggregate error crossed a degree boundary while its own identity test passed |
| 2 | **A loop that asserts conditionally must assert that it asserted** — `assert checked >= N` | a test that silently checked nothing and passed |
| 3 | **Name the falsifier, and prove the scanner can fail** — a fixture that deliberately breaks the property, which the test asserts **is** flagged | *"adversarially reviewed"* with no artifact is unfalsifiable, and was once false |
| 4 | **A number without a control is not a measurement, in EITHER direction** | a favourable uncontrolled result was banked and an unfavourable one published, in one session |

**And one thing these tests are explicitly NOT for.** No test here has this repository's own process as its
subject. **A guard is earned only when the artifact it protects is load-bearing on the game, the exported
params, the port, or a decision that is genuinely a person's to make.** Everything below is load-bearing
on the game.

---

## §2 · THE FOUR STRUCTURAL TESTS

### T1 · NO DECISION FUNCTION CAN SEE THE WORLD

**The claim.** `choose` and every person-side Query read the actor, their view and their sensation, and
nothing else.

**Setup.** Import the module owning `choose` in a **subprocess**, so that import side effects are
observable. The pattern exists and works: a probe already in this repository imports one package in a
subprocess and asserts the interpreter loaded **zero** modules of a forbidden family, with its regex
ceilings held at 0.

**Assertions.**
- **(a)** `inspect.signature(choose)` has **no parameter typed or named `world`**.
- **(b)** An AST walk over the module finds **no reference to any global state accessor**, no import of
  the hub, and **no read of the event log** — the last clause being the one people forget, because a
  decision function reading the log has re-introduced the world **by the back door**, and it will not
  look like a violation at the call site.
- **(c)** **The scanner is proven able to fail:** a fixture module that deliberately reads the hub is
  scanned, and the test asserts it **is** flagged, plus `assert modules_checked >= 1`.

**Falsifier.** Add a `world` parameter or a hub import — (a)/(b) go red. Delete the fixture — (c) goes red.

> ⚠ **CARRIED CAVEAT, AND IT IS PERMANENT.** [engine] In GDScript this downgrades to
> *unreachable-by-name*. **The Python test is the oracle-side enforcement; the port carries the
> World-first argument convention plus the one-line autoload check and the token scan.** Do not write
> the port test as though it proved the same thing.

> ⊕ **AND ONE STEP-ZERO OBLIGATION NOBODY NOTICED** [LANE F B7]. The stub that is to become `choose`
> currently declares the signature `select_action(actor_id, world)` — **the exact shape T1 forbids.**
> **The entry point is REPLACED with a new signature; it is never implemented as declared.** Implementing
> the stub as written forfeits T1 at birth, and no adjudication caught it.

### T2 · TWO WITNESSES OF ONE EVENT CAN DISAGREE

**The claim.** Perspective is divergent by construction, not by tuning.

**Setup.** One event; two observers of **different vantage and different marks**. Call `witness(p1, e)`
and `witness(p2, e)` — **two calls. The collection signature must not exist to be called.**

**Assertions.**
- Both return **non-empty** claim lists — `assert len(c1) and len(c2)`, which observes the vacuous pass.
- The claims have **distinct ids** and **differ in value or construal**.
- **Each deposited only into its own ledger**, asserted by **the other ledger's length being unchanged**.
- **`assert witness_call_sites == 1`** — a scan proving `witness` has exactly one call site, because the
  refusal is conventional in the port and a convention with no check is a hope.

**Falsifier.** Implement `witness` as a broadcast writing one shared claim — the distinct-id assertion
fails. Implement it reading the other ledger — the length assertion fails.

> ⚠ **AND A PRECONDITION THAT IS NOT A CAVEAT.** The executing substrate deliberately does **not**
> implement observer resolution, **because the ordering rule that would make it deterministic is
> proposed and unratified**, and implementing it first *would bake in hash-order nondeterminism*.
> **Ratify the observer-order rule — a deterministic, order-preserving enumeration — BEFORE building the
> fan-out**, or T2 passes while T4 silently fails. The rule is drafted; what is missing is a ratification.

### T3 · A PERSON WITH NO OFFICE CAN ACT, PETITION, AND RECEIVE AN OPPORTUNITY

**The claim.** Office changes whether a decision **binds others**, never whether you may act. **This is
S-DOWN, and it is the criterion the running tree fails today.**

**Setup.** A person holding **zero `hold` Tenures over any Office**, and holding no rank in any practice.

**Assertions.**
- `opening_set(person, view)` is non-empty — `assert len(openings) >= 1`.
- It contains `petition`.
- **It contains at least one act from three different families** — `assert len(families) >= 3` — because
  the measured predictor of a playable seat is **mode count**, not act count.
- A chosen act reaches RESOLVE and produces an Event — **refusal-by-obstacle is legal;
  refusal-by-eligibility is the failure** — and `assert resolved_count >= 1`.

**Falsifier.** Gate `opening_set` or the resolver on office-holding, **or on a practice rank**: the set
empties or the act is refused, and the test observes exactly that.

### T4 · ORDER INDEPENDENCE

**The claim.** The season's outcome does not depend on the order persons were processed in.

**Setup.** Six acts against one world snapshot, including:
- **the poison triple** — three `alter`s of `+0.3, −0.5, +0.3` on one additive field **sitting at `0.9`**,
  which is a band edge;
- **one conflicting pair** — a `destroy` racing a `create` on the same parent.

**Assertions.** Over **at least ten permutations** of submission order, sampled plus **both extremes**:
- the canonicalized Event list is **identical**;
- **the post-state hash is BIT-IDENTICAL — not approximate**;
- the conflicting pair routes to `contest` **in every permutation**;
- `assert permutations_run >= 10`.

**Falsifier.** Clamp-as-you-go fails the poison triple. A submission-position tie-break fails the
Event-list identity. **Float accumulation without fixed point fails the bit-identity at the last bit —
which is precisely the failure the assertion must be able to see, and which an approximate comparison
would blind it to.**

---

## §3 · THE FIFTH TEST, WHICH THE FOUR DO NOT COVER

### T5 · THE WRITE MATRIX HOLDS

**The claim.** No value is written outside its class.

**Setup.** For each row of the write matrix, a **write sweep** over the field's **assignments** — not its
readers, which are unbounded and mostly harmless.

**Assertions.** Every assignment site to a matrix-governed field is inside a step the matrix permits;
**the registry of governed fields is parameterized, so a newly class-owned value inherits the guard by
adding one key**; and a fixture containing a **new bare assignment** is asserted to be flagged.

**Falsifier.** Add a bare assignment anywhere outside the permitted step — the sweep flags it.

> **This is the guard the read/write-asymmetry hazard earns**, and it is the one guard-shaped thing this
> suite licenses beyond the two port checks. The pattern already exists in this repository for a
> cell-owned field, and the reason it earns its existence is the predicate, not the technique: **the
> artifact is the game.**

---

## §4 · THE CONTROL DISCIPLINE — what proves a change did what it says

**Every change carries a control, and the control is chosen by whether the change is campaign-reachable.**

| the change | the control |
|---|---|
| **cannot** move a golden | **prove it**: byte-identity across the seeded campaigns **including the log hash** |
| **is meant to** move goldens | **both arms**: an n≥100-campaign comparison, **plus** an intentional re-pin with a note naming the step |
| **is campaign-unreachable** | **both oracle arms are identical by construction. Running it there is a FAKE control, and saying so is part of the discipline** |

> ⚠ **AND ONE THING THE SUITE DOES NOT CREDIT ITSELF WITH.** The unit suite is a **shipping gate, not a
> belief gate.** It caught one confounded measurement **only** because the change incidentally broke ten
> unrelated tests; **a clean implementation of the same confounded measurement would have been green.**
>
> **Equally, targeted-green is not validation.** The tests you write for the thing you built encode
> **your model of it**, not the system.

---

## §5 · THE TESTS THIS SHAPE REFUSES TO WRITE

| refused | why |
|---|---|
| a validator over these design documents | its subject is this repository's process, not the game |
| a freshness checker on any document here | same |
| a guard on a guard | the recorded pathology: 1,718 lines guarding the prelude of the scripts that ran the audits |
| a test that the design's status lines are consistent | **prose is reference; a status line is not a mechanism** |
| a coverage-percentage gate | coverage is not correctness, and a percentage is satisfiable by writing tests for what is easy |
| a convergence checker | **§6.1 of `06` argues this properly**: if convergence is a game property it is settled by running campaigns, not by building a checker |

---

## §6 · WHAT IS MEASURED, NOT ASSERTED — and every number here is owed

**Six quantities in this suite are MEASUREMENTS, not rulings, and no amount of argument settles any of
them.** They are listed here so that nobody records a settled-looking number for one.

| # | quantity | why it cannot be argued | what would settle it |
|---|---|---|---|
| 1 | **`wear` : restoration ratio** | it sets **the entire difficulty curve**: too high and the world dies whatever anyone does; too low and tending is decoration | campaigns at a range of ratios, comparing the distribution of site outcomes |
| 2 | `season_factor`'s distribution | it multiplies every harvest | the same |
| 3 | the requisition **burden** coefficient | flagged as doing **more dramatic work than any other coefficient in the design**, and **untested by either exercise** | A/B at seats |
| 4 | the ledger cap `L` and the view budget `K` | they set how much a person can hold and retrieve — **and therefore whether the decisive claim surfaces** | the measured failure was *the claim that does not surface*, found by **6 of 6** lanes |
| 5 | **whether confrontations arrive at all** | **the sharpest unmeasured claim in the suite** — there is a recoverability check and no convergence check | campaigns, counting collisions |
| 6 | the individuated-person ceiling | the loop is linear in persons **only after** the six O(N²) surfaces are made linear | a run, at a real N |

> **Nothing in this suite has been run. The four structural tests have never executed. The verdict on the
> whole shape is paper-grade until they do — and the documents saying so is the single most creditable
> thing about them.**
