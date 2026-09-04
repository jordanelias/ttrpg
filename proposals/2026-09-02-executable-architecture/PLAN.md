# THE IMPROVEMENT PLAN — WHAT TO BUILD, IN WHAT ORDER, AND WHAT MAY NOT BE INVENTED WHILE BUILDING IT

## Status: **PROPOSED (2026-09-02). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Scope: **PR #337 → now, for evidence AND for answers.** Every closure in Part 3 is made on #353's
## own text. §2.6 and W16 record what a tree-wide search returns and **the plan rests on none of it.**
## Companion to `ARCHITECTURE_V2.md` (the specification) and `01_NPC_VS_ARC.md` (the split).
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** Under §0.2 **nothing in
## it runs** — **Part 6** names what would.

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
| **4** | **seventeen work items**, each with a deliverable and a DONE-WHEN that executes | §0.2: a juncture is done when the behaviour runs |
| **5** | the **dependency graph** and the **critical path** | seven of the seventeen reach the bar; the other ten run beside it |
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
> **3.** **The tested version ran zero cases end to end.** Every one of the seventeen items is
> subordinate to making that number **one**.
>
> ⚠ **AND ONE WAS REACHED WHILE THE GOAL WAS NOT — which is why PART 4B exists.** Artifact 2 runs;
> 0 of 143 cases run by Part 6's current definition. The number this document is subordinate to is
> now TWO counts over the whole corpus, not one case.

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
one log, the seam, no per-container clock and fixed point: **uphold.** The honesty tests
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
`python3 -m pytest test_tracer_is_honest.py -q` → **63 passed** ⚠ **AT THE TIME OF WRITING. The file defines 143 tests today; run the command rather than citing this number, which is what `G11` asks for and what this line was doing wrong (`W19`).**

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

> ### ⚠ ROUTER-ERA · NOT REPRODUCIBLE UNDER `W10` · NEITHER WITHDRAWN NOR CONFIRMED
> Every count in this section was computed from a `results.json` produced by the **regex router**,
> which `W10` deleted. Routing is now an authored `exercises:` declaration, so the corpus verdicts
> are **6 BLOCKED · 2 DEGRADED · 135 NOT-ASSESSED** — and 135 of those mean *nobody has authored a
> declaration yet*, which is a fact about authoring, not about the design. The ARC lane has **0 of
> 611 rows declared**, so its column is **unmeasured**, not measured as zero (§42.2's polarity
> rule; §0.1 pt 4 in both directions). Re-measuring is `W13`'s lane.
> Commands: `cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py` · `python run_cases.py`.

> *(The agreement-across-emitters claim — `W15`'s subject — is unaffected: it is about there being
> ONE WRITER, not about the numbers that writer emits.)*

> **This is not a typo class. It is the `CLAUDE.md` §8 invariant — *every rule lives once* — applied
> to artifacts rather than rules: EVERY ARTIFACT HAS ONE WRITER.** Work item **W15**.

## §2.2 · Three published counts were wrong. Corrected here.

⚠ **The `measured` column below is ROUTER-ERA** (see the mark above §2.4; commands there). The
*finding* — that `V2` published counts nothing reproduced — is unaffected and is why the register
exists; the specific replacement figures are not current. Both columns are kept: neither is the
answer, and the section's point is that they differed.

| claim | published | measured (router-era) | where |
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

**⚠ SUPERSEDED BY `W10`, WHICH IS THE ITEM THIS SECTION EXISTS TO ARGUE FOR.** The `routed` column
measured what a regex matched. That router is deleted, so the table below is history — kept because
it is the evidence the item was worth doing, not because a reader can check it.

| | cases | rows | `core` rows | routed *(regex, retired)* | **unrouted** |
|---|---:|---:|---:|---:|---:|
| NPC | 46 | 346 | 122 | 59 | **63** |
| ARC | 97 | 626 | 300 | 133 | **167** |
| **total** | **143** | **972** | **422** | **192** | **230 (54.5%)** |

**THE LIVE TABLE, and the denominator is authored coverage rather than pattern coverage**
(`cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py`, `python run_cases.py`):

| | cases | rows | `UNCLEAR:` | declarable | **declared** | `core` | **core declared** |
|---|---:|---:|---:|---:|---:|---:|---:|
| NPC | 46 | 346 | 54 | 292 | **35** | 122 | **32** |
| ARC | 97 | 626 | 15 | 611 | **0** | 300 | **0** |
| **total** | **143** | **972** | **69** | **903** | **35** | **422** | **32** |

The two tables are **not comparable and must not be subtracted from one another** — the first
counts what a pattern matched, the second what a human wrote — and that non-comparability is
exactly `W10`'s claim: an undeclared row is now VISIBLY unauthored rather than silently unmatched.
Every count the router published was a **floor**.

~~**All 60 NOT-ASSESSED cases have zero core blockers.**~~ Router-era. There are **135**
NOT-ASSESSED cases now, and the reason is authoring, not aim. Declared routing makes each one
assessable *once somebody authors it* — which is not the same as runnable, and this document does
not conflate them.

## §2.4 · THE MEASURED UNBLOCK YIELD — the number this plan is sequenced on

> ### ⚠ ROUTER-ERA · NOT REPRODUCIBLE UNDER `W10` · NEITHER WITHDRAWN NOR CONFIRMED
> Every count in this section was computed from a `results.json` produced by the **regex router**,
> which `W10` deleted. Routing is now an authored `exercises:` declaration, so the corpus verdicts
> are **6 BLOCKED · 2 DEGRADED · 135 NOT-ASSESSED** — and 135 of those mean *nobody has authored a
> declaration yet*, which is a fact about authoring, not about the design. The ARC lane has **0 of
> 611 rows declared**, so its column is **unmeasured**, not measured as zero (§42.2's polarity
> rule; §0.1 pt 4 in both directions). Re-measuring is `W13`'s lane.
> Commands: `cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py` · `python run_cases.py`.

> ⚠ **AND THIS IS THE LOAD-BEARING ONE, by the section's own title.** The set cover below is
> computed over probe ids in a `blockers` field that no longer contains any, so it cannot be
> re-derived today at all. **The sequencing it justified is not being re-litigated on that basis**
> — the ordering also follows from the dependency graph in Part 4, which is independent of these
> counts — but no reader should take the yield figures as current, and `W13`'s authoring lane is
> what makes them checkable again.

A case is **freed** when *every one* of its blockers is a hole that closed. Set cover over the 76
blocked cases, using `01_NPC_VS_ARC.md` §2.1's probe→hole mapping:

| closing | frees | NPC | ARC | |
|---|---:|---:|---:|---|
| **H-20 alone** | **21** | 5 | 16 | |
| H-20 + H-22 | **33** | 12 | 21 | |
| H-20 + H-22 + H-23 | 37 | 13 | 24 | ⚠ **`H-23` is a REFUSAL, ruled in §3.1 — it frees nothing. Row kept so the raw computation is auditable; see §5.2 — ⚠ the set-cover table this pointed at was router-era and is deleted** |
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

### **H-35 — does a scene equal an act? ✅ RULED BY JORDAN, 2026-09-02. THE QUEUE IS EMPTY.**

> **Verbatim, in answer to the escalation this document raised:**
> ### ***"5 scenes for a character to play per season"***

This is **reading 2** of the three the in-chain ruling doc flagged, and it is the reading that ruling
doc marked as the one the canonical prior art already supplies. **The budgeted unit is the SCENE.**

| what the ruling settles | |
|---|---|
| **the unit** | **the scene**, not the act. `budget` bounds scenes; #353's verbs are what happens *inside* one |
| **the number** | **5** |
| **who gets it** | **"a character"** — the neutral word, not *"the player"*. See below; this closes the hazard the ruling doc named as the one to watch |

### What it settles that was open, and how each is graded

| | grade | basis |
|---|---|---|
| the unit is the scene · the number is 5 | **RULED** | Jordan, 2026-09-02, verbatim above |
| **every character has the budget — the archive's asymmetric economy is REJECTED** | **ruled by design document + architecture** (§0 tests 3 and 5) | Jordan said *"a character"*. #353 L1 makes the person the only actor and §26 has **everyone run `choose`**. The in-chain ruling doc flagged reading 3 — *"named NPCs have no action budget at all; they generate Scene Slate entries that cost **the player's** budget"* — as **"precisely the player-only mechanism §07 §1 forbids"**. It is now closed against the archive and toward the shape |
| **how many interactions a scene admits** | **`assumption`, default 1–3** | ⚠ **NOT ruled.** Jordan did not say. The default comes from `player_agency_v30.md` §6.3 — *"One scene action = one scene opportunity pursued. A scene contains 1–3 mechanical interactions"* — which is `## Status: CANONICAL` but **pre-#337 and, under §0.05, reference rather than mechanism.** Inject it, declare it, **sweep it 1 · 3 · unbounded** |
| **whether an extended scene costs 2** | **`assumption`, default 2** | same source, same grading. Sweep `1 · 2` |
| rank changing the budget | **already consistent, no action** | #353 §26.3 varies `budget` by *"office, condition, distance travelled"* and `V2` §F3's formula carries `office_bonus`. `player_agency_v30`'s Standing `+1`/`+2` is the same shape. **PR #350's *"No office, rank or holding changes it, ever"* was already overturned by #353** |

### What it costs, stated plainly, because the escalation named this cost and Jordan accepted it

**It buys the container the loop does not have.** The question as put said reading 2 *"costs a second
budget object and a container the loop does not have"*. That is now work, not a hypothetical:

- **`budget` returns SCENE actions.** #353 §26.3's prose counts acts throughout — *"a wounded duke gets
  fewer **acts**"*, *"a character who spends all five **acts** petitioning"*. **The argument survives
  the noun change unaltered** (five scenes each spent petitioning is still the triage the budget
  exists to create), but every one of those sentences needs re-stating in scenes.
- **Part E's verb table is UNCHANGED and is now correctly placed.** Its ~28 verbs are the *mechanical
  interactions*; the scene is the container above them. **Nothing in Parts D or E is invalidated** —
  a level is added above, which is the cheapest possible shape for this ruling to take.
- ⚠ **Probe `P2x` changes meaning and must be re-expressed.** It currently fails with *"`p_king`
  returned 8 acts against a budget of 5"*. Under the ruling **8 interactions across ≤5 scenes is
  lawful**, so as written the probe now tests the wrong proposition. **This is a real defect the
  ruling creates and it is named rather than absorbed** — work item **W17**.

> ### **THE `needs_jordan` QUEUE FOR THIS PROPOSAL IS NOW EMPTY.**
> `ARCHITECTURE_V2.md` sent three escalations. One closed on precedent (`H-38`), one closed on
> architecture and is held back for objection (`H-36`), and **the one that genuinely survived all five
> tests has been answered.** Nothing in this plan is now waiting on a ruling.

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

> ### ⚠ THAT COMMAND RETURNS `[('NPC', 0), ('ARC', 0)]` AS OF `W10`, AND EVERY FIGURE IN THE TABLE
> ### ABOVE IS ROUTER-ERA. Amended 2026-09-02 by `W10`'s adversarial pass.
>
> **What broke it, and it is not a bug.** The table was computed from a `results.json` whose
> `blockers` were **probe ids**, because under the regex router a probe was the only thing a case
> row could reach. `W10` deleted that router; `blockers` now names the **declared token that
> failed** — a hole id, a verb, or `probe:PID` — so a set membership test against bare probe ids
> matches nothing. `W10`'s own note says naming `H-84` is a better answer than "P22 gapped", and
> this is the price of that: the old query no longer has a subject.
>
> **And the old numbers were a FLOOR, not a total.** A row matching no pattern fell silently to
> UNMAPPED, so every count derived from routing understated the corpus **in the direction that
> flattered it**. That applies to the "published" column and to both "measured" columns alike.
>
> **Status of the finding: NOT REFUTED, NOT REPRODUCIBLE — awaiting re-measurement.** `§0.1`
> point 4 governs, and it cuts both ways: a router-era number is not evidence, and its absence is
> not evidence against. Do not cite the `0` / `2` / `3` cells as current, and do not delete them
> either — they are what a re-measurement has to beat.
>
> **What re-measures it.** Declared coverage, which is `W13`'s lane and is thin:
> ```
> cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py
> #   NPC: 35/292 rows authored (32/122 core)
> #   ARC:  0/611 rows authored ( 0/300 core)
> ```
> The ARC lane has **no declared row at all**, so *every* arc figure in this section is currently
> unmeasured rather than measured-as-zero — §42.2's polarity rule, applied to this instrument.
> The re-measurement is meaningful once `W13` authors the arc overlay, and its command is the one
> above with `R` rewritten over declared tokens rather than probe ids.

> **The qualitative conclusion survives and is sharper; the number `0%` is wrong.** The NPC pathway
> is *overwhelmingly* blocked by holes — 21 of 23 blocked cases have no refusal in them — and the arc
> pathway is *nearly half* refusal-touching. **A claim of exactly zero is the kind of number that
> should have had a control, and §0.1 point 4 says so in both directions.** Two further omissions in
> the same table: `P6` and `P20` block NPC cases (NPC-021, NPC-035) and appear in neither column.

## §3.6 · The residue, and it is small

| | `V2` | after the ladder | after Jordan's 2026-09-02 ruling |
|---|---:|---:|---:|
| `absent` rows | **12** | **1** — `H-02`'s two verb rows, which fall out of **W3** | **1** |
| **genuine Jordan escalations** | **3** | **1** — `H-35` | **0 — THE QUEUE IS EMPTY** |
| conditional closures held back in the PR body | 0 | **1** — `H-36` | **1** |
| new `assumption` rows the ruling creates | — | — | **2** — interactions per scene (1–3) · extended-scene cost (2) |
| **holes with NO ROW AT ALL** | *unknown* | **19** — §1.4 plus `A18` | **19** |

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

> ### ✅ **`W0` LANDED 2026-09-02 — and its Proof's first clause is WRONG. Recorded loudly rather than quietly satisfied.**
>
> `hole_register.yaml` carries **54 rows** — the 32 transcribed mechanically from `V2` §VII, the
> 18 holes of §1.4 with its four §62/§54 carry-overs expanded to four rows, and `A18`.
> `tracer/register.py` reads it and nothing else does.
>
> **`--check` exits 1, and it must.** *"Exits 0"* was written before anyone transcribed the rows,
> and it contradicts **this document's own §1.5**: if not one of the 32 rows carries `site:`,
> `sweep:` or `cite:`, then a register that transcribes them faithfully **cannot** pass the rules
> that read those fields. Writing 0 would have required backfilling citations nobody derived —
> laundering a transcription into a closure, which is the move the register exists to stop. So the
> honest proof is a **measurement**, and it is stronger than the assertion it replaces:
>
> | rule | today | closed by |
> |---|---|---|
> | `R0` shape · `R1` graded · `G8` discharged | **ok** — `--check --rule R0,R1,G8` exits 0 | — |
> | `R2` an `assumption` carries `site:` + 3 `sweep:` points | **23 violations** | `W1` |
> | `R3` an `absent` carries no `default:` | **2 — `H-02` and `H-20`** | `W3`, `W1` |
> | `G6` an `absent` carries a `cite:` | **34 violations** | `W1` |
>
> **One tier assignment was overturned by the adversarial pass and is corrected here.** `H-55`
> (`D22` × `H-33` — per-write MATTER emissions under total fan-out flooding every ledger) was
> placed in **Tier 0** and belongs in **Tier 1**: §VII.1's bar is *"required before ANY season
> completes"*, and **a flooded ledger completes the season** — eviction churn is a fidelity defect,
> not a completion blocker. It was also internally inconsistent, since `H-33` — the unfilled
> predicates that CAUSE the total fan-out — is Tier 1, and an interaction row cannot block harder
> than its own component.

> **`R3`'s two are a finding, not noise.** `V2` grades `H-02` and `H-20` partly `absent` **and
> supplies each a default**. A part-absent hole with one `default:` field is **not representable in
> §G4's shape**, and §42.2.1 forbids the combination it expresses. The fix is to split the hole, not
> to delete the default.
>
> **Both plants fire**, and a third was added: an ungraded row fails `R1`; a `default:` on an
> `absent` row fails `R3`; and `--verify-transcription` re-extracts `V2`'s tables and fails on
> drift **in either direction**, so the register and the prose cannot part company silently.
>
> **Also discharged from the list above:** the `§D20`–`§D26` citation form — **eighteen** citations,
> not the four this item names, **and on two grounds rather than one.** Part D has only
> `§D1`–`§D5` (verified: the headings are at `ARCHITECTURE_V2.md` `:277`, `:289`, `:305`, `:350`,
> `:360`).
>
> - **Thirteen are above `§D5`** — `§D6`, `§D7`, `§D8`, `§D11`, `§D18`, `§D20`, `§D21`, `§D22`,
>   `§D26` — so **no section of that name exists** and each is a Part B defect id wearing a
>   section's clothes. Fixing only the four this item names would have left five wrong on
>   identical grounds, which the note above calls *"the worst of both"*.
> - **Five are `§D1`–`§D5`, and they rest on a different ground that must be stated rather than
>   folded into the first:** they are the *`where`* column of §0.3's defect table (`:68`–`:72`),
>   which is a **defect-id column** — its rows 13 and 14 hold `**§G**` and `**Part VII**`, so the
>   column mixes both namespaces and normalising the twelve defect rows to ids is an **editorial**
>   call, not a consequence of the range rule. ⚠ **Two of those five were defensible as section
>   references** — row 1's verdict restates §D1's argument and row 4's restates §D4's heading —
>   and are changed anyway, for column consistency. A reader applying only the range rule could
>   not reproduce those five edits, which is why the ground is written out here.
>
> **No `§D1`–`§D5` outside that column was touched**; each surviving one is a genuine section
> reference (`:152`, `:333`, `:350`, `:535`, `:602`, `:688`). And **`V2` §I2's artifact 0 is now
> marked UNMET**, which it is — on `H-02` and several more. `register.py --counts` **names** them,
> so it can no longer be a sentence; the count is not restated here because it moves with every
> re-grade and every re-tier.

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

> ### ✅ **`W1` LANDED 2026-09-02. The ladder ran; two of this item's own claims did not survive it.**
>
> **All fourteen rows moved**, each carrying the citation that closes it:
>
> | | rows | grade |
> |---|---|---|
> | §3.1 closed | `H-23` (as a **refusal**) · `H-37` · `H-38` · `H-60` | `ruled` |
> | §3.1 closed, with an obligation | `H-25` | **`measured`**, not `ruled` — the argument is sound and **unexecuted**, and `W11` discharges it |
> | §3.4 closed, **held back for objection** | `H-36`, receiver-side | `ruled` |
> | §3.2 re-graded | `H-20` `H-26` `H-31` `H-32` `H-33` `H-39` | `assumption`, each with a `site:` and three distinct `sweep:` points |
> | §3.2/§3.3 re-graded **DOWN** from `ruled` | `H-27` `H-28` | `assumption` — a **strengthening**: the answers survive, the arguments for them do not |
>
> `H-26` moved to **Tier 0**, in the register *and* in `V2`'s tables — a tier that disagrees
> between the two is `W0`'s counts defect, one field over.
>
> **Measured** — `python tracer/register.py --counts` and `--check`:
> `absent` **34 → 22** · `assumption` 12 → 20 · `measured` 0 → **1** · `ruled` 8 → 11 ·
> `R3` **2 → 1** · `G6` **34 → 22**.
>
> #### ⚠ **THIS ITEM'S PROOF IS UNREACHABLE, AND §3.6 SAYS SO ALREADY.**
> *"Tier 0 containing no `absent` row"* cannot hold after `W1`. **§3.6's own residue table says one
> `absent` row survives the ladder — `H-02`, which is Tier 0 and falls out of `W3`.** The two
> sentences were always in conflict and §3.6 is the careful one. Artifact 0 closes at **`W3`**, not
> here, and it is now UNMET on `H-02` plus seven of the rows `W0` carried.
>
> #### ⚠ **NO WORK ITEM RUNS THE LADDER OVER THE TWENTY-TWO ROWS `W0` ADDED.**
> This item is scoped to §3.1–§3.4, which is **the twelve**. The 22 holes of §1.4 are discharged
> **by construction** at `W2`/`W3`/`W5` rather than by the five tests, so they stay `absent` with an
> empty `cite:` and **they are the whole of `G6`'s remaining 22.** That is the honest state and not a
> gap to paper over: closing them by ladder would be inventing closures for holes whose answer is a
> table nobody has built yet. **Each building item must set its rows' grades as it lands.**
>
> #### ⚠ **`R2`'S 23 VIOLATIONS ARE NOT THIS ITEM'S EITHER, AND NOBODY OWNS THEM.**
> They are the **pre-existing** `assumption` rows — `H-03`–`H-11`, `H-29`, `H-30`, `H-34` — which
> `V2` graded `assumption` and never gave a `site:` or a `sweep:`. That is §1.5's finding, and no
> item in Part 4 is assigned to fill them; each belongs with the item that builds what its default
> is injected into (`H-06`/`H-07`/`H-08` with `W8`, `H-09` with `W6`, `H-29` with `W5`).
>
> **Two line numbers in §3.2 are off** and are corrected in the rows that cite them: the *"vacant
> date fires… and lapses"* sentence is at **`:835`**, not `:837`; *"`yield` — only here"* is at
> **`:856`**, not `:855`. **Neither claim is wrong** — every one of the fourteen citations was
> verified by hand against #353 and then mechanised, so it stops depending on anyone remembering:
> `python tracer/register.py --verify-citations` checks that every `:NNN` exists and every verbatim
> quote is at the line cited, and it **distinguishes a fabricated quote from a wrong line number**.

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

> ### ⚠ THE GOVERNANCE SLICE'S ADVERSARIAL PASS — it overturned the headline, and found a
> ### fabrication committed inside the fix for a fabrication
>
> **1. "The governance verbs now RUN" is true of the FOLD and false of any person.**
> `person_side_eligible` declines every `remit:` alternative unconditionally — that is **`H-71`,
> already registered `absent` and TIER 0**, with its `unblocks:` already reading *"9 of 32 verbs
> cannot be formed person-side — 8 remit-ONLY"*. All four slice verbs are remit-only, so
> `Query.opening_set` never offers them **in any world**, including one where the actor genuinely
> holds the office whose remit names the act. **`resolvable_verbs()` moving 8 → 12 cannot affect
> any run.** I built the RESOLVE half of a mechanism whose DELIBERATE half is an open tier-0 hole,
> and said it runs. `test_no_person_can_choose_a_governance_verb_and_h71_is_why` pins it and goes
> red the day `H-71` closes.
>
> **2. `confer` published a FABRICATED `tenure.closed`.** `_fold` emitted every kind in `emits:`
> once anything changed, and `confer` declares both `tenure.opened` and `tenure.closed` — so
> conferring onto an unheld office announced a closure that never happened. **That is the
> fabricated-`person.died` class, committed inside the fix for it**, and the existing guard could
> not see it because it is all-or-nothing per act. An effect may now return `{kind: [ids]}` and
> the fold emits only what was earned.
>
> **3. The `scale:` column reaches NO resolver** — validated at load and read by nothing else.
> **Third instance of this defect in one session**, after `stratum` (`H-83`) and `contests:`; this
> session diagnosed both and then shipped a third. Registered as **`H-89`**, `absent`, with the
> candidate readers named and none chosen, because choosing is a design decision.
>
> **4. Three predicates were wrong.** `_req_confer` dropped a conjunct *and* an `or` disjunct — an
> **over-refusal**, `G4`; `_req_revoke` omitted the office check and could revoke a person's
> possession of a **book**, since §13 makes possession a `hold` — an **over-admission**;
> `_req_convene` tested that the venue *is* a rung rather than that its **container resolves**,
> and `Query.parent_of` already existed. All three now implement Part E's full text.
>
> **5. `H-87`'s cap was unreachable.** `contest_subsystem` ran BEFORE the depth check, so
> `ContestError("max_depth reached")` could not fire for any rostered prize — the registered
> number had no consumer and its sweep was three arms identical by construction. The dispatch
> moved below the check. ⚠ My first attempt added a SECOND cap test twelve lines above the
> existing one — §8 broken in the act of fixing an ordering bug.
>
> **6. `person.died` 4 → 0 was not caused by this change.** `W9`'s *"an effect that touched
> nothing"* guard already drove it to 0 and predates the seam work; and the seam is never reached
> anyway, because `kill / wound` left the chooser's set. Two sufficient causes, the earlier one
> already fired — the commit banked a delta it did not produce, and the `4` shipped with no
> command (`G11`, again).
>
> **7. `PROBE FLIPS 0` was not reassurance.** None of the new code is on an exercised path: the
> governance verbs cannot be chosen (1), `kill / wound` cannot be chosen, and the only probes
> reaching `contest()` use an unrostered prize. Arms identical by construction, reported as a
> control — §0.1 pt 4.
>
> **Two tests could not fail** and were rebuilt: the channel test used a hand-built Event and
> **would have passed on the pre-session tree**; and the "genuinely crossed" assertion was
> satisfied entirely by the unauthored `person` default bucket. A third guard, `W2`'s write-site
> walk, exempted the fold by **line proximity** and broke when the fold grew eight lines — it
> exempts by AST containment now.

> ### LANDED 2026-09-02 — and the gate found six silent MATTER writes on its first run
>
> **`shape.World.write` is the emitter.** `H-12` is RULED that way (*"MATTER emits an Event per
> write so crossings have an antecedent"*, default *"Part D's `emits:` column"*), and `W4` executes
> the ruling rather than making one. A MATTER write on a row Part D gives an `emits:` must name one
> of the declared kinds; a kind the row does not declare is refused. That pairing is **`D22` made
> mechanical in both directions** — a silent write and a fabricated kind are the two ways the
> column can be wrong. Emission lives in `write()` rather than at each call site because it keys on
> `(record_kind, fieldname)`, the same key the write class and the social partition already use, so
> **a new MATTER write inherits its emission by existing rather than by remembering** (§8).
>
> | proof clause | result |
> |---|---|
> | a crossing's `causes[]` walks to the wear that crossed the floor | **yes** — `condition.band_crossed → condition.worn → … → ROOT`, asserted in `test_w4_a_band_crossing_walks_back_to_the_wear_that_caused_it` |
> | `[ROOT]` only for the seed and a clock's genuine first emission | **one `[ROOT]` at 1, 2, 3 and 4 seasons**, always `condition.worn` at season 0, always one per site — asserted, not printed (`G3`) |
> | `(Claim, confidence)` decays at MATTER and emits | **yes** — the third licensed clock (#353 `:864`) runs; a decay walks back through its deposit to the act that was witnessed |
>
> ```
> cd proposals/2026-09-01-season-loop-tests/tracer
> python -m pytest test_tracer_is_honest.py -q -k w4       # 4 passed
> python delta.py                                          # PROBE FLIPS 0
> ```
> **Events per 2-season run: 18 → 108. Distinct kinds emitted: 9 → 12. `TRACE.EVENT` 62 → 1204.**
>
> **THREE DEFECTS THE PROOF CLAUSES CAUGHT WHILE `W4` WAS BEING BUILT**, which is the argument for
> asserting them rather than printing them:
> 1. `write()` used the **TRACE LABEL** as the Event subject, so every site's wear emitted under
>    the subject `"condition"`, `last_emission_of` never matched, and the clock **re-rooted every
>    season**. The ROOT count caught it on the first run.
> 2. A claim's first decay rooted at the seed, because **the deposit that created it emitted
>    nothing** — Part D declares `claim.deposited` on `(Person, claim_ledger)` and nothing ever
>    emitted it. 63 spurious roots in a 3-season run. A claim is not a clock; it is a thing a
>    witness deposited, and the deposit has an Event.
> 3. `P18` **asserted `ev.causes == [ROOT]`** — a probe pinning the defect `H-12` rules against. It
>    now checks the antecedent resolves to a `condition.worn` for the same site in the same season,
>    which is the claim `H-12` actually makes.
>
> **SIX SILENT MATTER WRITES, found by turning the gate on:** `(Record, matured)`, `(Person,
> exists)` twice, `(Tenure, until)`, `(Record, ttl)` and `(Rung, envelope)` — every one on a row
> whose `emits:` Part D declares. **Five are fixed. The sixth is a finding and is registered as
> `H-86`:** `(Record, ttl)` declares only `record.expired`, and the row is decremented every
> season, so emitting it per write would **assert an expiry that has not happened** — the
> fabrication `G1` forbids — while refusing the write would stop §13's licensed clock. Part D's
> column does not distinguish a per-write kind from a conditional one. The exempt rows are data
> (`rosters.yaml: conditional_emission_rows`), the ambiguity is registered rather than decided, and
> its third sweep point (split the column into `emits_per_write:` and `emits_when:`) is the real
> fix and belongs to whoever ratifies Part D.
>
> **Register.** `H-12` gains its `site:` and its execution note — `unblocks:` is left verbatim,
> because the transcription gate is right that an execution note is not a transcription. **`H-40`
> closes in two halves by §0's tests**: the SCHEMA_ROW half is **superseded** (`W2` gave Part D the
> `(Claim, confidence)` row), and the FORMULA half is answered by **precedent** — `Site.condition`
> wear is the other licensed MATTER clock and #353 gives *it* no rate either, so it is a registered
> fixture that refuses when unregistered. `absent` → `assumption`, `site: Fixtures.claim_decay`,
> sweep `[0, 5, 20]`. **`G6` 17 → 16.** Grading it `ruled` would credit an invented number to #353;
> leaving it `absent` would deny a mechanism that now runs.
>
> **One defect of my own, caught by an existing guard:** the first version re-implemented S19.4's
> empty-`causes[]` refusal inside `write()`, one constructor away from `Event.__post_init__`, which
> already does it. Two messages for one rule is §8 exactly. Deleted.

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
of §3.3** — and, per Jordan's 2026-09-02 ruling, **returning SCENE actions rather than acts** (§3.4).
`choose` returns **at most `budget` scenes**, each resolving into 1–3 verb applications from
`verb_table.yaml`; the interactions-per-scene bound and the extended-scene cost are **`assumption`
rows, swept** — never constants in a body. `standing` with a **defined predicate vocabulary and a defined `agreement`** — `V2`
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

> ### LANDED 2026-09-02 — and §1.4 hole 16 stopped being an argument
>
> **The five channels have predicates**, injected and declared in
> `rosters.yaml: witness_channel_predicates`, each computed from WORLD STATE — §19.3 removes
> `target` from the Event and says why: *"observers are computed at WITNESS from presence; the
> emitter declares no recipient."* `shape.observers_for` is the reader, and the presence index
> this barrier has always built was **unused until now**.
>
> | mode | events (3 seasons) | deposits | ledgers (sorted, as the instrument prints them) |
> |---|---:|---:|---|
> | `total` — **#353's specified behaviour, and the control** | 896 | **678** | `[200, 200, 200]` *(at the `L` cap)* |
> | `presence_only` | 161 | **68** | `[0, 34, 34]` |
> | `all_five` | 165 | **71** | `[0, 34, 37]` |
>
> *(The triples are quoted as the instrument sorts them. The first version of this table retyped
> them in a third order, and `hole_register.yaml` in a fourth — same multisets, three spellings,
> none of them a copy. `delta.py`'s own instruction is quote, don't retype.)*
>
> ```
> cd proposals/2026-09-01-season-loop-tests/tracer
> python -m pytest test_tracer_is_honest.py -q -k w6      # 3 passed
> ```
>
> ### ⚠ AMENDED BY `W6`'s ADVERSARIAL PASS — three corrections to the note above
>
> **1. `P15`'s flip was false when first published.** It passed on a channel BROKEN CLOSED, not
> on a predicate that excludes: `_event_place` tested `e.subject in w.rungs` first, and every
> person has a same-id `person`-kind Rung, so presence answered *"who is contained IN p_high"* —
> nobody. `presence_only` excluded the speaker and everyone in the room, and `P15`'s only
> assertion (`narrow < total`) could not tell that from an exclusion. It now asserts BOTH
> directions. **This was a repeat** of a conflation `witness` had already retracted once.
>
> **2. `all_five` is a measurement of THREE channels, not five.** `_ch_post_remit` compared an
> office id against remit ACT NAMES and could not return `True` in any world (the correct lookup
> already lived once in `_eligible` — §8, one function apart). `_ch_chronicle` does not read `pid`
> at all and fired zero times, because **no `binding_decision` verb was executable** — so the
> published justification for its design was wrong even where its number was right. Both are
> fixed, and the governance slice is what makes them reachable; before it, two of the five
> channels could never admit anybody.
>
> **3. §1.4 hole 16 is `H-55`, and it was `absent` with every field empty** while this note claimed
> the item discharges it. It closes **`measured`**, not `ruled`: a row carries the interaction now
> and the arms are quantified, but the DEFAULT is still `total`, so `W6` makes the flood
> **boundable and measured, not bounded**.
>
> ### ⚠ THE THIRD PROOF CLAUSE IS NOT DISCHARGED, AND IS NOT REACHABLE AS THE ITEM IS SHAPED
>
> `W6`'s Proof has three clauses. The two below are met. The third — *"a `tell` reaches **only the
> told**"* — is not, and the reason is structural rather than unfinished work: **§19.3 removes
> `target` from the Event on purpose** (*"observers are computed at WITNESS from presence; THE
> EMITTER DECLARES NO RECIPIENT"*), and §F1's Candidate carries no operand channel (`H-80`), so
> nothing in the world records who was told. `tell` emits `news.told` with the TELLER as subject;
> under the three arms it reaches everyone, everyone in the teller's rung, or that plus the
> teller's `knot` partners. None is *"only the told"*.
>
> And `observers_for` applies **one mode to every event kind**, so there is no arm in which
> `news.told` uses a narrower channel set than `condition.worn`. Satisfying the clause needs a
> PER-KIND channel policy — a different shape from the one this item built. Recorded as
> undischarged under §42.2's polarity rule rather than left silent.
>
> **`P15` flips to PASS BY CONSTRUCTION**, which is `W6`'s first Proof clause — the same Event
> reaches five persons under `total` and fewer under `presence_only`, so a channel predicate now
> **excludes**, which is what `S61` says a wrapper cannot do. **Deposits fall from `N × E` to a
> number the sweep reports** — the second clause — by a factor of ten.
>
> ⚠ **THE DEFAULT STAYS `total`, AND THAT IS NOT AN OVERSIGHT.** `H-33` remains `assumption`:
> #353 names the five channels and supplies **no predicate for any of them**, so these are an
> injected default and grading the row `ruled` on the back of this item would credit the design
> with an answer this session invented. `total` is the default because it is what #353 specifies,
> and it is therefore also the control arm. A guard asserts the grade has not drifted.
>
> ⚠ **`chronicle` IS DELIBERATELY NOT `everyone`.** A public channel matching every person would
> make `all_five` identical to `total`, and the sweep would carry two points that are one arm
> wearing two names. It is the matter-of-record channel: what a `binding_decision` verb emits is
> public, because that is the design's own category for an act whose effect is institutional.
> A guard asserts `all_five` sits strictly between the other two.
>
> **WHY THIS BECAME URGENT RATHER THAN OPTIONAL, WHICH IS THE ITEM'S OWN CLAIM.** §1.4 hole 16
> says `D22` and `H-33` are *"individually fine and jointly fatal"* and that **no row in `V2`
> carries the interaction**. `W4` landed `D22`, and the argument became a measurement within the
> hour: events per run **207 → 896 → 3389** over two, three and four seasons, every ledger pinned
> at the `L = 200` cap, and **the test suite stopped finishing**. The cleanest example in the
> corpus of a defect that appears only when two rows are read together — and it appeared by
> running, not by reading.

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

## **W9 — ARTIFACT 2: ONE NPC SEASON, END TO END.** ⭐ **THE BAR — AS PART 6 THEN DEFINED IT.** Part 6 now supersedes that bar with two per-lane counts; `W9`'s own landed record is preserved at §6.5.

**Size M.** Depends on **W0–W5**. **`W6`, `W7`, `W8` are NOT required.**

---

## **W10 — DECLARED ROUTING FOR THE 143 CASES.** *(artifact 7)*

**Do.** Every `season_requires` row gains **`exercises: [<verb> | <contract §> | <H-id>]`, authored
with the row**. Delete `ROUTES*` and `COMPILED` from `run_cases.py`; **`route_precision.py` retires
with them** — a guard for a thing that no longer exists is the apparatus this repo's §0.3 is about.
**NOT-ASSESSED then means *"nobody authored an `exercises:`"*** — a fact about authoring, which is
fixable — instead of *"the regex missed"*, which is not.

~~**The measured size of the job: 230 of 422 `core` rows (54.5%) never routed**, and **all 60
NOT-ASSESSED cases have zero core blockers**, so every one of the 60 becomes assessable. It is
**~973 rows** across both case directories.~~

⚠ **STRUCK — router-era, and this item is the thing that made it so.** `W10`'s own DO section
described the job in the vocabulary of the router it deletes. The measurement that replaces it is
authored coverage, which is the honest denominator: **NPC 35 of 292 rows (32 of 122 core); ARC 0 of
611 (0 of 300 core)**, plus 69 `UNCLEAR:` rows that are the source's own admission and are not
anybody's to author. `cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py`.

**Discharges.** §H1 and **the entire bare-token class** — structurally, by deleting the router,
rather than by enumerating another word.

**Proof.** `results.json` regenerates with **zero regex routes**; the run prints, per case, **which
declared verbs executed**; **no PLAYABLE verdict rests on a row with an empty `exercises:`.**

**Size L.** Depends on **W3** for the vocabulary. A parallel lane thereafter.

> ### LANDED 2026-09-02 — the mechanism, and what its adversarial pass changed
>
> **The mechanism is done and the authoring is not.** `ROUTES`..`ROUTES_5`, `COMPILED` and
> `route()` are deleted; `route_precision.py` is deleted; `exercises.py` is the only path from a
> case row to a verdict, binding each declaration to its row by `need_sha` — the first 12 hex of
> the sha256 of the whitespace-normalised need — so a reworded row orphans its annotation loudly.
> Authoring stands at **35 of 292 NPC rows (32 of 122 core); 0 of 611 ARC rows**:
> ```
> cd proposals/2026-09-01-season-loop-tests/tracer && python exercises.py
> ```
>
> **⚠ CORRECTION TO THIS LANE'S OWN COMMIT MESSAGE.** `5a1d388` published *"`run_cases.py`
> 633 → 319 lines"*. **319 does not reproduce; the file was 366 at that commit and is 376 now.**
> The `633` is right. `git show 5a1d388:proposals/2026-09-01-season-loop-tests/tracer/run_cases.py
> | wc -l` is the check, and `G11` — every number ships with its command — is the rule that would
> have caught it before it was published. Recorded here rather than by rewriting a pushed commit.
>
> **Six defects the adversarial pass found in the landed mechanism, all fixed:**
>
> | | what was wrong | why it mattered |
> |---|---|---|
> | 1 | `resolve` graded an `assumption` register row as **PASS** | 15 rows published PASS while their own `from:` said the injected default was the *negation* of the need. Now three states — `absent` blocks, `assumption` is `ASSUMED` and carries the case to **DEGRADED**, `ruled`/`measured` pass |
> | 2 | `token == "term.matured"` — a **one-element kind list in a Python body**, added in the commit that deleted the router for that exact habit | The seventh recurrence of the bare-token class. Replaced by a union over `shape.MATRIX`'s and the verb table's `emits:` columns, so it moves when the data moves |
> | 3 | the token-resolution guard matched **three of `resolve`'s four failure strings** | A token naming a nonexistent Event kind was unguarded. Now asserted on a `bound` flag — *does this token name anything* — which is deliberately not `ok`, since a token can name a real thing that is `absent`. `G3` |
> | 4 | `unbound()` **skips a `case:` id it does not recognise**, and is called once per lane | A file naming a case in neither lane passed both checks with every row bound to nothing. `orphan_cases()` closes it |
> | 5 | the anti-router guard had **three evasions** — scoped to a function named `grade`, fired only on a receiver named `re`, and blacklisted three names | Replaced by a taint check: a need's TEXT may only be hashed, rendered or tokenised by a declared sanitizer, across whole modules and every scope. ⚠ **The claim "it would not have caught the router it replaced" was HALF WRONG and is corrected here.** Its *AST half* would not have — `COMPILED` held precompiled patterns, so there was no `re.` receiver, and `route()` is not `grade`. Its *blacklist half* would have, by name, and only by name: a rename defeats it. Settled by `git show 5a1d388:proposals/2026-09-01-season-loop-tests/tracer/test_tracer_is_honest.py`, which is the command `G11` asked for and the first version of this row did not give |
> | 6 | two grading guards were **satisfiable by deleting the rule they named**, and one of the rules was **inert** (`more than half unrouted` — its own predicate proved the strict clause below returned the same verdict) | The rule is deleted; the guards now build the discriminating input, with a control that reaches PLAYABLE so the assertion can observe its own failure. §0.1 pt 2 |
>
> **Not fixed, and named instead:** every router-era count is marked where it stands rather than
> deleted — §2.1, §2.2, §2.3, §2.4, §3.5, this item's own DO section, `W13`'s arc partition and
> `01_NPC_VS_ARC.md`. **Eight surfaces, not the three the first version of this note claimed.**
> The finding is neither withdrawn nor confirmed; re-measuring it *is* `W13`'s authoring lane.
>
> ### THE SECOND PASS, on the reconciliation above — seven more, and it overturned one of my fixes
>
> | | what was wrong | why it mattered |
> |---|---|---|
> | 1 | **the taint check was a name test wearing a dataflow test's clothes.** `text = r["need"]` laundered the taint in one statement, so the retired router came back **verbatim with one identifier renamed**, past all five of its plants | It also skipped module scope (where `ROUTES`/`COMPILED` actually lived), let the word `UNCLEAR` **in a comment inside a call's parentheses** exempt it, and could not see a bound method handed to an exempt builtin. Rewritten as real dataflow — assignment, walrus, `for`, comprehension and `with` targets, to a fixpoint, per lexical scope — with four more plants |
> | 2 | it scanned a **two-name filename tuple**, leaving `report.py` — the SOLE EMITTER — unscanned, and `report.py` had two inline need operations | A filename roster is a word roster one level up (`G2`), and `test_jordan_no_definition_is_hardcoded_in_a_body` had settled that shape 400 lines above. The file set is now globbed; rendering and tokenisation got **declared sanitizers** (`need_display`, `need_terms`) so the scan could be total instead of scoped away |
> | 3 | it **could not observe that it had scanned anything** | `not []` is true of an empty corpus. It now counts sanitizer applications and fails if the pipeline contains none — rename the extraction key and the guard goes red instead of quietly green |
> | 4 | `grade` **never read `bound`**, the flag fix 3 of the first pass added | A mistyped token (`create_recrod`) resolved `ok=False` → graded `GAP` → made its case **BLOCKED** and landed in `blockers` beside real holes, while `report.py`'s legend told the reader *"`GAP` — a declared token named a real thing"*. An unbound token is `INSTRUMENT-ERROR` now, kept out of `blockers` |
> | 5 | **the caselog never rendered the declaration.** The table had a `probe` column, `None` on eight of nine declared rows | W10's claim is that a wrong binding is *"an authoring error somebody can argue with"*. A binding no reader can see is no better than a regex no reader can see |
> | 6 | the kind token's stated semantics were **false in the flattering direction** — *"satisfied when the kind appears in a run"* for what is a **static table lookup** | `term.matured` published PASS because a Part D row *lists* the kind. Corrected in the docstring, the `detail` string and the caselog. **`W4` is the item that makes it a run** — today 25 of 40 declared kinds are emitted by nothing |
> | 7 | **`H-46`'s `cite` argued for a grade the row does not carry** — `H-20`'s conclusion, pasted | It satisfied `G6` (*a refusal nobody argued for is not a refusal*) on an argument for a DIFFERENT refusal, on a `tier: 0` row. The grade was right and the citation wrong; new register rule **`G12`** fails on recurrence |
>
> **And two the pass reported as observations, both real:** `verb_table.yaml` declared
> `writes_note` **twice** on `issue` and on `petition`, so `yaml.safe_load` silently discarded
> Part E's transcribed cell in the file whose whole purpose is fidelity to Part E. Both cells are
> merged, and `shape.load_yaml` is now the instrument's only YAML entry point and **refuses a
> duplicate key**. ⚠ Severity stated accurately: `writes_note` has no reader, so *that* instance
> lost transcribed text and not behaviour — what earns the guard is the same class at the ROW
> level, which did change behaviour (two `(Office, exists)` rows, gate behaviour depending on file
> order). `report.py`'s unused `defaultdict` import is gone.

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

**The list, computed rather than estimated — FROM A ROUTER-ERA `results.json`, and no longer
re-derivable** (reproduction command and its failure in §3.5). ⚠ Amended 2026-09-02 by `W10`'s
adversarial pass: the arc lane has **0 of 611 rows declared**, so nothing in the current
`results.json` produces this partition, and the token set it was computed over (`A3`, `W13`,
`P38`, `F3`, `F16b`) no longer appears in any `blockers` field. Treat the two rows below as the
**work list they were authored as** — which is all `W13` ever needed them for — and not as a
measurement anyone can check today. Re-deriving it is part of this lane: an arc gets its
`exercises:` before its re-authoring is judged.

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

## **W17 — THE SCENE CONTAINER.** *(Jordan's 2026-09-02 ruling, §3.4)*

**Do.** Add the scene as the level above the verb table — **the only structural change any ruling in
this chain has required, and it is additive.**

1. `budget` returns **scene actions**; `choose` returns at most that many **scenes**.
2. A scene carries its 1–3 verb applications. Both that bound and the **extended-scene cost of 2** are
   **register rows graded `assumption`**, citing `player_agency_v30.md` §6.3 as the default, with a
   declared sweep — **not constants**, because Jordan ruled the unit and the number and **did not rule
   these**.
3. **Re-express `P2x`.** It currently fails on *"`p_king` returned 8 acts against a budget of 5"*,
   which under the ruling is **lawful**. The propositions it should test are *"a person returned more
   SCENES than `budget` allows"* and, separately, *"a scene carried more interactions than the swept
   bound"*. **Leaving it as-is would be a probe asserting a rule the design no longer has.**
4. Re-state #353 §26.3's prose in scenes. **The spray argument survives the noun change unaltered** —
   five scenes each spent petitioning is exactly the triage the budget exists to create.

   > ⚠ **LANDED 2026-09-02 AS A REFUSAL TO EDIT #353, AND THE REASON IS THE POINT.** The W17
   > adversarial pass found this clause undelivered: `:896`, `:912-913` and `:922-923` still count
   > **acts**. They stay that way. **#353 is the specification under test**, `register.py
   > --verify-citations` pins ~40 register quotations to its line numbers, and an instrument that
   > edits its own subject to agree with a later ruling destroys the only fixed point the whole
   > chain measures against. The re-statement belongs in the surfaces that *derive* from it, and
   > that is where it landed: `Scene`'s docstring, `Query.budget`, `deliberate`'s refusal law,
   > `H-10`/`H-28`/`H-35`/`H-76`/`H-77`/`H-78`, `ARCHITECTURE_V2.md` §F3, and the
   > `act_budget` → `scene_budget` rename across 16 sites. **#353 `:1990` still lists "Does a scene
   > equal an act?" as open and that is correct of #353** — the ruling is Jordan's, dated after it,
   > and `A32` is where the instrument records that it is now settled.

**Does NOT change.** Parts D and E. The verb table's ~28 rows are the interactions; a level is added
above them. **This is the cheapest shape the ruling could have taken, and it is worth saying so.**

**Proof.** A person with `budget = 5` returning 6 scenes raises; a scene carrying 4 interactions
raises at the swept bound of 3 and **passes at the swept bound of `unbounded`, with the flip
reported**; `P2x` fails on scene count and no longer on interaction count.

**Size S–M.** Depends on **W3** and **W5**. ⚠ **On the critical path to `W9`** — artifact 2 cannot
count a season's activity until it knows what it is counting.

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

# PART 4B · THE SECOND ITEM SET — `W18`–`W32`, SEQUENCED ON **RUNNING** RATHER THAN GRADING

> **Added 2026-09-02, at Jordan's direction, after the first item set's critical path was completed
> and the goal was still not met.** `W0`–`W17` above are unchanged and stay citable; nothing in
> them is withdrawn. This part is what the plan did not contain.

## §4B.0 · Why the plan needed a second item set, stated as a defect in the first

**`PLAN.md` was written before any case had ever been executed.** Its instrument was
`run_cases.py`, which **grades** — it reads a case's prose `need` rows, looks up an authored
declaration naming the verb / hole / probe that answers each, and returns
`PLAYABLE / DEGRADED / BLOCKED / NOT-ASSESSED`. Every yield figure in Parts 2 and 5 is a grading
yield. Part 6's bar is **one** NPC season.

So the first item set optimised for a number that can rise while nothing runs, and it did:

| | measured | command |
|---|---|---|
| the critical path `W0→W1→W2→W3→W5→W17→W9` | **complete** — every item executes and is tested | `python -m pytest test_tracer_is_honest.py -q` (143 passed) ⚠ **NOT** `grep LANDED`: only `W0`/`W1`/`W4`/`W6`/`W10`/`W17` carry a note, which is `W19`'s subject |
| cases that GRADE as `PLAYABLE` | **0 of 143**, both lanes | `python run_cases.py` |
| cases whose season loop **runs** by §6.1's definition | **0 of 46 — INFERRED, not measured.** ⚠ **PARTLY SUPERSEDED 2026-09-04 — see `:1343`.** The inference rested on `N3` and on *0 Events whose cause is an Act by a different person*; the second is now 30 of 30 (NPC) and 54 of 59 (ARC). **`RUNS` itself is still 0 and this does not move it** — `RUNS` needs `R2`, which is NOT-COMPUTABLE | ⚠ no instrument computes it; that is `W18`. Derived from `N3` (no act cites its question, so no chain walks deliberation) and from **0 Events whose cause is an Act by a different person** — `python -c` over `headless.run(3,0)` comparing `causes[] → Act.actor` |
| arcs that reach an **ending** by §6.2's definition | **0 of 97 — INFERRED, not measured** | ⚠ same: no ending predicate exists (`W30`), `Q1` never forms (`N1`), and the contest branch cannot reach a subsystem (`N2`) |
| verbs that execute anywhere in the corpus | **6 of 32** | `python corpus_run.py` |
| Events whose cause is an **Act by a different person** | ~~**0** (21 acts, all Carin's)~~ ⚠ **SUPERSEDED 2026-09-04.** This is `R3`, and it is **30 of 30** on the NPC lane and **54 of 59** on ARC — the five misses being the five one-season cases, where the loop has no `t+1` to close in. See `:1343` and `H-102`; the zero is kept legible because it is what the row's inference rested on | `python -c` over `headless.run(3,0)`, matching `causes[]` against `driver.resolved[…].actor` |

⚠ **THE PATH IS EXHAUSTED, NOT WRONG.** Every item on it landed and each was worth landing — the
write gate, the resolver reading a table, the register computing its own counts, refusal-on-absence.
What the path never contained was an item whose proof was *a case running*. `§0.2` says done means
it runs; the plan's own bar said done means **one** thing runs, and one is what was delivered.

⚠ **AND THE INSTRUMENT THAT REVEALED THIS IS NOT IN THE PLAN EITHER.** `corpus_run.py` was built
2026-09-02 at Jordan's direction — *"shouldn't we consider running all NPCs and all arcs in our test
runs? a larger surface introduces more complexity, but given our goals, what solves one may solve
another while providing more pushback as to whether something is the RIGHT solve"* — and appears
nowhere in this document, either README, or `HANDOFF_IN.md`. `W18` fixes that first, because
**`§0.1` point 4 leaves every number below uncontrolled until it does**.

## §4B.1 · Five defects found by running, none of which had a register row

Each is assigned to the item that closes it (`G5`: findings are edits to the thing under review, not
a findings document).

| # | defect | measured | closed by |
|---|---|---|---|
| **N1** | **`Q1` is dead in the loop.** `calendar()` fires a Date and sets `fired=True`; `questions_for` at DELIBERATE the same tick requires `not fired`. The Q2 timing defect `W9` fixed, one barrier over. | ARC-01, 4 seasons: date fires at tick 1, docket populated, **`date_due` questions formed: 0** | **`W20`** |

⚠ **`W20` MUST ALSO MAKE CALENDAR EMIT, added 2026-09-04.** Closing `N1` gives Q1 a question to form; it does **not** give that question an antecedent. `calendar()` writes `Date.fired` through the gate with **no `emits=`**, so no Event carries a date id and `occasioned_by`'s `date_due` route walks to nothing — a Q1 that forms and cites nothing is `N3` again, one source over. `write_matrix.yaml` already declares `date.fired` for `(Date, fired)`; nothing emits it. `H-110` is the row.

| **N2** | **The loop cannot reach the contest seam.** `SeasonDriver.resolve` calls `contest(... claimants=[a.actor] ...)` — ONE party — so `combat_seam` returns `PARTY-GAP` and `contest()` raises. | a `kill / wound` act through `d.resolve` raises `Unspecified … needs two parties; got 1`; the same seam called directly with two returns `RESOLVED` | **`W23`** |
| **N3** | ✅ **CLOSED 2026-09-03 — and it was TWO edges, each hiding the other.** As written this row named one: *deliberation is absent from the causal graph; an act never cites what prompted it.* True, and fixing it alone moved nothing, because the second edge is that **a telling deposited a claim about the teller** — an Event that writes nothing fell through to its own subject, which is the actor — so §F1's Q2 could never fire for the listener and there was nothing to cite. `Scene` now carries `occasion : Question` and `Act` names its `scene` (the meta-architecture's own shape, Stage 4 `§B.9`), and a telling's deposit is about what was told. | 60 act-Events, **0** whose `causes[]` resolve to a question; 0 cross-person edges → **NPC `R3` 30 of 30, ARC 54 of 59**, `RUNS-ALONE-UNDECLARED` 64 → 5. ⚠ **The lane counters `NPC RUNS` and `ARC ENDS` are still 0 and this does not move them** — they need `R2`/`A2`, which `corpus_run.py` declares NOT-COMPUTABLE | ~~`W25`~~ — landed ahead of the item |
| **N4** | **Every corpus world has the same cast and the same motive.** `build_at` makes `p_a/p_b/p_c` with one shared OUGHT for all 143; `who_acts` (median 4, max 11) and `knowledge` are read by nothing. | 2 distinct executed sets over 86 worlds; the 5 that differ are exactly the 5 with `span_seasons: 1` | **`W27`** |
| **N5** | **A register `site:` is never checked to exist.** `H-32` is `assumption` with `site: sitting.judging_set`; no `sitting` symbol exists and `Query.judging_set` raises. `R2` tests non-emptiness only. | `grep -n sitting shape.py` → comments only | **`W19`** |

⚠ **`N2` QUALIFIES A CLAIM THIS CHAIN PUBLISHED THE SAME DAY.** Commit `e5a848e` says *"the seam
CALLS personal combat"*, and its 22/40-vs-13/40 condition measurement is real — **of
`combat_seam.resolve`**. It is false of any season run, because the loop hands the seam one
claimant. The seam is built and the call site is not wired to it. Recorded here rather than
softened in the commit message, which is pushed.

## §4B.2 · The four buckets — what actually stands between here and 143 running

**A · Blocked by a ruling already made. The corpus is wrong, not the architecture.**
**47 cases declare `scale: faction`** (NPC 18, ARC 29), and a faction acting is a *ruled refusal* —
`ARCHITECTURE_V2.md:93` (held under 143 cases), `H-21` ruled, `H-95` ruled, and `shape.py`'s own
*"a faction never acts: a PERSON HOLDING AN OFFICE acts"*. The origin is traceable:
`2026-08-31-shape-tracer/cases/CASE_BRIEF.md` gives the extraction schema as
`scale: <person | settlement | faction | realm | world>` — **the brief was written in a vocabulary
the architecture had already closed**, so every extractor used it. The fix is a corpus authoring
pass (`W28`), not a design item. ⚠ And re-scaling alone buys representability, **not behaviour**:
the re-scaled actor is an office-holder, and `person_side_eligible` declines every `remit:` verb
(`H-71`), so a re-scaled corpus without `W21` yields 133 worlds executing the same six verbs.

**B · Blocked by an open design hole.** `H-71` (9 of 32 verbs unformable person-side) · `H-94`
(`transfer` refused 86/86; nothing to act *on*) · `H-84` (nothing moves a Record → 0 cross-person
propagation) · `H-75` · `H-98` (winner vs degree) · `H-32` · `H-95`'s `world` half (10 cases) ·
`H-43/44/45/52/58/62` (one verb family each) · `H-33` (the flood, which is why `MAX_SEASONS=6`
exists) · `H-96` (the ranking decides by alphabetical tie-break for 15–20 of 22 candidates).

**C · Blocked by unbuilt code with no hole.** N1–N5 above, plus: `Event.subject` carries the actor
(so every witness deposits an identical, certain attribution — #353 §19.3's *"may be wrong… may not
conclude at all"* is unreachable) · `term.matured` bypasses the write gate and marks nothing ·
`work` emits success and changes nothing · no ending is evaluated anywhere · the `World.tenures`
rebuild is ~N³ (100 persons → **seconds per season, rising ~N³** (11.44 s when first measured; **5.11 s** on a re-run at 97 persons — the literal moves with the tree and the shape is what the row asserts)).

**D · Blocked by unauthored data.** 868 undeclared `exercises:` rows — **which serve grading, not
running** · 47 ARC cases with no ending classification · 47 `scale:` values in the wrong vocabulary
· 40 prose ARC spans · 143 casts that exist only as prose in `who_acts`.

---

# PART 4B.3 · THE ITEMS

Sizes as Part 4 uses them (S ≈ half a day, M ≈ one to two, L ≈ three or more). **Every proof is an
execution** (`§0.2`), and every yield is a measured count with its command, or is marked inferred.

## The instrument, and the board — first, because nothing after them is measurable

### **`W18` — THE RUN DEFINITION, AS AN INSTRUMENT.**
**Do.** `corpus_run.py` computes, per case, **every check that is computable today** — `R1`, `R3`,
`R4`, `R5` and `A1` — and prints one table per lane plus per-verb execution and cross-person edge
counts. Reads `ENDINGS_CLASSIFIED.yaml`. Refuses a prose span on an arc rather than defaulting one.

⚠ **A CHECK IT CANNOT COMPUTE REPORTS `NOT-COMPUTABLE` AND NAMES THE ITEM THAT CLOSES IT — it does
NOT score.** `R2` needs authored `exercises:` rows (8 of 143 cases have any) and a real cast
(`W27`); `A2`'s DECIDER and ROLL predicates need binding decisions (`W26`) and contest results
(`W23`) that do not exist yet; `A3` needs the case's own cast (`W27`). **An instrument that silently
scores an uncomputable check is the defect this chain has found in its own work five times** — a
number that cannot fail is not a measurement (§0.1 pt 2), and it flatters in the direction of
progress every time.

⚠ **THIS ITEM AND `W30` OVERLAPPED IN THE FIRST DRAFT OF THIS PART, AND THE OVERLAP IS RECORDED
RATHER THAN QUIETLY REMOVED.** `W18` was written as computing `A1`–`A3` while `W30` was written as
implementing `A2`, which is impossible for `W18` to have done: `A2`'s labels depend on mechanisms
`W23` and `W26` build. Caught on re-reading before any code was written. The split is now: **`W18`
builds the frame and reports the gaps; `W30` fills `A2` when its dependencies land.**

**Depends.** Nothing. **Size.** M.
**Proof — and the control is the PLANTED case, not the zero.**
1. **The control.** A planted world carrying one hand-built Act by a second person, caused by the
   first person's act, **flips that case's `R3` column from false to true** and flips no other
   case. Without it the instrument has demonstrated nothing: printing 0 on a corpus where 0 is
   entailed is not evidence of sensitivity.
2. It prints `NPC RUNS 0` and `ARC ENDS 0` today, against a corpus where 86 cases already "RAN"
   under the loose reading this replaces.
3. It prints a **non-empty** `NOT-COMPUTABLE` list naming `W23`/`W26`/`W27`.

⚠ **THE FIRST DRAFT CALLED CLAUSE 2 "THE CONTROL" AND IT IS NOT ONE** (§0.1 pt 4). It also had the
planted case flip a case to **`RUNS`**, which is impossible while `W18` itself declares `R2`
uncomputable — a status needing five checks cannot be reached with four. The control flips a
**column**, and `§6.1` gains `RUNS-UNDECLARED` so today's 27 completing cases have a status to be
in at all.
**Yield.** 0 cases, and every number after it.

### **`W19` — BOARD, REGISTER AND STALE-TEXT HYGIENE.**
**Do.** `LANDED` notes for `W2`/`W3`/`W5`/`W15`, which are done in code and open on the board — the
§0.2 board defect, in this document. **`W9` IS ON THAT LIST TOO, AND ITS NOTE WAS DELETED BY THIS
REWRITE** — it lived in the Part 6 that Part 6 replaced (*"LANDED 2026-09-02 — ARTIFACT 2 RUNS, AND
THE BAR IS NOT MET AS THIS SECTION WRITES IT"*), and §6.3 now quotes a block that no longer exists.
Restore it. Replace *"63 passed"* (**§2.1 and §10 Provenance** — not §9.1, which never carried it)
with the command; the file defines **143** tests. Correct
**`2026-09-02-executable-architecture/README.md`**, which still publishes the old bar (*"one NPC
season"*) and the old six-item critical path — ⚠ **not** `season-loop-tests/README.md`, which was
already corrected and calls `run_cases.py` the GRADER. A fourth `HANDOFF_IN.md` entry naming this
part; its last entry predates `W0`.

`register.py` gains **`S1`: every `site:` resolves to a symbol** (fails on `H-32` today, `N5`) and a
`kind:` roster (29 distinct values against the 5 `V2` declares). ⚠ Named `S1`, **not `R4`** — §6.1
already uses `R1`–`R5` for the run checks, and a second `R4` meaning "every site resolves" beside a
first meaning "reproducible" is the vocabulary collision `CLAUDE.md` §4 forbids.
`DEFAULT_FIXTURES` reads its values **from** the register's `default:` — one owner (§8), where today
12 pairs are duplicated and never compared.
**Depends.** Nothing. **Size.** S.
**Proof.** `register.py --check` fails `S1` before `H-32`'s site is real and passes `S1` after; a
planted fixture literal that disagrees with its register row fails. ⚠ **`--check` exits 1 today and
will keep doing so**: `R2` has 6 violations (`H-05`/`H-30`/`H-34` — `assumption` with no site and no
sweep) and `G6` has 15. This item does not clear them and does not claim to; whoever owns those rows
does. A green `--check` is not this item's proof and never was.

## The loop's dead edges — the critical path

### **`W20` — `Q1` FORMS.** *(N1)*
**Do.** `questions_for` reads Dates fired **this tick** (`fired_at == tick`, written by `calendar`)
rather than `not fired`.
**Depends.** `W18`. **Size.** S.
**Proof.** ARC-01's world forms ≥1 `date_due` question at tick 1 (**0 today**); a world with no Date
forms none.
**Yield.** **11 arcs today** — 19 `forced_by_threshold` exist but 8 are `faction`/`world`, so 19 is the
**post-`W28`** figure and the first draft published it without that condition. And the whole
Date → sitting → `determine` path becomes reachable at all, which is the larger half.

### **`W21` — `H-71`: AN OFFICE-HOLDER CAN FORM A REMIT VERB.**
**Do.** The barrier builds the View with `remits` — the union of `remit.acts` over Offices the person
holds, from their **own** `hold` Tenures. The View is *"BUILT, not filtered"* (S18) and `deliberate`
already holds the World, so this is a build-time widening, not `choose` reading the world.
`person_side_eligible` evaluates `remit:<act>` against `v.remits`. Grade `assumption`; sweep
**`[remit-as-a-CLAIM in the holder's ledger, view-carried, tenure-payload (H-50), decline (today —
the control)]`**.

⚠ **THE CLAIM-CARRIED ARM IS FIRST BECAUSE THE ARCHITECTURE'S OWN TEXT PREFERS IT, AND THE FIRST
DRAFT OMITTED IT.** A View field is world truth injected at build time and therefore *infallible* —
which is precisely what L2 says a person's basis for deciding must not be, and what §F1 means by
*"a filter on world truth would be `choose` reading the world"*. A remit deposited as a Claim when
`office.conferred` is witnessed makes a revoked holder **still believe** they hold the remit, form
the act, and receive `convene.refused` from the fold — T3 and L2 working, and the same shape §F1
already licenses for `requires`. It also leaves S18's *"at most K claim ids from the holder's OWN
ledger"* intact, where a `remits` field widens the View's definition for the second time (`W5`
added `question`). ⚠ The `tenure-payload` arm needs `H-50` to move first; it is `absent` with an
empty cite today.
**Depends.** `W18`. **Size.** M.
**Proof.** With `p_a` holding an office whose `remit.acts ⊇ {convene}`, `opening_set` offers
`convene`, and `test_no_person_can_choose_a_governance_verb_and_h71_is_why` goes **red as designed** —
that test's docstring already says it should.
**Yield.** **9 of 32 verbs** become formable; every DECIDER and THRESHOLD ending runs through them.

### **`W22` — `H-94`'s STRUCTURAL HALF: OPERANDS FROM THE PERSON'S OWN INTERIOR.**
**Do.** `Candidate` gains `operands`, derived person-side: the question's referent as target
(`kill / wound`, `tie / knot`, `succeed`, `oblige`, `tell`); the actor's own hearth as `from` and a
held-store claim as `kind`/`amount` (`transfer`); the subject Record as the `hold:` argument
(`destroy_record`, closing `H-75`'s placeholder for the actor's own holds). `pack_scenes` carries
them into `Act.payload`. ⚠ The bug half is already closed — the Candidate's `subject` reaches the
payload — and this is the half that needed a ruling on where operands live.
**Depends.** `W18`. **Size.** M.
**Proof.** `transfer` executes in ≥1 corpus world (**refused in 86 of 86 today**); and `transfer`
twice from a one-unit larder yields `.made` then `.refused` — **`W3`'s own proof clause, never
tested**.
**Yield.** +5 verbs, plus `destroy_record`.

### **`W23` — THE CONTEST BRANCH REACHES THE ENGINE.** *(N2)*
**Do.** `resolve` passes `claimants=[a.actor, payload.subject]`. The seam's dict becomes Events —
`contest.resolved{winner}` / `contest.unresolved` — and the winner's writes proceed through `_fold`
while the loser's are refused through `emits_on_refusal`. ⚠ Latent and fixed here: `out.extend(r)`
on a dict would extend the Event list with the dict's **keys**.

⚠ **AND `kill / wound` GAINS A `requires` PREDICATE AND AN EFFECT, WITHOUT WHICH THIS ITEM CANNOT
REACH ITS OWN PROOF.** It is excluded from `resolvable_verbs()` — no predicate, and the effect is
gated behind `contests:` — and `make_chooser(verbs=resolvable_verbs())` narrows the candidate set,
so **no person in any corpus world can form the act at all**. Wiring the call site while nothing can
call it would leave the proof satisfiable only by a hand-built Act handed to `resolve`, which is
exactly what `N2` already did. The first draft of this item omitted that and no other item carried
it. **Also required: the target must be a PERSON** — today a question's referent is a rung or a
Proposition, so `W22`'s operand derivation must yield a person subject here or the seam returns
`PARTY-GAP "claimant not a person"`.
**Depends.** `W22`. **Size.** S–M.
**Proof.** A `kill / wound` act **in the loop** produces a `contest.*` Event with `causes=[act]` and,
on a kill, `person.died` — today it raises `PARTY-GAP`. Result `0` produces `contest.unresolved`
and no death, honouring Jordan's 2026-06-02 ruling that an undecided fight is a legitimate outcome.
Determinism holds across two runs.
**Yield.** ROLL endings become reachable. ⚠ `H-98` stays open: the seam still mints no band.

### **`W24` — PROPAGATION: A RECORD MOVES, AND A WITNESS ATTRIBUTES.**
**Do.** (a) `H-84` by §0 test 4 (precedent). Possession is already a `hold` Tenure (#353 §13
extends `hold`'s domain to Records; §15 makes it 1-per-object), and the tree already **opens and
closes** such Tenures — `confer` writes `(Tenure, since) → tenure.opened` and `revoke` writes
`(Tenure, until) → tenure.closed`. Moving a Record is that pair applied to a Record's hold. ⚠ The
first draft called this *"the existing `transfer` shape"*, which **contradicts `H-84`'s own text** —
Part E's `transfer` moves `(Rung, stores)`, MATTER, not Records. The mechanism is precedent; the
name was an invention. The Do must **name the verb and its Part E row** — extend `transfer`'s
`writes:` to carry the Tenure pair, or add a row — and a Part E edit is a data change under `W3`'s
guardrail. Register `assumption`, control arm "Records never move".
(b) `Event.subject` becomes the **primary changed object**, and the ACTOR is deposited per-witness
as a Claim through the `witness_key` channel — restoring #353 §19.3's *"attribution is a per-witness
Claim… may be wrong"*, which the ruled `H-36` cites verbatim. (c) `term.matured` goes through
`write()` and marks the stage.

⚠ **Do NOT add a `target` or `actor` field to `Event`** — §19.3 rules them off. ⚠ **AND THE FIRST
DRAFT SAID THE ACTOR IS READ FROM `changes[]`, WHICH IS FALSE**: `changes[]` carries `StateChange`
rows about the *changed objects*, never the actor. Once `subject` is the changed object the actor is
on the Event nowhere at all, and the only resolver-side route is **`causes[] → act id →
`driver.resolved[…].actor`** — the same route `R3` uses and the same integrity surface `H-82`'s
`log ∪ resolved` names.

⚠ **WHAT ELSE MOVES, MEASURED BEFORE THE ITEM STARTS RATHER THAN DISCOVERED DURING IT.** Six readers
of `Event.subject` change meaning: `last_emission_of` (find-by-kind+subject), **`content_hash`** —
so **every golden and every published hash re-records, and `W11`'s artifacts with them** —
`claim_subjects`' fallback, **`_event_place`** (a Record subject has no `contain` Tenure, so record
Events become unwitnessable under `presence_only`/`all_five`, which changes what `H-33`'s sweep arms
MEAN), and **`_ch_witness_key`** (`pid == e.subject`, so an actor stops auto-witnessing their own
act under the narrow arms). Under the ruled `total` default nothing breaks at WITNESS; every hash
still changes.
**Depends.** `W22`. **Size.** M.
**Proof.** On NPC-088's world the bailiff forms ≥1 question and acts; **cross-person cause edges > 0**
(0 today); the three ledgers stop being identical (they are byte-identical today — same subjects,
all `True`, all confidence 95); ROOT count unchanged, which is `W4`'s guard still holding.
**Yield.** `R3` becomes reachable for every representable NPC case (inferred).

### **`W25` — THE DELIBERATION EDGE.** *(N3)*
**Do.** `Act` carries `question`; `resolved` acts carry `question → claim/date id`, so a walk goes
Event → act → question → the claim's deposit → the witnessed Event. `H-82`'s integrity check becomes
checkable over `log ∪ resolved`.
**Depends.** `W20`, `W24`. **Size.** S.
**Proof.** §6.3's check-2 chain walks **five links across two persons** on NPC-088 — unreachable
today, and the reason Part 6's bar was *"not met as §6.3 writes it"*. A planted act citing no
question fails integrity.

### **`W26` — THE SITTING DECIDES.** *(`H-32`'s default, built)*
**Do.** `Query.judging_set` per `H-32`'s stated default — holders of a `determine` remit whose scope
contains the venue. `determine` gains a predicate (fired Date + docket item + non-empty judging set)
and an effect. A vacant date fires and lapses (#353 `:835`). `H-32`'s phantom `site:` becomes real.
**Depends.** `W20`, `W21`. **Size.** M.
**Proof.** In one seeded run: `convene` → `date.scheduled` → next season `date.fired` → `Q1` →
`determine` → `matter.determined`, with `causes[]` walking the whole way. `F8`/`F21` flip. An empty
judging set produces a lapse Event and no decision.
**Yield.** DECIDER and forced-THRESHOLD endings — the two largest ending classes.

## The corpus becomes the world

### **`W27` — THE CAST COMES FROM THE CASE.** *(N4)*
**Do.** `build_at` reads `who_acts` (persons directly; roles become an Office at the case's rung
carrying the remit the role implies, from a per-case `cast:` block `W28` authors), `one_line` → the
OUGHT Proposition, `knowledge` rows → initial Claims and Records. Cast size is the case's, not three.
**Depends.** `W21`, `W22`; **`W28` must merge first** (both the re-scale and the `cast:` blocks);
**and `W29`**, which the first draft omitted — this item's own proof runs an 11-actor case, and an
11-person world is beyond the scan ceiling `W29` lifts. **Size.** M–L.
**Proof.** Distinct executed sets across the corpus **> 2** (2 today), and `H-96`'s discrimination
line moves. A case with 11 actors runs within `W29`'s budget.
**Yield.** Every case becomes its own world — which is the control for every number after it.

### **`W28` — RE-SCALE THE 47, RULE THE 10, CLASSIFY THE 47, AUTHOR THE SPANS.** *(authoring; parallel from day one)*
**Do.** `scale:` → a rung kind plus `office:` for the 47 faction cases. Fix `CASE_BRIEF.md`'s schema
line, which is where the wrong vocabulary entered. **The loader refuses a foreign scale at load**, so
it cannot recur — today `corpus_run` refuses at run time while `run_cases` grades faction cases
happily. ENDING labels for the 47 unclassified ARC cases. Integer spans for the 40 prose ARC spans
(the NPC lane may default). For `world` (10 cases): propose by §0 test 5 that a world is *the set of
realms* and re-scale to `realm` with ≥2 realm Rungs; escalate **only** if Jordan rejects that
reading.
⚠ **AND THE `cast:` BLOCKS — 143 OF THEM — WHICH THE FIRST DRAFT ASSIGNED TO NOBODY.** `W27`
depends on *"a per-case `cast:` block `W28` authors"* and `W28`'s Do did not contain one. It is the
largest authoring deliverable here: `who_acts` is prose (median 4 entries, max 11), and a world
cannot be built from it until each entry resolves to a person, an office at a rung, or a non-actor.
**Non-actor entries are part of the deliverable, not an omission** — ~44 of 97 ARC cases name a
player, a PC or the party, and those become `WAITS-ON-PLAYER` rather than a failure.

⚠ **ORDER INSIDE THE ITEM MATTERS.** Re-scale the 47 **before** the loader begins refusing a foreign
scale, or `load_cases` refuses them in the grader too and `run_cases.py` loses 47 cases while they
are being fixed.

⚠ **THE `world` HALF: DECIDED HERE, NOT ESCALATED — the first draft did both and they contradict.**
By §0 test 5: a `world`-scale case is instantiated as ≥2 realm Rungs under a shared container,
because `rung_kinds` has eight members, no in-chain text defines `world`, and re-scaling is the only
move that makes the 10 cases representable at all. Recorded on `H-95` and **removed from §9.0's
escalation list**. Jordan may overturn it; that is a ruling, not an open question this plan waits on.

**Depends.** `W18` (the vocabulary). **Size.** L.
**Proof.** `python corpus_run.py` → `UNREPRESENTABLE 0` (**57 today**) and `ENDING-UNCLASSIFIED 0`
(**47 today**); a planted `scale: faction` fails at load; every case resolves a `cast:` block or is
reported `WAITS-ON-PLAYER` naming the entry that caused it.
**Yield.** **+47 representable immediately, +10 on the `world` reading — the largest single number in
this plan.**

### **`W29` — SPANS, AND THE SCAN CEILING.**
**Do.** Cache `World.tenures` per barrier (`cache_at_barrier` already exists; invalidate on
`add_tenure` and any `until` write). Lift `MAX_SEASONS`. Keep `fan_out_mode=total` as the control
arm.
**Depends.** `W18`. **Size.** S–M.
**Proof.** 100 persons × 1 season in **under 1 s**, against a re-measured baseline stated with its conditions (5.11 s at 97 persons in one `d.season`; 11.44 s when first measured — ⚠ **carry the conditions, not the literal**, and the `70,104 view rebuilds` figure has no instrument that prints it and must not be republished until one does);
ARC-44 runs its full 16 seasons unclamped; suite wall time reported before and after.
**Yield.** 3 clamped arcs, and every cast larger than three.

### **`W30` — ENDINGS ARE EVALUATED.**
**Do.** §6.2's five `A2` ending predicates in `corpus_run` — the checks `W18` reports as
`NOT-COMPUTABLE` — plus `WAITS-ON-PLAYER` and `REFUSED-BY-L5`. `A3` lands with `W27`'s cast.
**Depends.** `W18`, `W23`, `W26`, **and `W24 → W25`** — which the first draft omitted and Part 5
confined to *"gates NPC RUNS"*. It gates the ARC lane too: DECIDER requires *"`causes[]` walks back
to an earlier Event by a different person"* and NEVER requires `R3`, so **30 of the 50 labelled arcs
(DECIDER 20 + NEVER 10) cannot reach `ENDS` without cross-person propagation.** **Size.** M.
**Proof.** ARC `ENDS > 0` with a per-label breakdown; and a `NEVER` arc whose content hash stops
moving is reported as a **fixed point**, not as `ENDS`.
**Yield.** The ARC number comes into existence.

## The coverage tail — parallel lanes, after the path

### **`W31` — VERB COVERAGE, GROUPED BY WHAT BLOCKS IT.** **Size.** L, itemised per verb.
(a) **No hole, merely unbuilt** — `commit`, `repudiate`, `oblige`, `tie / knot`, `forge`, `petition`,
`carry`, `succeed`. ⚠ **`commit` first**: `Q4` (a live `commit` to an OUGHT) is the only question
source that fires in a quiet season, and **no verb can create one** — every world seeds it by hand.
(b) **Hole-gated** — each lands only when its row moves by §0's ladder.
**Proof.** Per verb: `corpus_run`'s executed set gains it in ≥1 world.

### **`W32` — `work` DOES SOMETHING.**
**Do.** `work`'s delta lands in §27.3's accumulator; `H-86` splits into `emits_per_write` /
`emits_when`. **Size.** S.
**Proof.** Site condition moves after a `work` act, and
`test_w8_work_emits_a_success_while_repairing_nothing` **inverts** — a test that pins a defect
should die when the defect does.

### Items carried forward, reframed
- **`W13`** (arc re-authoring) — kept, but judged by `W30`'s `ENDS`, never by a grading verdict.
  Starts after `W28`. A rewrite that still ends `REFUSED-BY-L5` is a defect in the rewrite.
- **`W12`** (the twelve transitions) — kept, after `W30`.
- **`W10`** (declared routing) — **demoted**. Author `exercises:` for **core rows only** (~390),
  because §6.1's `R2` reads them. ⚠ **~390 is the UNDECLARED core count**, not the core count: 427 core rows exist (NPC 126 + ARC 301) and ~35 are declared. The 476 non-core rows are dropped.
- **`W11`** — its reproducibility and float clauses are covered by `W9` checks 1 and 6; only the
  `H-25` spiral and serial-vs-pooled clauses remain.
- **`W14`** (Godot) — stays deferred, and not before `W30`.

---

# PART 5 · SEQUENCE AND THE CRITICAL PATH — REWRITTEN 2026-09-02

> ⚠ **The previous Part 5 is superseded and its critical path is COMPLETE.**
> `W0 → W1 → W2 → W3 → W5 → W17 → W9` all landed, and the goal is not met. That path is
> **exhausted, not wrong** — see §4B.0. It is preserved in git history; every edge argument it made
> still holds for the items it sequenced.

```
W18 ──▶ W20 ──▶ W21 ──▶ W26 ─────────────▶ W30     deadline → office-holder → sitting → endings
  │       └──▶ W22 ──▶ W23 ───────────────▶ W30     operands → the contest reaches the engine
  │              └──▶ W24 ──▶ W25 ────────▶ W30     propagation → walkable deliberation
  ├──▶ W29 ──────────────────────▶ W27              [gates spans > 6 and casts > 3]
  ├──▶ W10-core ─────────────────────────▶ R2       [gates NPC RUNS — see §5.3]
  └──▶ W28 (authoring, parallel) ─▶ W27 ──▶ W30
W19 alongside W18.   W31 · W32 · W13 · W12 after W30, in parallel.
```

⚠ **THIS IS A TOPOLOGICAL ORDER, NOT A CHAIN.** `W22` does not depend on `W21`; `W26` does not
depend on `W23`. The arrows are dependencies; the linear reading below is one valid sequence through
them, not the only one.

**THE CRITICAL PATH TO "ALL 143 RUN": `W18 → W20 → W21 → W22 → W23 → W26 → W27 → W30`,** with
**`W28` merging before `W27`** (representability *and* the `cast:` blocks), **`W29` before `W27`**,
**`W24 → W25` before either lane can score** — NPC `RUNS` via `R3` and ARC `ENDS` via DECIDER and
NEVER — and **`W10-core` before any NPC case can reach `RUNS`** (§5.3).

## §5.1 · Two ordering choices, made rather than left open

**Loop fixes before the corpus re-scale**, though `W28` has the largest yield. Re-scaling first would
bank *"133 representable"* against a loop whose 133 worlds all execute the same six verbs — and that
number has already been banked once, as *"86 RAN"*, which `§4B.0` shows meant almost nothing. The
authoring runs in parallel from day one and merges at `W27`, so no time is lost.

**`H-71` before `H-94`.** DECIDER and THRESHOLD are the two largest ending classes and both run
through remit verbs; ROLL runs through operands and is smaller.

## §5.2 · Measured unblock yield, so the sequence can be argued with

| item | yield | basis |
|---|---|---|
| `W28` | **57 cases** | scale census, `run_cases.load_cases` |
| `W26` | **≤31 endings after `W28`** | DECIDER 20 + forced 19 overlap at 9; only 12 DECIDER are representable today. The first draft's `~31` was loose in both directions |
| `W20` | **11 arcs today, 19 after `W28`** | `forced_by_threshold` ∩ representable |
| `W21` | **9 of 32 verbs** | remit-gated verbs in `verb_table.yaml` |
| `W22` | 6 verbs | operand-gated verbs |
| `W24` | 27 → 45 NPC cases | inferred from an identical fixture |
| `W29` | 3 arcs + every large cast | clamped spans; `who_acts` sizes |
| `W31` | up to 20 verbs | the unbuilt/hole-gated split |

## §5.3 · The trace this plan owes, and the hole it exposes — `R2`

⚠ **COMPLETING THE CRITICAL PATH AS FIRST WRITTEN WOULD HAVE PRODUCED NPC `RUNS` = 0.** Traced
item by item: `R1` reaches 45 (46 with the `world` reading), `R3` becomes reachable through
`W24`/`W25`/`W27`, `R4` and `R5` already hold — and **`R2` stays at 0**, because it requires a core
`exercises:` declaration and only **8 of 143 cases have any**. The item that authors them,
`W10-core`, was placed *"after `W30`, in parallel"* and was a dependency of nothing.

A plan whose critical path cannot reach its own bar is the defect this Part exists to fix, arriving
in the fix. Two ways out, and this plan takes the first:

1. **`W10-core` joins the NPC path** — author core `exercises:` rows for the NPC lane (**~390
   undeclared core rows** of 427 core rows total; the first draft's "~390 core rows" conflated the
   two). It is authoring, so it runs in parallel with `W28` from day one.
2. *(Rejected.)* Redefine `R2` as "the named person executes ≥1 verb" and demote the declaration to
   a separate `DECLARED` column. Rejected because `R2` is the only check that ties a run to **what
   the case actually asked for**; without it a case "runs" by doing anything at all, and the bar
   stops being about the corpus.

⚠ **AND `ARC ENDS` CANNOT REACH 97 BY CONSTRUCTION** — which the bar must say rather than imply.
The ceiling is set by the plan's own statuses: `UNCLEAR` endings (3 labelled, plus a share of the 47
unclassified), `REFUSED-BY-L5` (an arc whose only ending is the threshold itself), and
**`WAITS-ON-PLAYER` — ~44 of 97 ARC cases name a player, a PC or the party in `who_acts`** — plus
the 14 refusal-only arcs §8.4 already names. **`ENDS` is not the goal for those cases; `RUNS` is.**
See §6.4.

---

# PART 6 · THE BAR — REWRITTEN 2026-09-02

> ⚠ **The previous Part 6 is superseded.** Its bar was **one** NPC season (NPC-088, Carin Vedel),
> and `W9` met it in form while its own check 2 did not: the chain it produced is one mechanism
> repeating, and the multi-person chain §6.3 describes is unreachable. The six checks are kept as
> `R1`–`R5` below, generalised from one case to the corpus. **A bar that one case can satisfy is a
> bar this plan has already shown can be met while nothing runs.**

**The bar is now two counts, one per lane, and they may never be averaged (`G10`):** the NPC number
counts **propagation**, the ARC number counts **endings**. They measure different things.

Both definitions are predicates over a run's own artifacts — `w.log`, `causes[]`, the ledgers,
`w.dates`, the content hash. **Editing a case changes the world that gets built; it cannot satisfy a
predicate about what that world then does.** That is what makes this bar unsatisfiable by writing,
which `§0.2` requires and the old bar's row 4 did not achieve.

## §6.1 · The NPC lane — "this NPC's season loop runs"

The world is built **from the case** (`W27`): the named person, holding the office the case names, at
the rung it names; the case's ambition as an OUGHT Proposition with a live `commit`; the rest of
`who_acts` present.

| check | predicate | today |
|---|---|---|
| **R1 completes** | every season returns; no `DESIGN-GAP`, no `INSTRUMENT-DEFECT` | 27 of 46 |
| **R2 acts through a declared verb** | the named person executes a verb the case's **core** `exercises:` names, attributed by act id; the declaration's `need_sha` must predate the run | not computed |
| **R3 propagates** | ≥1 **Act by another person** whose `causes[]` walks back to the named person's act, resolved via `causes[] → Act.actor` on `driver.resolved` | **0 of 46** |
| **R4 reproducible** | same content hash twice; the float arm differs | met for NPC-088 only |
| **R5 no fill off the register** | the fixture-read log ⊆ the register's `site:` set | met (`W9` check 3) |

⚠ **`R3` SAYS *AN ACT BY ANOTHER PERSON*, AND THE FIRST WORDING SAID *AN EVENT*, WHICH WAS
SATISFIABLE 711 TIMES OVER ON DAY ONE.** Every `claim.deposited` Event has a cause whose `subject`
differs from its own — that is what a witness deposit *is* — so an Event-level test would have
scored `R3` for all 27 completing NPC cases the moment `W18` shipped, and the instrument built to
say zero would have opened by saying twenty-seven. Measured: **711 of 711** deposits pass the loose
reading; **0** Events have a cause that is an Act by a different person, and only Carin ever acts.
`Event` carries no actor by ruling (#353 §19.3), so "by another person" **must** resolve through
`causes[] → Act.actor` on `driver.resolved` — which is also what `H-82`'s `log ∪ resolved`
integrity check is for. A check that cannot fail is not a check (§0.1 pt 2).

Statuses: `RUNS` (all five) · `RUNS-ALONE` (`R1`, `R4`, `R5`, and `R2`, but not `R3`) ·
**`RUNS-UNDECLARED`** (`R1`, `R3`, `R4`, `R5` hold and `R2` is uncomputable — the honest status for
a case that propagates while nobody has authored its `exercises:` rows, which is 135 of 143 today) ·
`HALTS` · `UNREPRESENTABLE`.
⚠ `ends_when: never` is **correct** for this lane — 38 of 46 NPC cases say it. An NPC loop is proven
by propagation, not by ending.

## §6.2 · The ARC lane — "this arc runs"

`R1`–`R5`, plus:

- **A1 · the span is honoured.** An integer `span_seasons` is run in full, unclamped. A prose span is
  `SPAN-UNAUTHORED` — refused, never defaulted.
- **A2 · the ending is reached within the span**, by the case's `ENDINGS_CLASSIFIED` label:
  - **DECIDER** — a `binding_decision` Event by a named cast member whose `causes[]` walks back to an
    earlier Event by a *different* person.
  - **ROLL** — a seam Event from a subsystem with two named claimants (**including result `0`**,
    which is a ruled legitimate outcome, not a failure).
  - **THRESHOLD** — `date.fired` → a `Q1` question for a named person → that person's binding act or
    refusal citing the date. ⚠ An arc whose *only* ending is the threshold itself is
    `REFUSED-BY-L5`: a crossing may never produce an outcome, and the corpus asking it to is a
    finding about the corpus.
  - **NEVER** — `A1` and `R3` across the full span, **and** `content_hash(N) != content_hash(N-1)`:
    the arc must still be moving. An arc that reaches a fixed point is reported as one, never as
    `ENDS`.
  - **UNCLEAR** — `ENDING-UNCLASSIFIED`.
- **A3 · cast coverage.** Every `who_acts` entry that is a person acts at least once. Entries that
  are not persons ("the faction", "the players") are reported `L1-REFUSED` or `WAITS-ON-PLAYER` —
  the arc ran to the point where a Date or Petition awaits a holder the engine does not supply.

Statuses: `ENDS` · `RUNS-WITHOUT-ENDING` · `WAITS-ON-PLAYER` · `HALTS` · `UNREPRESENTABLE` ·
`SPAN-UNAUTHORED` · `ENDING-UNCLASSIFIED` · `REFUSED-BY-L5`.

**Today: NPC `RUNS` = 0 of 46. ARC `ENDS` = 0 of 97.** Command: `python corpus_run.py`.

## §6.3 · Rulings this Part carries forward, because the register cites them

⚠ **THE CITATION GATE CAUGHT THIS REWRITE DROPPING A LIVE RULING, WHICH IS THE GATE WORKING.**
Replacing Part 6 broke `H-33`'s `cite:`, because that row quotes the superseded §6.2. A rewrite may
supersede an argument; it may not silently delete a decision the register depends on. Both are
restored here, verbatim where a row quotes them.

**The fan-out default.** The `H-33` default at this milestone is TOTAL FAN-OUT — #353's specified
behaviour — with `sweep: [total, presence, five]`. The five channel predicates are a **sweep arm**,
not the default: `G1` makes the instrument inject *the register's* default, so setting it to the
five predicates would have handed the milestone `W6`'s content — a presence index and office-scope
predicates — without anyone deciding it. `W6` has since built the predicates and measured the arms
— deposits fall by roughly a factor of ten, **711 → 66 measured today** (⚠ the `678 → 68` this
line and `H-33`'s cite both carried is a stale literal from an earlier tree; the factor holds, the
numbers moved) — and **the default still stands at `total`**, because #353
names the five channels and supplies no predicate for any of them; grading the row `ruled` on the
back of an implementation would credit the design with an answer this chain invented.

**The multi-person chain**, which `H-84` cites and which `§6.1`'s `R3` and `§6.2`'s DECIDER predicate
both now formalise: a claim deposited in **another** person's ledger → that person's `Q2` question →
**their** act. Links three through five are unreachable, and `H-84` is why — nothing moves a Record
to a second person. `W9` measured it and built nothing that could have fixed it; `W24` is the item
that does. The old Part 6 recorded this as *"the bar is NOT MET as §6.3 writes it"*; this Part
records it as a count that is zero, which is the same fact with an instrument attached.

---

## §6.4 · What "run all 143" means when `ENDS` is unreachable for some — the expected distribution

⚠ **THE GOAL SAYS *RUN*; THIS BAR'S ARC HALF COUNTS *ENDINGS*, AND THOSE ARE NOT THE SAME TARGET.**
Stating the expected terminal distribution is how the bar avoids promising a number it cannot reach.

| lane | terminal status | expected | why |
|---|---|---|---|
| **NPC** | `RUNS` | the goal is **46** | `R1` reaches 45–46; `R3` via `W24`/`W25`; `R2` via `W10-core` (§5.3) |
| **ARC** | `ENDS` | **fewer than 97, and that is correct** | the classes below are not failures |
| | `WAITS-ON-PLAYER` | ~44 name a player/PC/party in `who_acts` | the arc ran to the point where a Date or Petition awaits a holder the engine does not supply — **that is the arc running** |
| | `REFUSED-BY-L5` | some of THRESHOLD | a crossing may never produce an outcome; the corpus asking it to is a finding about the corpus |
| | `ENDING-UNCLASSIFIED` | 0 after `W28` | 47 today |
| | `RUNS-WITHOUT-ENDING` | the NEVER class, 10 labelled | correct for an arc authored not to terminate |

**So "all 97 arcs run" means: every arc reaches a terminal status that is not `HALTS`,
`UNREPRESENTABLE` or `SPAN-UNAUTHORED`.** `ENDS` is the subset that terminates *in the engine*.
Publishing only `ENDS` would report a design working as intended as a failure — and would create
pressure to invent an ending for an arc the corpus says has none, which is `G1` at the corpus level.

## §6.5 · `W9`'s landed record — RESTORED, because this rewrite deleted it

⚠ **THE PART 6 THAT THIS PART REPLACED CARRIED `W9`'s ONLY `LANDED` NOTE, AND REPLACING IT DELETED
THE EVIDENCE FOR THE ONE ITEM THE OLD BAR WAS ABOUT.** §6.3 then quoted a block that no longer
existed. A rewrite may supersede a bar; it may not delete the record of what was measured against
it. Restored verbatim from `7870283^`, unedited — its verdicts stand as they were written, and this
Part's two counts are what replaces the *bar*, not what replaces the *measurement*.

### ⚠ **LANDED 2026-09-02 — ARTIFACT 2 RUNS, AND THE BAR IS NOT MET AS THIS SECTION WRITES IT.**

Both halves are true and neither may be dropped. `python headless.py --case NPC-088 --seasons 2
--seed 0` completes, reproducibly, with a computed option set and no `effect` lambda. **The number
this plan is subordinate to went from zero to one.** What follows is what the adversarial pass
established about the six checks, recorded here because §7.3 binds this document to `G5`.

| check | state |
|---|---|
| **1** reproducible | **MET.** Byte-identical across runs; a different seed diverges |
| **2** a chain of ≥4 Events | **MET AT FOUR SEASONS, NOT AT THE PUBLISHED TWO** — and by ONE mechanism repeating, not by the chain this section describes |
| **3** zero fills off the register | **MET**, and getting there gave `site:` to four rows that had carried an empty one since `W0` |
| **4** no `effect`, no roster | **MET**, asserted over signatures |
| **4b** ≤ `budget` scenes, swept bound | **MET** |
| **5** `exercises:` before the run | **NOT MET AS WRITTEN.** Authored after; the file declares it and substitutes a cited outside source per row |
| **6** the float control fires | **MET** |

**Three things this section asks for that the run does not do, and none is a defect in the run:**

1. **The chain in §6.3 check 2 requires links this design has no verb for.** *"a claim deposited in
   another person's ledger → that person's Q2 question → their act"* is unreachable: nothing in the
   resolvable vocabulary moves a Record to a second person, so only its maker ever holds one and
   **only Carin ever acts**. That is `H-84`, graded `absent` — inventing a `give_record` verb to
   close it would be §8.1's first forbidden move.
2. **Checks 1 and 2 cannot both hold at `--seasons 2`.** The only chaining edge is term
   maturation, one stage per season, so the chain reaches `1 + seasons − 1`: depth 2 at two
   seasons, depth 4 at four. Both are measured and printed.
3. **The chain's length is `1 + record_stages_default`**, a number this session invented (`H-80`).
   Its `0` control is now executed rather than described: depth 1 · 4 · 7 at 0 · 3 · 6.

**What the milestone does establish, and it is not small:** the loop runs a season end to end from
a computed `q`, a computed option set and a table-driven fold; and running it found **eight defects
no amount of reading had found** — `causes=[ROOT]` everywhere (`H-82`), a dead Q2 (`H-04`), claims
that could only be about actors (`H-79`), Events carrying no `changes[]`, a `person.died` emitted
when nobody died, the verb table's `stratum` column reaching no resolver (`H-83`), `A28`
short-circuited since `W3` on the one invariant it exists to check, and `H-84` above.

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

Nothing here is ratified by merging it. It is `PROPOSED`, held back in full. ⚠ **`H-35` WAS an open
question to Jordan**, `H-36` a closure explicitly offered for objection.

---

# PART 9 · HOW TO FALSIFY THIS PLAN

> ⚠ **REWRITTEN IN PART 2026-09-02.** The first table's falsifiers were written for the first item
> set. Several have now FIRED, and a falsifier that fired is worth more than one that did not — the
> rows below record which, rather than being quietly replaced. The second table is the live one.

## §9.0 · The falsifiers that FIRED

| claim | how it was falsified |
|---|---|
| *"the whole plan: artifact 2 does not run after `W0–W5`"* | **artifact 2 ran, and the diagnosis was still incomplete.** One case running proved the diagnosis of *why nothing ran* was right, and proved nothing about the goal: 0 of 143 cases run by Part 6's current definition. The falsifier was too weak, not wrong |
| *"declared routing makes 60 cases assessable"* | never tested — **0 of 143 grade `PLAYABLE`**, and 868 of 903 rows are unauthored, so the antecedent never obtained |
| *"the register is now complete"* | **fired repeatedly.** `H-86` … `H-98` were all added by instruments needing a hole that carried no row. `V2`'s own falsifier, still firing against its successor |
| *"the escalation queue is empty"* | **fired.** `H-94`'s structural half, `H-98`, and `H-95`'s `world` half are live escalations, each a design choice with two defensible options |

## §9.1 · The live falsifiers — for the SECOND item set

| claim | what would prove it wrong |
|---|---|
| the critical path is `W18→W20→W21→W22→W23→W26→W27→W30` | a case that reaches `RUNS` or `ENDS` **without** one of the eight — show it — **or** a ninth item that turns out to block it |
| `W18` is first | any later yield figure that can be argued without it. §0.1 pt 4: name the control |
| the 47 faction cases are the CORPUS's defect, not the architecture's | a reading of `ARCHITECTURE_V2.md:93`, `H-21` or #353 under which a faction acts as an actor — the refusal is ruled, so this is falsified by overturning the ruling, not by disliking it |
| `W28` is the largest single yield | a re-scaled corpus that does **not** move `UNREPRESENTABLE` from 57 toward 0 |
| the bar cannot be satisfied by writing | **a case edit that flips a status without changing what the world does.** This is the load-bearing one: Part 6's predecessor failed exactly here, and if Part 6 fails it too the plan is measuring authorship again |
| propagation gates the NPC lane | an NPC case reaching `RUNS` with **0** cross-person cause edges |
| `H-71` before `H-94` | an ending class that runs through operands and outnumbers DECIDER + THRESHOLD |

| claim | what would prove it wrong |
|---|---|
| the critical path is `W0→W1→W2→W3→W5→W9` *(FIRST SET — historical)* | an artifact-2 run that completes without one of the six, **or** a seventh item that turns out to block it |
| `W0` is first | a re-grade, a matrix row or a verb row that can be written correctly **without** a graded register — show one |
| eleven of twelve `absent` rows close in chain | **a cited line that does not say what §3.1–§3.4 claims it says.** Every citation is a file and a line; check them |
| the 22-arc residue needs re-authoring, not design | a re-authored arc, expressed purely through §36.3's petition chain and §37's `tell`, that **still** routes to a refusal probe |
| **the whole plan** | **artifact 2 does not run after `W0–W5`.** Everything above is a hypothesis about why the tested version ran zero cases end to end. **One case running is the only evidence that the diagnosis was right.** |

## §9.2 · What would make THIS document done — §0.2's standard, applied to itself

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
| **Measured by** | direct execution during composition — `report.py`, `pytest test_tracer_is_honest.py` (**63 passed at composition; 143 today — run it**), and set-cover/verdict queries over `results.json`, each with its command in-line |
| **Corrections this document makes to its own author's prior work** | three, in §1.3: `H-23` (a precedent that would have overturned an explicit sentence of the specification), `H-36` (emitter- vs receiver-side, decided the wrong way), and the Part E verb-roster check (**a keyword search reported as a verified negative** — the same router failure the plan exists to end) |
| **Escalations** | **zero.** `H-35` was escalated and **ruled by Jordan on 2026-09-02** — *"5 scenes for a character to play per season"* — and is recorded at §3.4 with its consequences and the two `assumption` rows it creates. **Nothing in the FIRST item set was waiting on a ruling ⚠ **and that is no longer true of the document**: §9.0 records three live escalations — `H-94`'s structural half, `H-98`, and (until `W28` decided it) `H-95`'s `world` half.** |
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
