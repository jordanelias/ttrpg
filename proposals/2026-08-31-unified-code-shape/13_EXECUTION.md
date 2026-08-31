# 13 · THE EXECUTION PATH — every step ends in something running

## Status: PROPOSED (2026-08-31). **HELD BACK. Nothing here ratifies on merge.**
## Layer: **L5.** **This is the only document in the suite whose purpose is to stop being a document.**
## A step is done when its behaviour EXECUTES and someone has looked at the artifact — never when a
## document exists with a status line. **Nothing below has been executed.**

---

## §1 · WHERE WE ACTUALLY ARE — measured this pass, not asserted

**What runs, and is therefore the floor:** the event log with its six raised invariants and its content
hash · the three-phase tick · the seeded regression and parity suite with byte-exact goldens · seven
exporters with blocking round-trip checks · the single-owner four-band degree ladder with its
demote-only extension seam · role resolution by string.

**What does not run, measured:**

| # | fact | how it was established |
|---|---|---|
| 1 | **Every core object of this shape is absent** — `Person`, `Rung`, `Office`, `Site`, `Tenure`, `Query`, `Act`, `Claim`, `Proposition`, `View`, `Sensation`, `StateChange` — **zero class definitions across all Python** | grep, by two lanes independently |
| 2 | **The running campaign resolves with ZERO PEOPLE IN IT.** The person generator has **zero production callers**; the population store is empty in every seeded campaign | grep + execution |
| 3 | **The population guards are blind to a direct loader.** They watch a counter only the generator increments, so writing the store directly is **invisible to every existing check** | read |
| 4 | **2 of 55 registered event types are emitted in a seeded campaign.** One subscriber's thirteen subscriptions are **all for types nothing emits** | **executed** |
| 5 | **30 of 31 faction-stat writes bypass the event log entirely.** Exactly one write path is log-mediated | counted, twice, independently |
| 6 | **71 of 140 non-test modules are never loaded** in a campaign; **9 of 14 world registries stay empty** | **executed** |
| 7 | **M1 stands at 0 of 7 junctures, verdict NOT MET**, and the row that aggregates them is **doc-derived and says so** | ran the gate |
| 8 | **None of the four structural tests has a harness** | — |

**And three defects found by RUNNING the tree rather than reading it**, each of which would have bitten a
step below:

| # | defect | consequence |
|---|---|---|
| **A** | **`run_campaign(max_seasons=N)` is a DEAD PARAMETER** — a default of 50 always wins. Passing 3 runs 50 | a population test intending five seasons **silently runs fifty**. Any step that "runs a short campaign" is not running one |
| **B** | **Four malformed fields in the cooked event-type registry** — flow-lists with trailing comments parse as **strings**. Emitting either affected type without an explicit scale signature **raises** | two event types are **unemittable today**, and nobody would find out until they tried |
| **C** | **Fifteen modules annotate a parameter with a type they never import** — reflecting over any of them raises | **T1's AST/signature probe hits this on its first run**, in the very module that becomes `choose` |

> **Defect C is a step-0 blocker for the whole path, and it was found by execution rather than by
> reading.** That is the argument for this section existing.

---

## §2 · THE RULING THAT ORDERS EVERYTHING

> **Verbatim (Jordan):** *"all faction actions, settlement governance, mass battles, etc are predicated
> upon people existing. we do not allow the game to perform faction actions if there is no leader of that
> faction, and that leader themselves is going to influence what choices are made for available faction
> actions in the same way that the person(s) who are governing a settlement or conducting a battle may
> make different choices with the same information and options."*

**Two separable clauses.** **(1) The gate:** no leader, no faction action. **(2) The decider:** the
holder's identity changes *which* choice is made.

> **The consequence, stated plainly: a campaign obeying clause 1 as written performs ZERO faction actions
> today**, because no faction has a leader and there are no people at all. **So clause 1 cannot land
> before a person loader.**

**That is why the order below is the order it is.** It is not this suite's preference; it is the ruling
arriving at its own precondition.

**And clause 2 has a shape, which the ruling itself names:** the person changes **the option set and the
pool source**. **Never a flat modifier** — worth `X / (0.800 · sqrt(Pool))`, which helps a weak pool more
than a strong one.

---

## §3 · STEP 0 — THE THREE THINGS THAT MUST BE TRUE BEFORE STEP 1

**None is a feature. Each is a blocker that would otherwise surface halfway through a later step.**

| # | what | artifact that proves it |
|---|---|---|
| **0a** | **Fix the fifteen unresolvable type annotations.** Either import the type or drop the annotation | a script that calls `get_type_hints` on every non-test module and exits 0. **T1 cannot run until this passes** |
| **0b** | **Fix the four malformed cooked registry fields, and re-run the exporter's blocking check** | emitting each affected type with no explicit scale signature **succeeds** |
| **0c** | **Ratify the observer-order rule** — a deterministic, order-preserving enumeration | the ruling recorded. **Nothing is built here.** But WITNESS cannot be built before it, and building it first bakes in hash-order nondeterminism that no test would catch |

> **0c is not code and cannot be made into code.** It is the one genuine precondition in this path that a
> session cannot discharge by working harder, and the honest thing is to name it at the front rather than
> to discover it at step 6.

**And one correction to the record while we are here:** the substrate's own docstring lists campaign-loop
wiring as not implemented; **it is wired.** Two test files assert that no large-N balance oracle exists;
**one has existed since 2026-08-21 and cites the very line that denies it.** A golden test's docstring
states win-shares that **contradict the constant twelve lines below it.** *A stale comment is not a bug
until someone plans against it — and this path plans against exactly these files.*

---

## §4 · THE PATH

**Every row names the artifact that proves it ran.** Steps 1–4 are executable against the current tree
with no new architecture. Every later step builds on an artifact an earlier step produced.

| # | what gets built | the execution artifact | what it unblocks | size |
|---|---|---|---|---|
| **1** | **The season-close emitter.** Emit `mechanical.season_change` at `SEASON_TICK` and `mechanical.accounting` at the boundary, through the existing scheduler | the suite green with **both keys visible in the log**; **flag-OFF byte-identical — the control**; flag-ON hash re-pinned with an intentional note | the running tick becomes **observable**. Closes a real juncture. ⚠ **and see the correction in §4.1** | S |
| **2** | **The determinism substream, oracle-side.** `H(world_seed, tick, subject_id, purpose)` and a per-operation generator factory, used by nothing yet | **byte-identity across every golden** — the substream exists and is called nowhere, so this is provable | **step 3 becomes possible at all.** Without it a loader draws from the shared stream and moves every golden for reasons that have nothing to do with people | S–M |
| **3** | **Person loader v0.** A default-OFF flag; ON, it creates one leader per faction and fills settlement governors, **routed through the existing generator so the counter moves and every guard sees it**, drawing **only** from step 2's substreams | flag OFF: **full byte-identity across all goldens, including the log hash** — the control arm; flag ON: a seeded campaign completes with the population counter matching the roster | **the ruling becomes satisfiable at all.** ⚠ a golden that asserts the population is zero must be **intentionally re-pinned**, named in the message | M |
| **4** | **The gate — clause 1.** With the flag on, a faction action requires a living leader; a leaderless faction acts zero times | a test that **kills a leader mid-campaign and asserts that faction's action count freezes**; the two-arm A/B recorded | faction collapse acquires a mechanism; the succession contest becomes reachable | S–M |
| **5** | **The decider — clause 2.** **Replace** the stub decision entry point with `choose(person, view, sensation) -> Act`. **A new signature — never the declared one** (`12` T1) | the stub count drops measurably; an A/B in which **two different leaders on the same seed produce divergent action mixes**; **T1 lands here** | `choose` exists in running code. **DELIBERATE has a beachhead** | M |
| **6** | **CALENDAR v0 + the `engine_clock` contract.** Minimal date and docket firing inside `SEASON_TICK`, and the tick's canon filed where its `doc` field is null | a test that **a date scheduled at tick `t` fires at `t+h`**; the existing phase test extended and still green | the loop's first step exists as code; the conferral date for step 4's dead leaders | M |
| **7** | **WITNESS v0.** The `Claim` type, the per-person ledger, and `witness(person, event) -> Claim[]` over the **existing** fan-out — **gated on 0c** | **T2 green — the first of the structural tests ever to run**; the log hash **untouched**, because interior writes touch nothing else, **and that byte-identity is the control** | the epistemic layer executes; **withheld news becomes buildable** | L |
| **8** | **RESOLVE batching + fixed point.** The additive accumulator, sum-then-clamp-once, on the integer representation | **T4 green, asserting BIT-IDENTITY**; byte-identity on every path not using the accumulator | **the parallelism licence becomes tested instead of asserted** | M–L |
| **9** | **MATTER v0 — `wear` and `yield`** — and the reorder that moves the matter half of accounting before deliberation | **golden-moving BY DESIGN** — both oracle arms plus a full re-pin naming this step; the phase test amended deliberately | **the world starts churning.** The write matrix stops carrying its declared interim violation | L |
| **10** | **CENSUS v0.** The demand-driven trigger only — *the praefect fines a smuggler and the engine must produce one* | **T3 green**; population moves in a seeded run and **the counter accounts for every creation** | the population loop closes **at its smallest honest scope** | M |
| **11** | **The candidate contract + the cast gate.** Emitters return candidates at the boundary; the gate and the rank; no depth score yet | a seeded campaign printing **a per-person cast of N**, with **every candidate carrying a non-empty provenance and a non-empty channel** | **the attention layer executes.** `06`'s whole narrative surface becomes reachable | L |
| **12** | **The ownership cut-over, faction by faction.** Build the derived faction beside the stat-bag, flag-gated | per faction: the derived Query and the stored field **agree to the last bit** while both exist; then the field is deleted and the goldens re-pinned once | Law 3 becomes true of the running tree rather than of this document | **XL** |

### §4.1 A correction to step 1, which was mis-stated in the design line

**Both key types are declared emitted by the clock module and neither has an emitter — that half is
right.** But the two are **not symmetric**, and a plan that treats them as one thing will half-close its
juncture:

- **`mechanical.accounting` HAS a declared consumer.** Emitting it closes the loop.
- **`mechanical.season_change` HAS NONE.** It is one of exactly two declared-emitted types with no
  declared consumer.

> **So step 1 emits both, and then either declares `mechanical.season_change` TERMINAL or gives it a
> consumer.** The contract row currently declares it non-terminal, so **the honest close is a contract
> edit, not a code edit** — and saying which is the difference between closing a juncture and appearing to.

---

## §5 · THE ORDER'S LOGIC, IN ONE PARAGRAPH EACH

**Why the substream precedes the loader (2 before 3).** A loader that draws from the campaign generator
shifts **every downstream draw in the campaign**. Every golden moves, and **not one of the movements is
attributable to the people it added.** That is a confounded measurement of exactly the class this
repository has already paid for, and it is unrecoverable after the fact.

**Why the loader precedes the gate (3 before 4).** The gate is a Jordan ruling. Landing it first makes a
compliant campaign perform **zero faction actions**, which is not a conservative failure — it is the game
stopping.

**Why the gate precedes the decider (4 before 5).** The gate is a **refusal** and is cheap to control: an
action count freezes. The decider **changes outcomes** and needs the gate's A/B as its baseline.

**Why WITNESS precedes RESOLVE-batching (7 before 8).** WITNESS writes only interior state, so its
control is **byte-identity on everything else** — the strongest control available. Batching moves goldens
by design. **Take the free control first.**

**Why MATTER is late (9).** It is the first step that is golden-moving **by intent** and the first whose
constant — `wear` — is unmeasured. Everything before it can be proved byte-identical; **this one can
only be proved with two arms and a re-pin.**

**Why the ownership cut-over is last, and separately sized (12).** It touches 31 write sites across nine
modules, all pinned by goldens. **It is the one step that cannot be done in one commit and must not be
attempted as one.** Faction by faction, field by field, with both representations agreeing before either
is deleted.

---

## §6 · WHAT MUST NOT BE BUILT

**A guard is earned only when the defective artifact is load-bearing on the game, the exported params,
the port, or a decision that is genuinely a person's to make.** Apparatus outnumbers game code here, so a
session reading apparatus finds apparatus defects and mints apparatus guards — **that is the generator,
and this predicate is what disarms it.**

**Licensed by this suite — four, and only four:**

1. **The autoload check** (`10` §3) — one test that the autoload table contains nothing from the
   simulation tree. **Load-bearing on the port.**
2. **The token scan** (`10` §3) — matching **by file path**, not by a token that can be spelled around.
3. **The write sweep** (`12` T5) — over **assignments**, field-parameterized. **Load-bearing on the game.**
4. **The exporter round-trip** for any new authored registry — the pattern already proven seven times.

**Forbidden:** validators over these design documents · freshness checkers · guards on guards · a
coverage gate · **any apparatus whose subject is this repository's own process rather than the game.**

> **If a defect is found in an artifact that is load-bearing only on process, that is evidence the
> artifact can be wrong without cost. Fix it in place, or delete it, and write nothing.**

---

## §7 · THE HONEST SUMMARY

**Step 0 is three fixes, one of which is a ratification nobody can code around.** Steps 1–2 are small and
provable by byte-identity. **Step 3 puts the first person into a game that currently has none**, and
steps 4–5 discharge a standing ruling. **Steps 7, 8 and 10 are the first time any structural claim in
this shape is tested rather than argued.**

**Step 12 is larger than steps 1–11 combined**, and it is the price of Law 3. It is stated at the end,
sized honestly, rather than folded into an earlier row to make the path look shorter.

> **Until step 1 lands, the correct description of this entire suite — every document in it — is that it
> is prose.** That is not false modesty. **It is the standard, and the only reason this document exists
> is to be the shortest path out of it.**
