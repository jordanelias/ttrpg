# 07 · THE EXECUTION PATH — every step ends in something running

## Status: PROPOSED (2026-08-31). **This is the only document in the suite whose purpose is to stop
## being a document.** `CLAUDE.md` §0.2: a juncture is done when the behaviour EXECUTES, not when a
## document exists with a `## Status:` line. **Nothing below has been executed.**

---

## §1 · WHERE WE ACTUALLY ARE

Measured, not asserted:

- `tools/m1_acceptance.py --summary` — **M1 at 0/7 junctures, verdict NOT MET.** Matches
  `workplans/workplan_v6_progress.yaml`.
- **Every core object of this architecture is absent from `engine/` and `systems/`** as a named
  identifier: `Person`, `Rung`, `Office`, `Site`, `Tenure`, `Query`, `Act`, `Claim`.
- **The running campaign resolves with zero people in it.** `world.npcs` is empty in every seeded
  campaign; `generate_npc` has no call site; `mc_v18.py` stub-wires NPC generation and knot formation
  rather than fabricate a trigger it has no canon for.
- **The population guards are blind to a direct loader.** They watch `world.npc_counter`, which only
  `generate_npc` increments — so writing `world.npcs` directly is invisible to every existing check.
- **None of the four structural tests has a harness.**

**What does run, and is therefore the foundation:** the Key substrate with its invariants and content
hash; the three-phase tick; the seeded regression and parity suite with byte-exact goldens; the seven
exporters with blocking `--check` round-trips; the single-owner degree ladder.

---

## §2 · JORDAN'S RULING THAT ORDERS EVERYTHING

**ED-IN-0201, verbatim, ruled 2026-08-27/28, `status: open`, `needs_jordan: false`:**

> *"all faction actions, settlement governance, mass battles, etc are predicated upon people existing.
> we do not allow the game to perform faction actions if there is no leader of that faction, and that
> leader themselves is going to influence what choices are made for available faction actions in the
> same way that the person(s) who are governing a settlement or conducting a battle may make different
> choices with the same information and options."*

**Two separable clauses.** (1) **The gate:** no leader, no faction action. (2) **The decider:** the
holder's identity changes *which* choice is made.

**The consequence, stated plainly: a campaign obeying clause 1 as written performs ZERO faction
actions today**, because no faction has a leader. **So clause 1 cannot land before a person loader.**
That is why the order below is the order it is — and it is Jordan's ruling that makes this the
critical path, not a preference of this suite.

---

## §3 · THE PATH

**Every row names the artifact that proves it ran.** Steps 1–4 are executable against the current tree
with no new architecture. Every later step builds on an artifact an earlier step produced.

**Control discipline** (`CLAUDE.md` §0.1 point 4 — *a number without a control is not a measurement, in
either direction*): a change that cannot move a golden must **prove** it by byte-identity across the
seeded campaigns including the key-log hash. A change that is *meant* to move goldens carries the
two-arm `tools/balance_oracle.py` comparison (n ≥ 100 campaigns; deliberately not a CI gate at
~13 minutes) **and** an intentional re-pin with a commit-message note naming this step. **A change that
is campaign-unreachable makes both oracle arms identical by construction — running it there would be a
fake control, and saying so is part of the discipline.**

| # | what gets built | the execution artifact that proves it | what it unblocks | size |
|---|---|---|---|---|
| **1** | **Season-close emitter.** Emit `mechanical.season_change` at `SEASON_TICK` and `mechanical.accounting` at the boundary, through the existing scheduler | `pytest engine/tests` green with both keys visible in the KeyLog; **flag-OFF path byte-identical (the control)**; flag-ON hash re-pinned with an intentional note | **M1 juncture 6** — the consumer is already built and tested and has never had an emitter. Makes the running tick observable | S |
| **2** | **Person loader v0.** A default-OFF `PERSONNEL` parameter; ON, it mints one leader per faction and fills settlement governors — **routed through `generate_npc` so `npc_counter` moves and every guard sees it** — drawing from derived substreams, **never `world.rng`** | flag OFF: **full byte-identity across all goldens** — this is the §0.1-pt-4 control arm; flag ON: a seeded campaign completes with the population counter matching the roster | ED-IN-0201 becomes satisfiable at all | M |
| **3** | **The gate (clause 1).** With `PERSONNEL` on, a faction action requires a living leader; a leaderless faction acts zero times | a test that kills a leader mid-campaign and asserts that faction's action count **freezes**; the two-arm `balance_oracle` A/B recorded — **the control ED-IN-0201's own consequences demand** | faction collapse acquires a mechanism; the succession contest becomes reachable | S–M |
| **4** | **The decider (clause 2).** De-stub `npc_ai.select_action` into the first real `choose(person, view, sensation) -> Act`. **Identity gates the option SET; it is never a modifier on a roll** | the M1 probe's stub count drops measurably; an A/B in which two different leaders on the same seed produce divergent action mixes; **structural test T1 lands here** | `choose` exists in running code. DELIBERATE has a beachhead | M |
| **5** | **`engine_clock` canon + CALENDAR v0.** File the design doc — closing one of the nine `doc: null` modules — and implement minimal date and docket firing inside `SEASON_TICK` | a test that a Date scheduled at tick *t* fires at *t+h*; the existing phase test extended and still green | the loop's first step exists as code; the conferral date for step 3's dead leaders | M |
| **6** | **WITNESS v0.** The `Claim` type, the per-person ledger, and `witness(person, key) -> Claim[]` over the **existing Key fan-out** — the visibility machinery already carries observer sets | **structural test T2 green — the first of the four ever to run**; the KeyLog hash is untouched, because INTERIOR writes touch nothing else, **and that byte-identity is the control** | the epistemic layer executes; withheld news becomes buildable | L |
| **7** | **RESOLVE batching + fixed point.** The additive accumulator, sum-then-clamp-once, on the integer representation of `03` §4 | **structural test T4 green**, asserting **bit-identity**; byte-identity on every path not using the accumulator | the parallelism licence becomes tested instead of asserted | M–L |
| **8** | **MATTER v0 and the reorder.** Minimal `wear` and `yield`; the matter half of accounting moves before deliberation | **golden-moving by design** — both `balance_oracle` arms plus a full re-pin naming this step; the phase test amended deliberately | the write matrix stops carrying `02` §3's declared interim violation | L |
| **9** | **CENSUS v0.** The Named trigger only — demand-driven mint: *the praefect fines a smuggler and the engine must produce one* | **structural test T3 green**; population moves in a seeded run and the counter accounts for every mint | the population loop closes at its smallest honest scope | M |

> **Nothing in this table is done when its document exists.** Each row is done when its artifact
> exists and someone has looked at it.

---

## §4 · THE FOUR STRUCTURAL TESTS, SPECIFIED

The architecture rests on these four claims. **None has ever been run.** Each is specified precisely
enough to implement, with the falsifier named (§0.1 pt 3) and an assertion that can *observe* the
failure it excludes (§0.1 pt 2) — including asserting that it asserted.

### T1 · No decision function can see the world

**Setup.** Import the module owning `choose` in a subprocess, modelled on the existing
`test_engine_does_not_import_systems.py` probe.
**Assertions.** (a) `inspect.signature(choose)` has no parameter typed or named `world`; (b) an AST
walk over the module finds no reference to the singleton hub, no other global state accessor, and no
read of the event log; (c) **the scanner is proven able to fail** — a fixture module that deliberately
reads the hub is scanned and the test asserts it **is** flagged, plus `assert modules_checked >= 1`.
**Falsifier.** Add a `world` parameter or a hub import — (a)/(b) go red. Delete the fixture — (c) goes
red.
**⚠ Carried caveat.** In GDScript this downgrades to *unreachable-by-name* (`03` §3). **The Python test
is the oracle-side enforcement; the port carries the World-first-argument convention plus the
one-line autoload check instead.**

### T2 · Two witnesses of one event can disagree

**Setup.** One event with two observers of different vantage and marks. Call `witness(p1, e)` and
`witness(p2, e)` — **two calls; the collection signature must not exist to be called.**
**Assertions.** Both return non-empty claim lists — `assert len(c1) and len(c2)`, which observes the
vacuous pass; the claims have **distinct ids** and differ in value or construal; **each deposited only
into its own ledger**, asserted by the other ledger's length being unchanged.
**Falsifier.** Implement `witness` as a broadcast writing one shared claim — the distinct-id assertion
fails. Implement it reading the other ledger — the length assertion fails.

### T3 · A person with no office can act, petition, and receive an opportunity

**Setup.** A minted Person holding zero `hold` Tenures over any Office.
**Assertions.** `opening_set(person, view)` is non-empty (`assert len(openings) >= 1`); it contains
`petition`; a chosen act reaches RESOLVE and produces an Event — **refusal-by-obstacle is legal,
refusal-by-eligibility is the failure** — and `assert resolved_count >= 1`.
**Falsifier.** Gate `opening_set` or the resolver on office-holding; the set empties or the act is
refused, and the test observes exactly that.
**What it encodes.** Office changes whether a decision **binds others**, never whether you may act.

### T4 · Order independence

**Setup.** Six acts against one world snapshot, including **the poison triple** — three `alter`s of
`+0.3, −0.5, +0.3` on one `additive` `[0,1]` field sitting at `0.9` — plus one conflicting pair, an
`efface` racing a `mint` on the same parent.
**Assertions.** Over at least ten permutations of submission order, sampled plus both extremes: the
canonicalized Event list is identical; **the post-state hash is bit-identical — not approximate**; the
conflicting pair routes to `contest` in every permutation; `assert permutations_run >= 10`.
**Falsifier.** Clamp-as-you-go fails the poison triple. A submission-position tie-break fails the
Event-list identity. **Float accumulation without `03` §4's fixed point fails the bit-identity at the
last bit — which is precisely the failure the assertion must be able to see, and which approximate
comparison would blind it to.**

> **`pytest.approx` on an exactness claim is not a weak test, it is an absent one.** This repo has
> already paid for that once, when a one-ulp aggregate error crossed a damage-degree boundary while
> its own identity test passed.

---

## §5 · WHAT MUST NOT BE BUILT

Under `CLAUDE.md` §0.1 point 5, a guard is earned only if the defective artifact is load-bearing on
**the game**, **the exported params**, **the port**, or **a Jordan decision**. Apparatus outnumbers
game code in this repository, so a session reading apparatus finds apparatus defects and mints
apparatus guards — that is the generator, and this predicate is what disarms it.

**Licensed by this suite — two, and only two:**
1. **The `[autoload]` check** (`03` §3): one test asserting `project.godot`'s autoload section contains
   nothing from `core/`. Load-bearing on the port; mechanical; fails on exactly the recurrence.
2. **The contract-tree `--check` round-trip** (`04` §3): the ED-IN-0200 discharge. Load-bearing on the
   exported params the port ingests, and it reuses the pattern already proven seven times.

**Forbidden:** validators over the design documents; freshness checkers; guards on guards; any
apparatus whose subject is this repository's own process rather than the game. **If a defect is found
in an artifact that is load-bearing only on process, that is evidence the artifact can be wrong
without cost — fix it in place, or delete it, and write nothing.**

---

## §6 · THE HONEST SUMMARY

**Step 1 is executable this week and closes a real M1 juncture.** Steps 2–4 discharge a standing Jordan
ruling and put the first person into a game that currently has none. Steps 6, 7 and 9 are the first
time any structural claim in this architecture gets tested rather than argued.

**Until step 1 lands, the correct description of this entire suite — all eight documents — is that it
is prose.** That is not false modesty; it is the standard `CLAUDE.md` §0.2 sets, and the only reason
this document exists is to be the shortest path out of it.
