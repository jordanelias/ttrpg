# THE IMPROVEMENT PLAN — WHAT TO BUILD, IN WHAT ORDER, AND WHAT MAY NOT BE INVENTED WHILE BUILDING IT

## Status: **PROPOSED (2026-09-02). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Scope: **PR #337 → now, for evidence AND for answers.** Every closure in Part 3 is made on #353's
## own text. §2.6 and W16 record what a tree-wide search returns and **the plan rests on none of it.**
## Companion to `ARCHITECTURE_V2.md` (the specification) and `01_NPC_VS_ARC.md` (the split).
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** Under §0.2 **nothing in
## it runs** — **Part 6** names the first thing that would.

---

# PART 0 · WHAT THIS DOCUMENT IS, AND WHY IT IS NOT ANOTHER ARCHITECTURE

`ARCHITECTURE_V2.md` says **what the specification must say.** It ends at §I2 with eight artifacts
and the observation that seven of them cannot be satisfied by writing. **It does not say what to do
on Monday.**

This document is that. It carries seven things and nothing else:

| part | what it is | why it is here |
|---|---|---|
| **1** | the **adjudication** of PR #354 by a structurally-independent read-only critic | a plan built on an unaudited proposal inherits its errors — and it found nineteen holes with no row, eight wrong counts, and three of this chain's own rulings wrong |
| **2** | what was **measured** for this plan, by execution, during its composition | a plan built on remembered numbers is the failure this chain exists to end |
| **3** | the **decision queue** — `CLAUDE.md` §0's five tests, run over the twelve `absent` rows | *"escalate only what survives all five"*, and nobody had run them |
| **4** | **sixteen work items**, each with a deliverable and a DONE-WHEN that executes | §0.2: a juncture is done when the behaviour runs |
| **5** | the **dependency graph** and the **critical path** | six of the sixteen reach the bar; the other ten run beside it |
| **6** | the **first milestone**, named down to the case and the six checks that close it | *"the tested version ran zero cases end to end"* |
| **7–9** | **guardrails**, **what not to do**, and **how to falsify this plan** | the guardrails are what stop the next session repeating this one |

**What this document is NOT.** It is not a new architecture, it does not amend `ARCHITECTURE_V2.md`'s
Parts D–G, and it decides no design question that `V2` left open except by applying `CLAUDE.md` §0's
five tests and reporting what they return. Where a test closes a hole, the closure cites a file and
a line **of #353**. Where no test closes it, the hole stays open and is named.

> ### THE THREE SENTENCES THAT ORGANISE EVERYTHING BELOW
> **1.** `ARCHITECTURE_V2.md` reports **twelve refusals and three escalations**. Run `CLAUDE.md` §0's
> five tests over them, in chain, and **eleven of twelve close or downgrade** — leaving **one
> escalation that blocks nothing**.
>
> **2.** **Nineteen holes have no row at all**, and the register could not say so **because it is not
> an object** — a markdown table nothing reads, whose own counts do not reproduce from its own rows.
> **That is why `W0` is first and everything waits on it.**
>
> **3.** **The tested version ran zero cases end to end.** Every one of the sixteen items is
> subordinate to making that number **one**.

---

# PART 1 · THE ADJUDICATION OF PR #354

A structurally-independent read-only critic (`.claude/agents/valoria-critic.md` — `Read`, `Grep`,
`Glob`, no write tools, so its independence is a property of the agent definition and not of its
prompt) was given `ARCHITECTURE_V2.md`, `01_NPC_VS_ARC.md`, #353 in full, the instrument's source and
the run output, and asked two things: **does V2 survive**, and **what is the plan**. It read #353's
2,068 lines and V2's 830 in full, sampled the instrument with grep over `results.json`, produced no
files, and stated its own coverage and its own null results. Its return is the spine of Parts 4–9.

## §1.1 · The verdict, in one line

> **The architecture survives. The defects are in what `ARCHITECTURE_V2.md` declines to say, and in
> numbers it did not re-derive.** No refusal was weakened; Parts I–VI of #353 are sound in every
> place checked; the determinism control is now honest; no verb was invented beyond `speak` and
> `forge`, which are harmless as `assumption`.

## §1.2 · What it upheld

Eleven of the fourteen retractions in `V2` §0.3 are upheld outright against #353's text — not a
sample, all fourteen were checked. The inheritance of L1, L3 clause 1, Part VIII's refusals whole,
one log, the seam, no per-container clock and fixed point: **uphold.** The 63 honesty tests
reproduce; `A31` does sweep 2 · 5 · 9; `shape_rev1.py` does declare the twelve Partition rows the
first antagonist's finding is about, so the retraction record is verifiable.

## §1.3 · What it overturned — including two of THIS document's own rulings

**This is the relay working, and both corrections are recorded rather than quietly absorbed.**

| item | what I had written | the ruling | why the ruling is right |
|---|---|---|---|
| **H-23** act cost | *"`assumption`, shape only — precedent `march_budget`, cost × magnitude"* | **RULED, and it is a REFUSAL** | #353 `:927-930` verbatim: *"**No cost clause is required. A petition consumes budget like any act, and that is the whole of the pricing.**"* My precedent came from army movement in another subsystem and would have **overturned an explicit sentence of the specification under test.** That is the over-refusal's mirror image and exactly as bad |
| **H-36** refraction side | *"emitter-side, because `Event` has no `target`"* | **RECEIVER-side** | #353 `:668`, `:1286-1288`: every witness **mints its own claim**; the Dispensation is immutable with *"no bare effect field"* (`:719`, `:1283`). **There is no emitter-side object to distort** — distorting one would require a second, mutable Dispensation, which §37.1 forbids. My argument showed the emitter cannot *target*; it did not show the emitter can *distort*, and it cannot |
| **Part E's verb roster** | *"covers every verb #353 names — a verified negative"* | **FALSE** | Part E omits **`establish`** (which `V2` names itself in its own `(Office, remit)` row), **`utter`** (Proposition creation — `commit`, `petition` and `issue` all require a Proposition and no verb makes one), **`exchange`** (`:1899`), and heir designation via `succeed`/`transmission` (`:371`, `:542`). **My check was methodologically broken**: I seeded the candidate list with Part E's own verbs and then looked for extras through a verb-context regex, which is a router, and routers miss — the exact failure §H1 exists to name. **A negative result from a keyword search is not a negative result.** |

## §1.4 · What it found that nobody had — eighteen holes with no row

`V2` §I1 names its own headline falsifier: *"the register is complete — falsified by **a hole an
instrument must fill that carries no row**."* §2.5 of this document fired it twice. **The critic
fired it eighteen times**, each checked against Part D, Part E and Part VII. The ones that change the
critical path:

| # | the hole | why it stops a run |
|---|---|---|
| 1 | **`(Claim, confidence)` decay at MATTER** | the **third licensed clock** (#353 `:864`). Part D has **no `Claim` row at all**, and `(Person, claim_ledger)` is WITNESS-only. **Part D is not total for a clock #353 licenses** — `V2`'s own falsifier at §I1 row 1 |
| 2 | **`(Rung, exists)`, `(Office, exists)`, `(Site, exists)`** | founding a hearth, establishing an office, building a site. Part D's existence rows cover **only `Person` and `Record`** |
| 3 | **`utter` — Proposition creation** | `commit`, `petition` and `issue` all `require` a Proposition to exist. **No verb creates one.** The season cannot start |
| 4 | **Petition, Dispensation and Proposition bypass `write()`** | Part E says *"created, not written"* and *"not a state write"*. #353 `:1061-1064`: *"Either the gate applies the write, or direct assignment is made impossible."* **An object created beside the gate is the unmarked-cell defect wearing a different hat** |
| 5 | **the nine Dispensation term types** | `comply` / `evade` / `defy` write *"per the term's own row"* — **rows that do not exist**, and the nine types are enumerated nowhere in the chain |
| 6 | **the six investigation acts** | T9 makes them first-class; they are **unnamed**, and `V2` grades them `assumption` with `requires: per act` — **nothing to inject** |
| 7 | **the 13 conviction axes** | §F2's `alignment(c.verb, axis)` is a verb×axis table **with no rows**, so H-03's default is not injectable. The "closed 13" appears nowhere in the chain |
| 8–11 | `Coherence` · the `disclosure:` column · `(Person, weight)` · `(Tenure, payload)` | four §54 fold-ins with no Part D row; the last means P39's *"a relationship carries state"* **has no writer** |
| 12 | **what demands an individuation** | H-05 covers world-generation only. NPC-035 blocks on `P20`; ruling the row exists says nothing about **what asks for it** |
| 13 | **`open_case`'s eligibility** | `V2` gates it on `remit:determine`; #353's **closed five remit acts do not include it.** `V2` invented an eligibility, and the alternative (`own`) is a different game |
| 14 | **the View-building rule** | #353: *"at most K ids … **BUILT, not filtered**"*. H-09 supplies `K = 12` and **not which K**; the instrument takes the last k, which is an invention |
| 15 | **question aggregation, and the dropped `need` source** | nothing says how many questions a person forms per season; and #353 `:605`/`:1297` make `need` an **opening source** that §F1 omits, so **an NPC with a standing ambition and a quiet season forms no candidates at all** |
| 16 | **`D22` × `H-33`** | per-write MATTER emissions under **total fan-out** flood every ledger every season and churn the `L=200` eviction. **Two rows that are individually fine and jointly break the log.** No row carries the interaction |
| 17 | the §62 / §54 carry-overs | reaction-inside-a-season vs the seam (`D16`) · may a social quantity sink by neglect · the exchange form · grievance clearance |
| 18 | player/NPC budget symmetry | **already answered** by #353 `:876` (everyone runs `choose`) and **recorded nowhere as closed** |

**Add the one this document found and the critic did not: `A18`, the contract descent (§41)** — no
row, and it is the reason **R-1 and R-2 are unenforceable in principle** while `V2` §0.2 inherits
them unchanged. **Nineteen.**

## §1.5 · The register does not reproduce from its own rows

`V2` §VII.3 says **39 holes · 8 ruled · 13 assumption · 12 absent · 1 mixed.** The tables carry
**H-01..H-12 (12) + H-20..H-39 (20) = 32 rows**; the Tier 0 header says *"Ten holes"* over **12**;
the grade tally sums to **34**. And `V2` §I2's **artifact 0** — *"Part VII has no `absent` row in
Tier 0"* — is **unmet by `V2`'s own `H-02`** and is not marked unmet.

> **The deeper finding, and it is the one that reorganises the work:** `V2` §0.3 row 13 claims the
> register is *"rows, not prose"*. **It is a markdown table that nothing reads.** By §0.05's own test
> — *"if this document were deleted, would the game behave differently?"* — **it is prose.** The row
> shape `V2` §G4 defines requires `site:`, `sweep:` and `cite:`; **not one of the 32 rows carries
> any of them.** That is why **W0 is the first work item and everything else waits on it.**

---

# PART 2 · WHAT WAS MEASURED FOR THIS PLAN

Every number below was produced by running something during the composition of this document, not
recalled from the session it summarises. `CLAUDE.md` §0.1 point 3: a result claim carries the test
that would have shown it wrong. The reproduction command is given for each.

## §2.1 · The instrument is reproducible — and the committed markdown was stale

```
cd proposals/2026-09-01-season-loop-tests/tracer && python3 report.py
```

`results.json` and `TRACE.txt` came back **byte-identical** to the committed versions. That is an
execution artifact under §0.2 and it is the first one this chain has: **the 143-case run reproduces.**
`python3 -m pytest test_tracer_is_honest.py -q` → **63 passed.**

**But six markdown artifacts changed**, because two entrypoints write overlapping outputs:

| entrypoint | writes |
|---|---|
| `run_cases.py.__main__` | `results.json`, `TRACE.txt` |
| `report.py.__main__` | `results.json`, `TRACE.txt`, **and the six markdown artifacts** |

Whoever ran `run_cases.py` last left the markdown a revision behind. Four ARC cases were wrong in the
committed tree:

| case | committed | correct | cause |
|---|---|---|---|
| **ARC-R19** | NOT-ASSESSED, *"blockers: none"* | **BLOCKED**, blockers `F16b` | pre-dates the F16/F16b split |
| **EMG-C2** | a core row PASSing on `F16` | that row is **UNMAPPED** | same |
| **NSC-09** | a core row PASSing on `F16` | that row is **UNMAPPED** | same |
| **SCN-06** | blockers `A27` | blockers **`A27, P17`** | same |

The regenerated artifacts are committed with this plan. **The verdict distribution now agrees across
both emitters for all 143 cases: 76 BLOCKED · 60 NOT-ASSESSED · 4 DEGRADED · 3 PLAYABLE.**

> **This is not a typo class. It is the `CLAUDE.md` §8 invariant — *every rule lives once* — applied
> to artifacts rather than rules: EVERY ARTIFACT HAS ONE WRITER.** Work item **W15**.

## §2.2 · Three published counts were wrong. Corrected here.

| claim | published | measured | where |
|---|---|---|---|
| cases NOT-ASSESSED | **50** | **60** (NPC 20 · ARC 40) | `V2` §H1, `V2` §I1 table, `01_NPC_VS_ARC.md` §5 |
| probe executions | **120** | **121** | `V2` §0.1, `README.md` ×2, `HANDOFF_IN.md` |
| probe PASSes | **62** | **63** | same |
| PASSes raised by a gate, a type or a law | **41** | **43** | same |
| unrouted `core` rows, ARC | 165 | **167** | `UNMAPPED_ARC.md` header |
| ARC verdicts | 52 BLOCKED · 41 NOT-ASSESSED | **53 · 40** | `CASELOG_ARC.md` |
| `core_blocked` summed | 25 NPC · 66 ARC | **26 · 71** | `01_NPC_VS_ARC.md` §1 |
| the 16 / 24 / 29 finding split | *"of 56"* | **sums to 69** — the 29 is the ledger's `no-signature` **probe** count, a different population | `V2` §A2 |

The probe-count row was found by the adjudicating critic and reproduced here independently:

```
python3 -c "import json;p=json.load(open('proposals/2026-09-01-season-loop-tests/runs/results.json'))['_probes'];\
print(len(p), sum(v['verdict']=='PASS' for v in p.values()), \
sum(v['verdict']=='PASS' and v['by']=='construction' for v in p.values()))"
# -> 121 63 43
```

**Every one of these is in the direction that favours the document making the claim**, which is the
signature §0.1 point 4 names — *"a number without a control is not a measurement, in either
direction"* — and none of the eight carried a generating command. **Guardrail G11: every number that
describes the run ships with the command that produces it.**

## §2.3 · The core-row routing rate, stated exactly

| | cases | rows | `core` rows | routed | **unrouted** |
|---|---:|---:|---:|---:|---:|
| NPC | 46 | 346 | 122 | 59 | **63** |
| ARC | 97 | 626 | 300 | 133 | **167** |
| **total** | **143** | **972** | **422** | **192** | **230 (54.5%)** |

**All 60 NOT-ASSESSED cases have zero core blockers.** Nothing about them is refused and nothing
about them is missing; the router simply did not aim. Declared routing (**W2**) makes every one of
the 60 assessable — which is not the same as runnable, and this document does not conflate them.

## §2.4 · THE MEASURED UNBLOCK YIELD — the number this plan is sequenced on

A case is **freed** when *every one* of its blockers is a hole that closed. Set cover over the 76
blocked cases, using `01_NPC_VS_ARC.md` §2.1's probe→hole mapping:

| closing | frees | NPC | ARC | |
|---|---:|---:|---:|---|
| **H-20 alone** | **21** | 5 | 16 | |
| H-20 + H-22 | **33** | 12 | 21 | |
| H-20 + H-22 + H-23 | 37 | 13 | 24 | ⚠ **`H-23` is a REFUSAL, ruled in §3.1 — it frees nothing. Row kept so the raw computation is auditable; see §5.4** |
| **every non-refusal hole** | **54** | **23 — every blocked NPC case** | 31 | |
| **residual** | **22** | **0** | **22** | |

Per-hole marginal freeing: `H-20` **21** · `H-22` **12** · `H-25` 4 · `H-23` 3 · `H-36` 2 · `H-37` 2
· `H-32` 1 · `H-38` 1 · `§36.1` 1 · `H-26` 0 · `H-27` 0 · `H-29` 0. (A hole marginally freeing zero
cases still matters — its cases carry other blockers too.)

> **THIS INDEPENDENTLY CONFIRMS THE 0% / 33% SPLIT BY A DIFFERENT COMPUTATION.** `01_NPC_VS_ARC.md`
> counted core blocks. This is a set cover over cases. **The NPC residual is exactly 0 and the ARC
> residual is exactly 22.** Two computations, one answer: the NPC pathway is blocked entirely by
> holes; a third of the arc pathway is blocked by principle.

**Stated as a ceiling, because it is one:** closing every non-refusal hole *and* declaring routing
leaves at most **121 of 143** cases carrying no refusal blocker. That is an upper bound on
candidate-runnable, not a prediction — new routes reach new refusals.

## §2.5 · `ARCHITECTURE_V2.md`'s own headline falsifier fires — twice

§I1: *"the register is complete — falsified by **a hole an instrument must fill that carries no
row**. This is the falsifier that matters."* All 65 gap records in `results.json._gaps` were checked
against Part VII's 39 rows and Part B's 26 defects. Two survive:

**① `A18` — the contract descent (§41). No row anywhere in `ARCHITECTURE_V2.md`.** The strings
"contract descent" and "S41" appear nowhere in the document. The probe's law:

> *"T5 needs to know PER MODULE what it may RECEIVE; T6 needs to know what it may EMIT; R-2's 'no
> module reaches through another' is the same requirement as a prohibition. **NO SURFACE IN THE
> CHAIN ANSWERS IT FOR ANY MODULE, which means R-1 AND R-2 ARE TODAY UNENFORCEABLE IN PRINCIPLE**,
> not merely unenforced."*

`V2` §0.2 inherits R-1 and R-2 **unchanged** and never says they cannot be enforced. **This is the
most serious of the two**, and it has a live partial answer — see W14.

**② `A14` / defect `D16` — *"no reaction inside a season"* (§34.1) vs the seam's nested DELIBERATE
(§40.2).** Part B says the defects not handled in Parts D–G are *"discharged in… Part VII"*. All 26
were checked. **`D16` is the only one of 26 with no Part VII row.** It is a COLLISION between two
sentences both in chain, and it is claimed discharged.

**And one that RESOLVES — reported so the count is not inflated.** `A27` raises four unowned values.
Three have rows (`season_factor` H-26 · travel legs H-27 · construal spread H-39) and the fourth is
answered by the probe itself (*"the object-side Tenure index — Nobody, by rule, a barrier-built
cache"*). **A27 does not count**, and the temptation to count it is exactly the finding-inflation
`CLAUDE.md` §0.3 names as the generator.

## §2.6 · **NOBODY RAN §0's FIVE TESTS OVER THE TWELVE REFUSALS**

This is the finding that reorganises the plan, and it needs no scope argument at all.

> **`CLAUDE.md` §0, amended 2026-08-24 by Jordan:** before a row is flagged `needs_jordan`, or left
> flagged, a session must try **superseded · irrelevant · answered by a design document · answered
> by precedent · answered by what makes sense for the architecture**. *"Escalate only what survives
> all five."* And, in the same amendment: *"a session that finds a stale `needs_jordan` on a settled
> question is expected to **CLOSE it with its citation**, not preserve it out of caution.
> **Preserving a dead question is not conservatism; it is how a 156-row queue formed.**"*

**That ladder was never run over `ARCHITECTURE_V2.md`'s twelve `absent` rows.** Run in chain, against
#353's own 2,068 lines and nothing else, **it closes or downgrades eleven of the twelve** — including
`H-31`, which `V2` marks *"every contest is blocked"*, and `H-32`, which `V2` §E5 calls *"the single
most consequential `absent` in the document"*. **Part 3 is the result, and every citation in it is a
line of #353.**

### The separate, smaller point about scope — recorded, and load-bearing on nothing

The session's rule — *"any code before PR #337 is to be ignored"* — was **correct and load-bearing
for the TEST**: it is what stopped the instrument inheriting a pre-#337 implementation and reporting
it as the specification's, which is precisely the failure the adversarial passes existed to catch.

A tree-wide search was run **once**, for this plan, and finds live owners for several of the same
holes. **It is reported in `W16` and used for nothing.** Where it agrees with the in-chain reading —
and on the degree ladder the two agree exactly, both giving a margin-read ladder of four bands — that
is corroboration, not a dependency. **The plan would be identical if the search had never been run.**

> **The guardrail this earns is `G6`, and it is narrower than the scope question:** **before a row is
> graded `absent`, §0's five tests are run and their results are written into the row's `cite:`
> field.** A row graded `absent` with an empty `cite:` fails `register.py --check`. That is
> mechanical, it needs no ruling about scope, and it would have caught all eleven.

---

# PART 3 · THE DECISION QUEUE — `CLAUDE.md` §0's FIVE TESTS, RUN OVER THE TWELVE `absent` HOLES

`CLAUDE.md` §0, amended 2026-08-24 by Jordan: *"I don't believe that I need to be involved in the
vast majority of pending decisions."* Before a row is flagged or left flagged, a session must try
**superseded → irrelevant → answered by a design document → answered by precedent → answered by what
makes sense for the architecture**, and *"escalate only what survives all five."*

**Nobody ran that ladder over `ARCHITECTURE_V2.md`'s twelve `absent` rows.** Run in chain, against
#353's own text, it closes or downgrades **eleven of the twelve.**

## §3.1 · Closed — the hole is answered and needs no ruling

| hole | disposition | test | citation, verified |
|---|---|---|---|
| **H-23** act cost beyond budget | **CLOSED — ruled, as a REFUSAL** | 3 | #353 `:927-930`: *"**No cost clause is required. A petition consumes budget like any act, and that is the whole of the pricing.**"* An earlier revision proposed a standing cost and the document **retracts it in place**. ⚠ **This changes a headline number — see §3.5** |
| **H-37** the fault roster | **CLOSED — irrelevant to the season loop** | 2 | #353 `:1929-1933` scopes the twelve named faults to the **deferred social-contest subsystem**, and the seam carries it as a declared extension (`:1403-1409`). `P41`'s needs route to the extension, not to a season-loop row |
| **H-38** does a Person carry a banded scalar | **CLOSED — precedent, and the answer is YES** | 4 | `Site.condition` is the model (#353 `:442-462` — *"an accumulator that reads its own previous value **is** primary state"*, and *"`condition` gates verbs, and that is how damage removes an option"*); bodies are already written at MATTER (`:854`); and **`V2` presupposes the answer in two places of its own** — Part D's `(Person, body)` row and §F3's `condition_penalty(p's body band)`. **Not Jordan's** |
| **H-25** a termination bound | **CLOSED — architecture, with a `measured` obligation** | 5 | It is an **argument**, not a value. L5's second paragraph (#353 `:183-192`): *"every clock that moves such a quantity — other than the three the world already licenses — **was set by a nameable act**, so it can be bribed, delayed, burned, or killed."* **Every cross-season feed is a budgeted act by a person; a spiral nobody feeds stops.** Obligation: a seeded N-season run of a spiral case in which the feeding acts cease — **W11** |
| **player / NPC budget symmetry** | **CLOSED — design document** | 3 | #353 `:876` — everyone runs `choose`. `02_SCENE_BUDGET_RULING.md` flagged it as a fork **before** #353 decided it; it has been closed since and recorded nowhere |

## §3.2 · Re-graded — the shape is ruled and only a value is open, so a default may be injected

`V2` §G2's own rule: **the grade decides the behaviour.** `absent` → REFUSE; `assumption` →
inject · declare · **sweep**. Eight rows were graded `absent` that are `assumption` by that rule.

| hole | new grade | shape ruled by | the default to inject |
|---|---|---|---|
| **H-31** the margin model | **assumption** | #353 `:1397-1401`: *"There is **one degree ladder for every scale of the game** — four bands read off the **margin**, never off the obstacle's size. A duel, a debate, a siege and an examination all use it."* | four bands off `margin = successes − obstacle`; **the band edges are the swept triple** |
| **H-32** `judging_set_rule` | **assumption** | shape ruled — a **resolver-side Query** (#353 `:599`) | live holders of a `hold` on an Office whose `remit.acts` includes `determine` **and** whose `scope_rung` contains the sitting's rung; **empty set → the date fires and lapses** (`:837`) |
| **H-33** the five channel predicates | **assumption** | FORMULA ×5, derivable from the presence index (`:1004`) and `hold` Tenures | `co_located` = presence at the subject's rung at the barrier · `post_remit` = holders of an office whose `scope_rung` contains it · `witness_key` = persons named in `changes[]` · `document_key` = holders of a Record whose subject matter names the subject · `chronicle` = holders of a chronicle Record, else nobody. **Sweep: total / presence-only / five** — and **total fan-out must be in the sweep, because it is #353's specified behaviour and therefore the control** |
| **H-26** `season_factor` | **assumption — and it moves to TIER 0** | NUMBER/FORMULA-shaped | constant `1`, swept. ⚠ **Tier 0 because `yield` is the matter economy's only source** (#353 `:855` — *"`yield` — **only here**"*) and H-11 draws subsistence from stores, so **every multi-season run starves without it** |
| **H-20**'s roster | **assumption** | SCHEMA_ROW-shaped by `V2`'s own kinds | the closed 13 (once enumerated — **that enumeration is §1.4 hole 7 and is itself a row**) plus the corpus-asked `suspicion`, `harm_borne`; **never `exposure` bare** (`:1897`) |
| **H-27** travel-leg ownership · **H-28** `budget`'s placement | **assumption by architecture**, not *"ruled by precedent"* | — | see §3.3; and ⚠ `V2` §D4 conflates a Person with its person-kind Rung — #353 `:539` types `contain: Rung → Rung` and `:390-392` keeps the two distinct |
| **H-39** the construal spread | **assumption** | representation choice with one obvious shape | a per-person scalar on the cohort's members |

### §3.3 · One re-grading that also **shrinks an amendment** — `budget`, H-28

`V2` §F3 makes `budget` a **second** non-decision function taking a `World`. #353 `:634` says
`sense()` is *"the **ONE** non-decision function permitted a World"*, and `V2` §0.2 lists §18.2 as
**inherited unchanged**. Both cannot be true, and `V2` §0.3 does not list the amendment.

**The smaller amendment is available and is the one to take.** A Person owns every Tenure whose
subject they are (#353 `:546`, `:730`) — office-holding is the person's own `hold`; `V2`'s own §D4
gives travel legs to the traveller; `(Person, body)` is the person's own state; and
`entrenchment(p, …)` (`:605`) is an **existing person-side Query that reads the asker's own Tenure**.

> **So `budget : (Person, View) → int` stands unchanged, reading own `hold`, own body band, own
> travel legs — and §18.2's *"the ONE"* survives.** `V2` chose the larger amendment and is
> inconsistent with its own §D4. **Take the smaller one. It is not Jordan's.**

## §3.4 · The one that closes conditionally, and the one that escalates

### **H-36 — refraction, emitter- or receiver-side. CLOSE at test 5. Hold back loudly.**

**Receiver-side, by construction of T3.** Every witness **mints its own claim** (#353 `:668`,
`:1286-1288`), and the issuer's Dispensation is **immutable with no bare effect field** (`:719`,
`:1283`). **There is no emitter-side object to distort.** Emitter-side would require a second,
mutable Dispensation — which §37.1 forbids. `refract` as a **receiver act** is the executor's
deliberate re-telling, which is the mechanism the design already has.

| option | cost |
|---|---|
| emitter-side | a second mutable Dispensation — **forbidden by §37.1** |
| **receiver-side** | **none new**; distortion at each WITNESS deposit plus the deliberate `refract` act |

Magnitude stays `assumption`. **Unblocks `F6`, NPC-020 and two arcs.** Per `CLAUDE.md` §2's
loud-exception rule: **close it, and name it as held back in the PR body** so a reviewer who
disagrees can say so. Do not send it to Jordan.

### **H-35 — does a scene equal an act? ESCALATE. It is the only one that survives all five.**

The ambiguity is in **Jordan's own sentence**, quoted in chain: *"i expect a character to get ~5
playable **scenes** per season, **which may mean** that they get ~5 actions."*

| option | what it costs |
|---|---|
| **1 · one scene = one act**, budget 5 acts | simplest; NPC and player run the identical loop; a player season is 5 resolutions |
| **2 · a scene contains 1–3 acts** and costs 1–2 scene actions | a **second budget object** and **a container the loop does not have**; `capacity` moves to the scene |

**Two defensible options leading to materially different games** — §0's definition of a genuine
escalation. ⚠ *(An answer exists in the pre-#337 archive; under this session's scope rule it is a
**subject**, not a reason, and it is not offered as one.)*

> **It blocks nothing on the critical path.** Artifact 2 runs at H-10's integer `5` either way. **Ask
> it; do not wait on it.**

## §3.5 · WHAT THE H-23 RULING DOES TO THE HEADLINE NUMBER — and it must be published

`01_NPC_VS_ARC.md` §1: *"of which design REFUSALS — **0 (0%)** [NPC] · 22 (33%) [ARC]"*, and §2.1
*"**Not one** of the 25 core blocks is a refusal."*

**`P33` — "an act costs more when it is bigger" — is a §26.3 RULING, not a hole.** With `P33`
reclassified (and `F19`, *"a place produces a demand with nobody petitioning"*, which is
substantively an L1/T5 refusal filed under §36.1):

| | published | measured, `P33` a refusal | measured, `P33` + `F19` |
|---|---|---|---|
| NPC blocked cases touching a refusal | **0** | **2** | **3** |
| NPC blocked cases blocked **only** by refusals | **0** | **1** (NPC-089) | **2** (NPC-083, NPC-089) |
| ARC touching a refusal | 22 | **25** | **25** |
| ARC blocked **only** by refusals | — | **17** | **17** |

```
python3 -c "import json;d=json.load(open('proposals/2026-09-01-season-loop-tests/runs/results.json'));\
R={'W10','A3','W13','P38','F3','F16b','P33'};\
print([ (s, sum(1 for c in d[s] if c.get('blockers') and set(c['blockers'])<=R)) for s in ('NPC','ARC')])"
```

> **The qualitative conclusion survives and is sharper; the number `0%` is wrong.** The NPC pathway
> is *overwhelmingly* blocked by holes — 21 of 23 blocked cases have no refusal in them — and the arc
> pathway is *nearly half* refusal-touching. **A claim of exactly zero is the kind of number that
> should have had a control, and §0.1 point 4 says so in both directions.** Two further omissions in
> the same table: `P6` and `P20` block NPC cases (NPC-021, NPC-035) and appear in neither column.

## §3.6 · The residue, and it is small

| | `V2` | after the ladder |
|---|---:|---:|
| `absent` rows | **12** | **1** — `H-02`'s two verb rows, which fall out of **W3** |
| **genuine Jordan escalations** | **3** | **1** — `H-35`, blocking nothing |
| conditional closures held back in the PR body | 0 | **1** — `H-36` |
| **holes with NO ROW AT ALL** | *unknown* | **19** — §1.4 plus `A18` |

> ### THE SHAPE OF THE WORK, RESTATED
> **`ARCHITECTURE_V2.md` reports twelve refusals and three escalations. In chain there is one open
> row, one escalation that blocks nothing, and NINETEEN HOLES WITH NO ROW.** The problem was never
> that the register refused too much. **It is that the register is not an object** — it is a
> markdown table nothing reads, whose counts do not reproduce from its own rows, and which therefore
> could not tell anyone it was missing nineteen entries. **W0 exists because of that sentence.**

---

# PART 4 · THE WORK ITEMS

Sizes: **S** ≈ half a day · **M** ≈ 1–2 days · **L** ≈ 3+ days. **Every proof is an execution**, per
`CLAUDE.md` §0.2, except where marked *(doc)*. Every item names what it discharges so that nothing is
built twice and nothing is believed done because a document says so.

---

## **W0 — MATERIALISE THE REGISTER AS DATA.** *The first item, and everything waits on it.*

**Why it is first.** `V2` §0.3 row 13 claims Part VII is *"rows, not prose"*. It is a markdown table
that nothing reads: **not one of its 32 rows carries the `site:`, `sweep:` or `cite:` fields `V2`
§G4 defines for the row shape**, its self-reported counts do not reproduce (39 claimed, 32 present;
*"Ten holes"* over 12; grades summing to 34), and it could not detect that **nineteen holes have no
row**. By §0.05's own test — *would the game behave differently if this document were deleted?* —
**it is prose.** A plan whose first move is anything else is planning on top of it.

**Do.**
1. Create `proposals/2026-09-02-executable-architecture/hole_register.yaml`, one row per hole in
   `V2` §G4's exact shape — `id · hole · kind · owner · grade · default · site · sweep · unblocks ·
   cite` — carrying **the 32 existing rows, the 19 holes of §1.4 + `A18`, and the four §62/§54
   carry-overs**.
2. Write `proposals/2026-09-01-season-loop-tests/tracer/register.py` with a blocking `--check` that
   fails on: any row with no `grade`; any `assumption` row lacking `site:` or three `sweep:` points;
   **any `absent` row that carries a `default:`** (that is §42.2.1's whole content, made mechanical).
3. In the same commit, correct in `V2`, `README.md` and `HANDOFF_IN.md`: **121 / 63 / 43**, the
   NOT-ASSESSED **60**, the `core_blocked` **26 / 71**, the §D20–§D26 citations (they are Part B row
   ids, and Part D has only §D1–§D5), and **mark `V2` §I2's artifact 0 UNMET**, which it is.
   > ✅ **PARTLY DISCHARGED IN THIS COMMIT.** The **121 / 63 / 43** and **NOT-ASSESSED 60** counts are
   > corrected in `V2` and `README.md`, and `01_NPC_VS_ARC.md` §1 carries a **marked correction** for
   > the `0%` claim and the three circulating `core_blocks` totals. A wrong number left standing
   > while a plan says it is wrong is the worst of both, so these were fixed rather than filed. What
   > `W0` still owes: the citation form, artifact 0's UNMET marking, and **the register as data**,
   > which is the part that matters and which no edit to a markdown table can deliver.

**Discharges.** `V2` §0.3 rows 13–14 · §VII.3's counts · the precondition for artifact 0 · **G11**.

**Proof.** `python tracer/register.py --check` exits 0 and **prints the computed counts** (so the
counts can never again be a hand-typed sentence); planting a row with no `grade` makes it exit 1;
planting a `default:` on an `absent` row makes it exit 1.

**Size S.** Depends on nothing.

---

## **W1 — RE-GRADE AND CLOSE BY THE FIVE TESTS.** *Part 3, executed as edits to the register.*

**Do.** Apply §3.1–§3.4 as row edits: close `H-23` (as a **refusal**), `H-37` (irrelevant), `H-38`
(precedent, **yes**), `H-25` (architecture + a `measured` obligation), the budget-symmetry row;
re-grade `H-20`/`H-26`/`H-27`/`H-28`/`H-31`/`H-32`/`H-33`/`H-39` to `assumption` **with the defaults
of §3.2 written into `default:` and three points into `sweep:`**; close `H-36` receiver-side and
**mark it held back in the PR body, loudly, per `CLAUDE.md` §2**; leave `H-35` escalated.
Move `H-26` **to Tier 0**.

**Discharges.** Eleven of twelve `absent` rows · `D9`, `D11`, `D13`, `D15`, `D18`, `D19`, `D24`,
`D25`.

**Proof.** `register.py --check` green **with Tier 0 containing no `absent` row** — which is `V2`
§I2's **artifact 0**, and the only one of the eight that writing can satisfy. Every closed row's
`cite:` resolves to a line that says what the row claims (spot-check by a critic, not by the author).

**Size S–M.** Depends on **W0**.

---

## **W2 — PART D AS DATA, AND `write()` READS IT.**

**Do.** `write_matrix.yaml` — `kind · field · steps · class · social · by · emits`. Replace
`WRITE_MATRIX`, `WRITE_CLASS_OF`, `PARTITION`, `PARTITION_ASSUMED`, `MATRIX_FIELD_OF` and
`PARTITION_MISSING` in `tracer/shape.py` with a loader. **Add the missing rows §1.4 names:**
`(Claim, confidence)` at MATTER · `(Rung|Office|Site, exists)` · `(Petition|Dispensation|
Proposition, exists)` in the ACTS class **so creation stops bypassing the gate** · `(Person, weight)`
at CENSUS · `(Tenure, payload)` · `(Person, coherence)` **via the seam only**. Fix `(Date, due_at)`
— it is marked CAL and *"true at RES"* on a column L4 says is **static**, and `due_at` is written
only by `convene`, so CAL should be `·`. Mark the three former `PARTITION_ASSUMED` rows `by: DR-3`.
**Retire the dead rows** — `(Person, capability)`, `(Person, marks)`, `(Rung, stake)`,
`(Site, drawers)`, `(Office, establishment)`, `(Office, remit)` carry `emits:` kinds **no Part E verb
produces**.

**Discharges.** `H-01`, `H-22`, `H-24`, `D1`, `D7`, `D8`, and §1.4 holes 1–4 and 8–11.

**Proof.** `ASSUMPTIONS.md` regenerates with **zero assumed Partition rows**; a test **walks the AST**
of `shape.py` and asserts every `w.write(...)` call site names a `(record_kind, fieldname)` present
on the table — *walk the tree, do not grep the string*, which is **G3**; a planted `(Person, mood)`
write raises `Unspecified` **with the pair named**.

**Size M.** Depends on **W0** for grades; may start against a stub table.

---

## **W3 — PART E AS DATA, AND ONE `resolve` READS IT.** *The item that turns grading into running.*

**Do.** `verb_table.yaml` in §E2's shape. **Remove the `effect` parameter from
`SeasonDriver.resolve`.** The fold becomes: eligibility (`own | remit: | hold: | presence:`, **never
`capability`**) → `requires` evaluated **against the world the predecessors left** → each `writes:`
through `write()` → `emits` or `emits_on_refusal`. **Add the verbs #353 names and Part E omits:**
`utter` (**without it no Proposition exists and `commit`/`petition`/`issue` cannot fire**),
`establish` (which `V2` names in its own `(Office, remit)` row), `exchange`, and heir designation via
`succeed`/`transmission`. Give `tell` a **refusal event** — it has a `requires` and no refusal, against
§E2's *"failure emits, never raises"*. Move `restore`'s **effect formula out of its `requires`
column**. Mark `open_case`'s eligibility `assumption` with `own` as the swept alternative — **`V2`
gated it on `remit:determine` and #353's closed five remit acts do not include it.**

**Discharges.** `H-02`, `D20`, §1.4 holes 3, 5, 6, 13.

**Proof.** `P8` and `F17` re-run **with no lambda**; a planted verb writing a field outside its
`writes:` raises; **`transfer` twice from a one-unit larder yields `transfer.made` then
`transfer.refused`** — scarcity falling out of the fold, which is §E4's property and #353 `:970-976`;
`grep -c "effect(" shape.py` is **0**.

**Size M–L.** Depends on **W2**.

---

## **W4 — MATTER EMITS PER WRITE, WITH CAUSES.**

**Do.** Every MATTER write emits its `emits:` kind; a band crossing's `causes[]` **names the wear
Events**; `(Claim, confidence)` decays at MATTER and emits; **`[ROOT]` only for the campaign seed and
a licensed clock's genuine first emission** (#353 `:682-685` — the carve-out `V2`'s `D22` treats as a
defect, which is why the row must say which write emits which kind rather than that MATTER emits
nothing).

**Discharges.** `H-12`, `D22`, §1.4 hole 1.

**Proof.** A seeded 2-season run in which a `condition.band_crossed` Event's `causes[]` **walks to**
`condition.worn` Events; **the count of `[ROOT]` after season 1 equals the number of declared roots
and nothing else** — asserted, not printed, which is **G3**.

**Size S–M.** Depends on **W2**. Parallel with **W3**.

---

## **W5 — PART F: THE PERSON'S DECISION.**

**Do.** `q` from **four** sources, not three: Q1 a Date due · Q2 a claim landing · Q3 a subsistence
band · **Q4 `need`** — a live `commit` to an OUGHT Proposition generates a standing question each
season (#353 `:509`, `:605`, `:1297`). **Without Q4 an NPC with a standing ambition and a quiet
season forms no candidates at all**, which is most of the NPC corpus. `opening_set(p, view, q)`
computed from `verb_table.yaml` — **remove the `roster` parameter**, which is `D2` entire. `choose`
scores with an `alignment` table **registered as its own `assumption` row** (§1.4 hole 7: the closed
13 axes are enumerated nowhere, so the table is a row before it is a formula). **`budget(p, view)`
person-side**, reading own `hold` Tenures, own body band, own travel legs — **the smaller amendment
of §3.3**. `standing` with a **defined predicate vocabulary and a defined `agreement`** — `V2`
§F4's `agreement(claims, convictions)` is undefined and compares the TRUE layer with the RIGHT layer
that #353 `:352-362` calls *"the most dangerous collision in the design"*, so **H-29's default is not
injectable as written**. A **View-builder rule row**: #353 says *"at most K ids … BUILT, not
filtered"*; `K = 12` says nothing about **which** K, and the instrument takes the last k.

**Discharges.** `H-03`, `H-04`, `H-28`, `H-29`, `D2`, `D3`, `D4`, `D21`, §1.4 holes 7, 14, 15.

**Proof.** `Query.opening_set` has **no `roster` parameter**; probe `P12` flips from `probe-model` to
`construction`; the `alignment` table swept at three points **with every flipped verdict printed**;
and **`sense()` remains the only World-taking non-decision function — asserted by AST over every
person-side function's signature**, never by reading the docstring.

**Size M–L.** Depends on **W3**.

---

## **W6 — WITNESS CHANNEL PREDICATES, AND LEDGER FLOOD CONTROL.**

**Do.** The five defaults of §3.2's `H-33` row. **Sweep: total / presence-only / five.**

**Why it is not optional once `W4` lands.** `D22` (MATTER emits per write) and `H-33` (`absent`, so
fan-out is total) are **individually fine and jointly fatal**: every `condition.worn` and
`stores.changed` reaches **every** ledger **every** season and churns the `L = 200` eviction. **No row
in `V2` carries that interaction.** It is §1.4 hole 16 and it is the cleanest example in the corpus
of a defect that only appears when two rows are read together — which is an argument for the register
being a queryable object rather than a table a human reads a page at a time.

**Discharges.** `H-33`, `D14`, §1.4 hole 16.

**Proof.** `P15` flips to PASS **by construction**; deposits per season fall from `N × E` to a number
**the sweep reports**; a `tell` reaches **only the told**.

**Size M.** Depends on **W2** and **W4**. Parallel with **W5**.

---

## **W7 — THE SITTING DECIDES, AND THE CONTEST RETURNS A DEGREE.**

**Do.** `H-32`'s default so **`determine` executes** — *nothing is decided at a sitting* until it
does; `H-31`'s default so `contest()` **returns a band** instead of raising; the demote-only veto
typed as `bool` and nothing else (#353 `:1411-1414`).

**Discharges.** `H-31`, `H-32`, `D11`, `D13`.

**Proof.** `F8`, `F21`, `A7` flip; **a vacant date fires and lapses**; a nested contest at
`max_depth` still returns `ContestError`; the three-point sweeps reported.

**Size M.** Depends on **W3**. Parallel with **W5** / **W6**.

---

## **W8 — THE MATTER ECONOMY RUNS.**

**Do.** `season_factor` (`H-26`) as a params row, default `1`, swept; **`yield` at MATTER**;
subsistence (`H-11`) and per-kind wear and floors (`H-07`/`H-08`) as **registry rows rather than
`DEFAULT_FIXTURES` literals in the instrument body**.

**Proof.** A **10-season seeded run in which stores neither monotonically deplete nor overflow** —
the control that catches a starving world, which is what H-26 blocked; `W5` flips.

**Size S–M.** Depends on **W2**.

---

## **W9 — ARTIFACT 2: ONE NPC SEASON, END TO END.** ⭐ **THE BAR.** See Part 6.

**Size M.** Depends on **W0–W5**. **`W6`, `W7`, `W8` are NOT required.**

---

## **W10 — DECLARED ROUTING FOR THE 143 CASES.** *(artifact 7)*

**Do.** Every `season_requires` row gains **`exercises: [<verb> | <contract §> | <H-id>]`, authored
with the row**. Delete `ROUTES*` and `COMPILED` from `run_cases.py`; **`route_precision.py` retires
with them** — a guard for a thing that no longer exists is the apparatus this repo's §0.3 is about.
**NOT-ASSESSED then means *"nobody authored an `exercises:`"*** — a fact about authoring, which is
fixable — instead of *"the regex missed"*, which is not.

**The measured size of the job: 230 of 422 `core` rows (54.5%) never routed**, and **all 60
NOT-ASSESSED cases have zero core blockers**, so every one of the 60 becomes assessable. It is
**~973 rows** across both case directories.

**Discharges.** §H1 and **the entire bare-token class** — structurally, by deleting the router,
rather than by enumerating another word.

**Proof.** `results.json` regenerates with **zero regex routes**; the run prints, per case, **which
declared verbs executed**; **no PLAYABLE verdict rests on a row with an empty `exercises:`.**

**Size L.** Depends on **W3** for the vocabulary. A parallel lane thereafter.

---

## **W11 — THE DETERMINISM ARTIFACTS.** *(artifact 4; #353 §66 items 4–5)*

**Proof.** `headless.py --seed 0 --seasons 2` twice → **byte-identical hash**; **the float arm
produces a DIFFERENT hash** (the control must fire — this is the failure `V2` §A2 records as the
session's worst, a control that printed `differing=False` and asserted it had fired); serial versus
pooled DELIBERATE identical. **Plus `H-25`'s obligation**: a seeded N-season spiral case in which the
feeding acts cease **and the spiral stops**.

**Size S.** Depends on **W4**.

---

## **W12 — ARTIFACT 8: THE TWELVE TRAJECTORY TRANSITIONS AS EXECUTABLE CASES.**

**The only supplied acceptance set in the chain, and a runner has still never run it.** This session
ran 143 cases it authored and **not the twelve that were given to it.**

**Proof.** The score **re-derived by a run** — #353 §66 item 10 says *"the chain says five of twelve
work; a runner has never confirmed it"*, so a run reproducing five is evidence and one reproducing
twelve is a bug.

**Size M.** Depends on **W9** and **W7**.

---

## **W13 — THE ARC RE-AUTHORING LANE.** *Not a specification change. Do not confuse the two.*

**The exact list, computed rather than estimated** (`results.json` blockers; reproduction command in
§3.5):

| | arcs |
|---|---|
| **refusal-ONLY — 14.** Re-author; **no specification work will help** | `ARC-01`, `ARC-13`, `ARC-R16` *(a faction acts)* · `ARC-R17`, `ARC-43`, `ARC-44` *(a settlement holds a mood)* · `ARC-R19` *(a pooled social quantity)* · `ARC-20` *(a clock nobody wound)* · `ARC-24`, `ARC-47`, `EMG-10`, `SCN-02` *(a counter ends the story)* · `SCN-13`, `SCN-15` *(a referee)* |
| **MIXED — 8.** Need a hole closed **first**, then re-authoring. **Re-authoring alone will not free them** | `ARC-03`, `ARC-05`, `ARC-11`, `ARC-22`, `ARC-23`, `ARC-55`, `SCN-07`, `SCN-LOOP-C` |

**Do.** Re-express so that **a counter compels a named person** (#353 `:192-195`) through §36.3's
petition chain and §37's dispensation-as-`tell` — the shape **19 of 50 surveyed arcs were already
asking for**. Each rewritten row declares its `exercises:`.

**Proof.** Re-run under **W10**; **a re-authored arc that still routes to `A3`/`W10`/`W13`/`P38`/
`F3`/`F16b` is a defect in the re-authoring, not in the design.**

**Size L.** Authoring may start after **W1**; **validation depends on `W7` and `W10`**, because the
petition chain ends at a sitting and a sitting does not decide until `H-32` has a default.

---

## **W14 — THE GODOT PORT ARTIFACTS.** *(#353 §66 items 1, 3, 6)*

**Observation only. Not on this plan's path. Do not start before `W9`.** Named so that a reader does
not mistake its absence for an oversight.

---

## **W15 — ONE WRITER PER ARTIFACT.** *(the defect of §2.1)*

**Do.** Delete the `results.json` / `TRACE.txt` writes from `run_cases.py.__main__`, or make that
entrypoint refuse to write. `report.py` becomes the sole emitter. Commit the regenerated artifacts.

**Proof.** Running either entrypoint leaves the six markdown files and `results.json` **mutually
consistent**; a test asserts the caselog's per-case verdict equals `results.json`'s for all 143.

**Size S.** Depends on nothing. **Do it first, with `W0`** — it costs half an hour and it is why four
ARC cases were wrong in a merged PR.

---

## **W16 — THE SCOPE QUESTION, PUT ONCE AND NOT ACTED ON.** *(doc)*

**This is the only item in the plan that asks rather than does, and it does not block anything.**

The session's scope rule — *"any code before PR #337 is to be ignored"* — was **correct and
load-bearing for the test**: it is what stopped the instrument inheriting an implementation and
reporting it as the specification's. Everything in Parts 3–4 above is decided **inside** it.

But a search of the tree, run once for this plan and **used for nothing in it**, finds that several
holes have live owners outside the chain — among them a **margin-based degree ladder that is the
single owner for every scale of the game by a 2026-08-14 Jordan ruling**
(`engine/autoload/dice_engine.py::degree_from_net`), a **closed four-item `ethical_axis` roster** and
a registered `personal_track` kind (`references/descriptor_registry.yaml`), a **`## Status: CANONICAL`
13×4 Conviction→axis matrix** (`systems/characters/conviction_axis_matrix_v30.md`), a **live
adjudicator taxonomy with a Panel decision rule** (`systems/social_contest/`, ED-137/ED-1057), and a
`Visibility` block with an enforced three-shape invariant (`engine/substrate/keys.py`).

**Two facts sit against each other and neither may be suppressed:**

- **`CLAUDE.md` §0.05 (Jordan, 2026-08-24):** *"we rely on code ONLY for the game work"* — **the code
  is the mechanism**, and §0's five tests direct a session to answer from precedent and architecture
  before escalating.
- **The session's scope rule**, given twice, which says pre-#337 work may not be referred to.

**The plan resolves it conservatively and does not need a ruling to proceed:** every closure in
Part 3 is made **in chain**, on #353's own text, and **not one of them rests on the paragraph above.**
Where the two agree — and on the degree ladder they agree exactly, both giving a margin-read ladder
with four bands — that is corroboration, not a dependency.

**What is genuinely open is whether the eventual engine has ONE ladder or two.** #353 `:1397`
says *"there is one degree ladder for every scale of the game"*; `dice_engine.py` says *"single owner
for every scale of the game"*. **Two documents, each claiming to be the only one.** That is a real
question for whenever the port begins — **and it is not on the critical path, so it is asked here and
left.**

---

# PART 5 · SEQUENCE, INTERDEPENDENCIES AND THE CRITICAL PATH

## §5.1 · The critical path — six items, and they are hard blocks

```
W0 ──▶ W1 ──▶ W2 ──▶ W3 ──▶ W5 ──▶ W9
(register  (re-grade  (Part D   (Part E   (the        (ARTIFACT 2:
 as data)   by the     as data)  as data,  person's     one NPC season,
            5 tests)             one       decision)    end to end)
                                 resolve)
```

**Why each edge is a hard block and not a preference:**

| edge | why it cannot be reordered |
|---|---|
| **W0 → W1** | a re-grade that is not written into a checkable row is a paragraph. The whole failure of `V2`'s register is that its grades live in prose |
| **W0 → W2** | every new Part D row needs a **grade**, and #353's polarity rule (`:1576-1578`) **fails an ungraded row** rather than defaulting it. Adding rows before there is a grader inverts the polarity |
| **W2 → W3** | every verb's `writes:` cell **must be a Part D row** (§E2). A verb table over a matrix that does not carry `(Proposition, exists)` cannot express `utter` |
| **W3 → W5** | `opening_set` is **computed from the verb table**. That is the whole of `D2`: option sets stop being authored the moment the verb table exists, and not before |
| **W5 → W9** | without a computed `q` the season is **graded, not run**. This is the distinction the entire session failed to cross |

**Everything else is off the path.** `W6`, `W7`, `W8`, `W10`–`W14` do not block artifact 2.

## §5.2 · What runs in parallel, and the condition that makes it safe

| lane | after | touches |
|---|---|---|
| **W4** MATTER emits | W2 | the MATTER step body |
| **W6** witness predicates | W2 + W4 | the WITNESS step body |
| **W7** sitting + contest | W3 | the seam and `determine` only |
| **W8** matter economy | W2 | MATTER + the fixtures registry |
| **W10** declared routing | W3 | the case corpus and `run_cases.py` |
| **W13** arc re-authoring | W1 *(authoring)*; W7 + W10 *(validation)* | the arc corpus only |

> **The condition, and it is the whole reason these are safe:** **the YAML tables are the only shared
> surface, and each lane APPENDS rows rather than rewriting them.** A lane that edits another lane's
> rows is not a parallel lane; it is a merge conflict with a schedule. `CLAUDE.md` §10's
> `isolation: worktree` rule applies if these are run as agents.

## §5.3 · The long pole, and why it is not the critical path

**`W10` is the long pole for measured improvement on the NPC pathway** — 973 rows, and until it
lands **60 of 143 cases stay NOT-ASSESSED for a reason that is about the router, not the design**,
so no re-run can show how far Parts D–F actually clear the pathway.

**It is still not on artifact 2's path**, because artifact 2 is **one** case whose `exercises:` are
authored by hand as part of `W9`. **Start `W10` the moment `W3` fixes the verb vocabulary, and run
it beside the path, never in front of it.**

## §5.4 · The measured payoff of each stage — so the sequence can be argued with

Set cover over the 76 blocked cases (§2.4). **A case is *freed* when every one of its blockers is a
hole that closed.** This is what the sequence is buying, stage by stage:

| after | frees | NPC | ARC | note |
|---|---:|---:|---:|---|
| `W1` closes `H-20`'s roster | **21** | 5 | 16 | the largest single row in the corpus |
| + `H-22` (`W2`'s Record rows) | **33** | 12 | 21 | |
| + `H-23` — **now a REFUSAL, so it frees nothing** | 33 | 12 | 21 | ⚠ `V2` counted this as 3 cases of upside. **It is 3 cases of correctly-priced refusal** |
| + every remaining non-refusal hole | **54** | **23 — every blocked NPC case** | 31 | |
| **residue** | **22** | **0** | **22** | `W13`'s lane, and no specification change touches it |

⚠ **Freed is not runnable.** A freed case has no blocker; whether it *runs* depends on `W10` giving
its rows an `exercises:` and on Parts D–F being total for what they exercise. **The honest ceiling is
121 of 143 cases carrying no refusal blocker**, and that is an upper bound, not a forecast: new
routes reach new refusals, and §1.4's nineteen rowless holes are where they will reach them.

## §5.5 · What is NOT sequenced here, stated so its absence is deliberate

- **`W14`, the Godot port.** #353 §66's items 1, 3 and 6 are untouched by `V2` and by this plan.
- **The 22-arc residue's design implications.** `01_NPC_VS_ARC.md` §2.2 is right that no
  specification work unblocks them; whether the *design* should change to accommodate them is a
  question this plan does not raise and does not answer.
- **`H-35`.** Asked in §3.4, blocking nothing, and the plan proceeds at `budget = 5` acts either way.

---

# PART 6 · THE FIRST MILESTONE — ARTIFACT 2, IN FULL

> ### **THE TESTED VERSION RAN ZERO CASES END TO END. ONE IS AN INFINITE IMPROVEMENT OVER ZERO, AND IT IS THE ONLY NUMBER THAT WOULD PROVE ANY OF THIS.**

## §6.1 · The case: **NPC-088, Carin Vedel, the copyist**

**Chosen on four grounds, all checkable:**

1. **#353 §13.1 already narrates her season as the worked lawful case.** The specification's own
   example is the cheapest possible first execution: if it does not run, the failure is unambiguous.
2. **Her only routed blocker is `P22` → `H-22`**, which Part D rules. Nothing about her needs a
   ruling that does not exist.
3. **Her needs exercise the largest number of ruled rows**: a Record created with **act-declared
   stages**, MATTER **maturation** whose Event names her act as its cause, a `hold` on a Record,
   and `(Person, exists)` as an ending.
4. **She needs no sitting (`H-32`), no contest (`H-31`) and no dispensation (`H-36`)** — the three
   places where a default is still being injected. **Her season is the one that tests the loop
   rather than the defaults.**

**Second case if she fails for a reason about her own rows rather than about the shape:** **NPC-033,
Kolbrun Thale.**

## §6.2 · The minimum work-item set

**`W15` · `W0` · `W1` (only the rows `W9` touches) · `W2` · `W3` (verbs `create_record`, `move`,
`tell`, `transfer`, `destroy_record`, `kill`, plus **`utter`**) · `W4` · `W5` (Q2 and Q4 sources; a
**non-zero** `alignment` default; person-side `budget`).**

**`W6`, `W7` and `W8` are not required.** The `H-33` default at this milestone is **total fan-out** —
declared as such in the register with `site: witness.fan_out` and `sweep: [total, presence, five]`.
That is **honest** (it is #353's specified behaviour), it makes the log walk, and it is exactly what
`V2` §G's inject-declare-sweep doctrine is for.

## §6.3 · What proves it done — six checks, all executions

| # | check |
|---|---|
| **1** | `python tracer/headless.py --case NPC-088 --seasons 2 --seed 0` prints a content hash. **Run twice: byte-identical.** |
| **2** | The log contains, **in `causes[]` order**: `record.created` *(causes: her act)* → `term.matured` at MATTER *(causes: `record.created`)* → a claim deposited in another person's ledger → **that person's Q2 question** → **their act** → `news.told` \| `record.destroyed` \| `person.died`. **A chain of at least four Events walks from her act, with no `[ROOT]` after the seed.** |
| **3** | **The fixture-read log names only sites present on `hole_register.yaml`.** Zero fills off the register — `V2` §G's central claim, made falsifiable. |
| **4** | `resolve` was called **with no `effect` lambda**, and `opening_set` **with no roster**. |
| **5** | Her `season_requires` core rows each carry an `exercises:` **written before the run and not edited after it**, and each declared verb's `emits:` kind appears in the log with `causes[]` walking back to her act. Her **three currently-unmapped core rows** resolve to a verb with eligibility `hold:<record>`, a Q2 question in another person, and a Record stage — **or are recorded NOT-ASSESSED with the reason.** |
| **6** | **The A5-style float control still fires.** `W11` may follow, but the float arm must not have been removed to make the run clean. |

> **Check 2 is the one that cannot be faked, and check 5 is the one that stops the author moving the
> goalposts after seeing the result.** The session this plan follows failed at exactly that seam:
> it graded cases against probes it had written, and the probes were the model.

---

# PART 7 · THE GUARDRAILS

**A guardrail here is a rule with (a) the specific failure that earned it and (b) a check that fails
on recurrence.** `CLAUDE.md` §0.1 point 5, as amended: **a guard must earn its existence** — it is
licensed only where the defective artifact is load-bearing on the game or on a Jordan decision. Every
guard below lives **inside the instrument directory**, because the instrument's output is what an
adoption decision would rest on. **None goes under `tools/`.** That distinction is the whole of the
amendment and it is not negotiable.

## §7.1 · The global guardrails

| id | rule | the failure that earned it | the check |
|---|---|---|---|
| **G1** | **A fill off the register is a red test.** The instrument reads a default **only** through `register.py` | **24 avoidable inventions across four revisions** | the run's fixture-read log is a **subset** of the register's `site:` list; any other numeric or structural literal in a body is a defect. `Fixtures.get` already raises `Ungraded` on an unregistered number — **extend the same polarity to schema rows, formulas and producers** |
| **G2** | **No route decisive on a single common word.** Forbid the **shape**, never enumerate the words | **five recurrences**; the whitelist built for the fourth did not catch the fifth (`age\w*` matching AGENT/AGENCY/AGENDA), and a **sixth** is in §7.4 | until `W10`, `route_precision.py`'s audit returns an empty offender list at every commit. **After `W10` there is no router — delete the module rather than keep a guard for nothing** |
| **G3** | **A test asserts the PROPERTY, never the string** | a control that computed `differing=False` and asserted in the same sentence that it had fired; a pin on `stated == [one row]` when the head states two | two worked replacements: the Partition pin becomes *"every non-derived row carries a chain citation"*; `assert "assert float_differs" in src` becomes **`assert fa != fb and ia == ib`, called directly** |
| **G4** | **An over-refusal is a defect of EQUAL WEIGHT to an invention** | `F16` refused a faction treasury under L3 and **survived all four adversarial passes**, costing **ten arcs**; and this document's own `H-23` reading would have overturned an explicit sentence of #353 | every `Forbidden` raised at a new site **names the law and cites the section**, and a critic pass on `W2`/`W3` **must attempt the opposite reading for each new refusal** |
| **G5** | **An adversarial pass EDITS THE THING UNDER REVIEW** | the 224-line findings ledger is, by `V2`'s own account, the **fifth T3 instance** | output is edits to the YAML/Python plus **one paragraph in the commit message**. No findings file, no report directory, **no sixth ledger** |
| **G6** | **The scope rule binds the INSTRUMENT, not the REGISTER** | eleven of twelve `absent` rows are answerable **in chain** and nobody ran the ladder; separately, the tree answers several of them outright | before any row is graded `absent`, §0's five tests are run **and their results recorded in `cite:`**. A row graded `absent` with an empty `cite:` fails `register.py --check` |
| **G7** | **One writer per artifact** | four ARC cases were **wrong in a merged PR** because two entrypoints wrote overlapping outputs | a test asserts the caselog's per-case verdict equals `results.json`'s for all 143 |
| **G8** | **Every defect gets a register row, or is discharged with a named section** | `D16` is the only one of 26 defects with **no Part VII row and no Part D–G discharge**, and was claimed discharged | `register.py --check` fails on a Part B row id that appears in neither the register nor a discharge map |
| **G9** | **No new guard, validator or dashboard outside the instrument directory** | `CLAUDE.md` §0.3's whole diagnosis: 1,718 lines guarding the prelude of the scripts that run the audits | a new file under `tools/` in a commit on this lane is rejected at review |
| **G10** | **Never average the two pathways again** | a single headline over 143 cases hides that one set is blocked by silence and the other by principle | any reported figure carries the NPC and ARC columns separately, **or is not reported** |
| **G11** | **Every number describing the run ships with the command that produces it** | **eight published counts were wrong** (§2.2), every one in the direction favouring the document making the claim, and not one carried a generating command | a number in a document with no adjacent reproduction command is a defect at review |

## §7.2 · The per-item guardrails

| item | binding rule |
|---|---|
| **W2** | an `emits:` kind with **no producing verb and no MATTER site** is a red row (six such rows exist today and are listed in `W2`). The `social:` column **stays two-valued**; the INTERIOR row carries `by: DR-3, note: step-confined` rather than a third value |
| **W3** | every verb's `eligibility` is one of the four kinds and **never `capability`** — assert **over the table**, not over the prose. **No verb exists only for office-holders.** A verb needing behaviour the columns cannot express is **`grade: absent`, never a special case** — that is precisely where a second resolver would enter the design |
| **W4** | the `[ROOT]` count is **asserted, not printed** |
| **W5** | `choose` receives **no World** — assert by signature. The engine **never truncates** an over-budget act list; it raises. ⚠ **The `alignment` default must not be a zero matrix** — a zero matrix makes convictions inert, which is the dead-carrier defect #353 `:739-744` names, and it would pass every test while meaning nothing |
| **W6** | **the sweep MUST include total fan-out**, because that is #353's specified behaviour and therefore the **control** against which any predicate is measured |
| **W7** | the veto returns `bool` and nothing else |
| **W9** | the case's `exercises:` are **written before the run and not edited after it** |
| **W13** | a rewrite that introduces a settlement mood, a clock nobody wound, a referee, or a faction as an actor is **rejected at review** — grep the refusal probes. The *"counter compels a named person"* shape **must name the person** |

## §7.3 · The one guardrail this document is itself under

**`G5` binds this plan.** The temptation, having found nineteen rowless holes and eight wrong counts,
is to write a findings document about it. **This document is not that**: every finding above lands as
a work item, a register row, or a correction to be made in the same commit. **The only new files this
plan licenses are `hole_register.yaml`, `write_matrix.yaml`, `verb_table.yaml` and `register.py` —
three data files and one checker, all of which the game reads.**

## §7.4 · The sixth recurrence of the bare-token class, found while writing this plan

`F16`/`F16b` were split so that pooled **material** is lawful and pooled **social** is refused.
`F16b`'s routes require one of `loyalty | unrest | legitimacy | morale | standing | cohesion`.

Two core rows — `EMG-C2`'s *"campaign-wide **institutional threat value**"* and `NSC-09`'s *"shared
**institutional-threat value**"* — are **the same L3 refusal** and route to **nothing**, because
**`threat` is not on the list**. They fell silently to UNMAPPED when the split narrowed `F16`.

> **The ARC refusal count is therefore a FLOOR, not a total** — and the fix is **not** to add
> `threat`. Adding the word is what was done at recurrences two, three and four. **The fix is `W10`:
> delete the router.** This is `G2` firing on this document's own evidence base, and it is the
> cleanest possible argument for declared routing: **a roster of words IS a specification, and nobody
> ratified this one.**

---

# PART 8 · WHAT NOT TO DO

**Each of these is a thing a competent session would plausibly do next, and each would cost.**

## §8.1 · Do not weaken the design to make cases pass

- **Do not add a `target` or an `actor` field to `Event`** to make routing or witnessing easier. It is
  the twin of the attribution field the design **deliberately removed**, and it would make L2
  unenforceable.
- **Do not add** a `Cohort` subclass · a per-container clock · a second resolver · an auto-resolve
  band · a default `max_depth`.
- **Do not cap, dedup or price petitions** to thin the option set. #353 `:919-945`: any of them is
  *"an engine deciding a person's options, which is L1"*. **The thin vocabulary is an accepted state.**
- **Do not "fix" the treasury by pooling a social quantity.** `stores` are matter and are lawful at a
  Rung; unrest is a Query. That confusion already cost ten arcs once.

## §8.2 · Do not repeat the method failures

- **Do not write a findings document** as the output of any adversarial pass on `W2`/`W3`. Edits and
  one commit paragraph. *(§0's amendment; `G5`.)*
- **Do not write a repository guard under `tools/`** for any of this. *(§0.1 point 5; `G9`.)*
- **Do not restore prose lists of open items.** Every new hole is a register row or it does not exist.
- **Do not average the two pathways again.** *(`G10`.)*
- **Do not add another word to a router's roster.** *(§7.4; `G2`.)*
- **Do not report a count without its command.** *(`G11`.)*

## §8.3 · Do not escalate what the ladder answers

- **Do not send `H-36` or `H-38` to Jordan.** Both close with citations, and `H-38` is presupposed by
  `V2`'s own Part D row and its own §F3. **Mark `H-36` held back in the PR body** — loudly, per
  `CLAUDE.md` §2 — so a reviewer who disagrees can object; that is the mechanism for a closure a
  session is confident in but does not own.
- **Do not preserve a `needs_jordan` row out of caution.** *"Preserving a dead question is not
  conservatism; it is how a 156-row queue formed."*

## §8.4 · Do not confuse the two lanes

- **Do not attempt to unblock any of the fourteen refusal-only arcs by specification work.** No
  specification change reaches them.
- **Do not attempt to unblock any of the eight mixed arcs by re-authoring alone.** Each needs a hole
  closed **first**; re-authoring one before its hole closes produces an arc that still fails, and the
  failure will be read as a defect in the re-authoring.
- **Do not start `W14` (Godot) before `W9`.**

## §8.5 · Do not treat this plan as ratified

Nothing here is ratified by merging it. It is `PROPOSED`, held back in full, and **`H-35` is an open
question to Jordan**, `H-36` a closure explicitly offered for objection.

---

# PART 9 · HOW TO FALSIFY THIS PLAN

| claim | what would prove it wrong |
|---|---|
| the critical path is `W0→W1→W2→W3→W5→W9` | an artifact-2 run that completes without one of the six, **or** a seventh item that turns out to block it |
| `W0` is first | a re-grade, a matrix row or a verb row that can be written correctly **without** a graded register — show one |
| eleven of twelve `absent` rows close in chain | **a cited line that does not say what §3.1–§3.4 claims it says.** Every citation is a file and a line; check them |
| `H-35` is the only genuine escalation | a second row where two defensible options lead to materially different games and no test of the five returns an answer |
| the register is now complete | **a hole an instrument must fill that carries no row** — `V2`'s own falsifier, which fired **19 times** against `V2` and will be re-run against `hole_register.yaml` |
| declared routing makes 60 cases assessable | a case with `exercises:` authored on every core row that is still NOT-ASSESSED for a reason that is not *"nobody authored it"* |
| the 22-arc residue needs re-authoring, not design | a re-authored arc, expressed purely through §36.3's petition chain and §37's `tell`, that **still** routes to a refusal probe |
| **the whole plan** | **artifact 2 does not run after `W0–W5`.** Everything above is a hypothesis about why the tested version ran zero cases end to end. **One case running is the only evidence that the diagnosis was right.** |

## §9.1 · What would make THIS document done — §0.2's standard, applied to itself

**Nothing in it runs.** It is reference under §0.05 and it is prose under §0.2. Exactly **one** of
its claims is satisfiable by writing — **`V2` §I2's artifact 0**, *"Part VII has no `absent` row in
Tier 0"*, which `W0` + `W1` deliver and which `V2` currently **fails on its own `H-02`** without
saying so.

**Everything else in Part 4 is an execution, and the plan is worth exactly what those executions
return.**

---

## §10 · PROVENANCE

| | |
|---|---|
| **Adjudicated by** | a read-only `valoria-critic` on the top tier — `Read`/`Grep`/`Glob`, **no write tools**, so its independence is a property of `.claude/agents/valoria-critic.md` and not of its prompt (`CLAUDE.md` §10). It read #353 (2,068 lines) and `ARCHITECTURE_V2.md` (830) in full, produced **no files**, and stated its own coverage, its own sampling and its own null results |
| **Measured by** | direct execution during composition — `report.py`, `pytest test_tracer_is_honest.py` (**63 passed**), and set-cover/verdict queries over `results.json`, each with its command in-line |
| **Corrections this document makes to its own author's prior work** | three, in §1.3: `H-23` (a precedent that would have overturned an explicit sentence of the specification), `H-36` (emitter- vs receiver-side, decided the wrong way), and the Part E verb-roster check (**a keyword search reported as a verified negative** — the same router failure the plan exists to end) |
| **Escalations** | **one** — `H-35`, and it blocks nothing |
| **Held back for objection** | **one** — `H-36`, closed receiver-side |
| **Scope** | every closure is made **in chain** (PR #337 → now). `W16` records what a tree-wide search returns and **the plan rests on none of it** |
| **`ED` allocated** | **none.** A gap in a `PROPOSED` architecture gets no ID; the adoption decision gets one |

> ### THE TWO SENTENCES TO CARRY
> **1.** The register was never the problem for being too strict. **It was not an object** — a
> markdown table nothing reads, whose counts do not reproduce from its own rows, which is why it
> could not tell anyone that nineteen holes had no row and eleven of its twelve refusals were
> answerable from the document it was refusing about.
>
> **2.** **The tested version ran zero cases end to end.** Every item in Part 4 is subordinate to
> making that number **one**.
