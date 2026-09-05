# Degrees of success across the ARC and NPC corpus — what 143 cases have never exercised

## Status: **PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## This is an INSTRUMENT and its output. It changes no head, no roster, no verb table, no code under test.

Per `CLAUDE.md` §2 a merge ratifies PROPOSED contents *by default*, with one exception — held back
**loudly** in the PR body. This is that mark. No `CURRENT.md` row moves, no `ED`/`PP` is allocated,
and **nothing in `proposals/2026-09-01-season-loop-tests/`, `architecture/`
or `systems/` is edited.** The sweep reads them and reports.

---

> ### THE HEADLINE
> **Every mechanical decision in the ARC and NPC corpus was flipped every way it could be flipped,
> and each fork was followed forward three decisions — over a SEASON-AWARE window, because
> `DELIBERATE` is a parallel map over a frozen world and decisions bind in order only across
> seasons. 3,204 forks across 89 cases; 801 excluded as having no live window; **2,403 scored, all
> of which genuinely changed the act taken and the event stream written. NOT ONE changed any of
> the next three decisions. Reconvergence: 100%.**
>
> **No decision in the corpus influences any later decision.** A person does something else, the
> world moves, a different narrative is written — and the next three deliberations present the
> same options and take the same pick.
>
> ⚠ **The cause is exact and it is not "the acts do nothing".** The world *does* change (controlled:
> fingerprint `b24bb0df` → `a0862f1e`, three distinct log hashes). `Query.opening_set`
> (`shape.py:2220`) has four clauses and **not one consults world state** — the only channel from
> what happened to what is decided next is a claim in the actor's own ledger, which is §F1's
> deliberate epistemic design. **That channel is closed.** `belief_contradicts` fires only on a
> claim whose `predicate ∈ PERSON_PREDICATES` *and* whose `value is False`. Measured over **4,800
> claims**: the predicate vocabularies are **disjoint**, and **zero** claims are falsy. Clause 4
> cannot fire.
>
> ⚠ **And the design's own way of making an alternative future is unavailable.** The v30
> counterfactual corpus branches by *"alternate degree"* in **7 of 11** scenarios. Across the whole
> corpus **no act has ever resolved at a degree of success** — the contest seam is unreached, and
> all 12 interpersonal verbs (`speak`, `tell`, `the six investigation acts`, …) carry **no degree
> column**, 6 of them writing no state at all.
>
> ⚠ **The fix for both was prescribed and not built.** `HANDOFF_NEXT.md` §2 — *"the real backlog"* —
> lists five root causes; **4 of 4 scorable ones are unmet and the fifth was never tested.** Row 2b
> is the discovery model: *a contest of capability against secrecy, emitting a Degree.* `H-72` and
> `F.24`/`H-94` — typing `requires` so a belief can reach a decision — are the same class.

---

## THE TAKEAWAY — what to extend, what to fix, in order

**The loop is open.** Acts happen, the world changes, and nothing that happened can alter what
anyone decides next. That is one bug appearing in three places, and the order below is a
dependency order, not a wish list.

| | edge | state | evidence | why this rank |
|---|---|---|---|---|
| **1** | **belief → decision** | **SEVERED** | 4,800 claims measured; `belief_contradicts` can read none | **the bottleneck.** Every other fix is inert without it — a consequence that cannot reach a decision is a log line |
| **2** | **outcome → magnitude** (degrees) | **ABSENT** | 0 acts resolve at a degree; 12 of 12 interpersonal verbs degreeless | a degree is a *magnitude on an edge*. Build the edge first or you get a better-labelled log |
| **3** | **world → belief** | **PRESENT, WRONG PAYLOAD** | 339,804 claims deposited, carrying event-kind predicates | cheapest of the three, and probably the shortest path to closing #1 |

### ⚠ CORRECTED 2026-09-04 BY A FABLE-TIER PLANNING REVIEW — the "one type mismatch" claim below was wrong in a way that would have caused harm

I wrote that the design's worked example is **one type mismatch from running**, and made that this
report's most actionable item. **It is one type mismatch AND one operand away, and doing the type
fix alone would be actively harmful.**

The refusals I measured are **operand-gap refusals, not world refusals.** `pack_scenes`
(`shape.py:2739`) puts **only `subject`** on the payload — the code comment directly above it says
so: *"`transfer`'s `stores(hearth(giver), kind) >= amount` still has no `kind` and no `amount` that
any part of the pipeline can carry."* So `_req_transfer` reads `give.get("from","")` → `""` →
`w.rungs.get("")` → `None` → **False**, and `_req_move` reads `to` → `None` → **False**.

**Every `transfer.refused` and `travel.blocked` in the corpus is a malformed act, not an empty
granary.** Open the belief→decision channel without first supplying operands and the first thing it
does is teach every witness a **false fact about the world** — *"the hearth cannot supply grain"* —
derived from an act that was never well-formed. `H-94`'s structural half is therefore **on** the
critical path, not behind it.

⚠ **A second correction, of degree rather than direction:** my "zero of 4,800 claims are falsy" is a
sample statistic for something true **by construction**. `witness()` mints every claim as
`Claim(cid, pid, subj, e.kind, True, …)` (`shape.py:4782`) — predicate is the Event kind, value is a
**literal `True`**, always. Disjointness from `PERSON_PREDICATES` is a theorem; I sampled what I
could have proved.

### The single most actionable thing in this report *(as corrected above)*

`opening_set`'s own docstring describes the feedback loop as working:

> *"a person who **wrongly** believes the granary full still forms the Candidate, acts, and gets
> `transfer.refused` from the fold. That is T3 and L2 working."*

**The fold does deposit that refusal.** Measured, a real one looks like:

```
holder=p_a  subject='r_hearth'  predicate='travel.blocked'  value=True
```

`belief_contradicts` requires `predicate ∈ {church_standing, grade, heritage, office, residence}`
**and** `value is False`. The deposited claim fails **both** conditions — wrong predicate
namespace, and recorded `value=True` (*"it is true that this was blocked"*) where the reader wants
`False`. **The feedback loop this design describes is already being deposited and is already
unread.** `H-72` (map a `requires:` note to a predicate) and `F.24`/`H-94` (type `requires`) are
the registered, unbuilt form of exactly this.

### What the 143 cases are actually asking for (ARM 10)

972 `season_requires` rows, 427 of them `core`. Demand ranked by cases wanting it, against what
the engine supplies:

| demand | cases | rows (core) | engine |
|---|---|---|---|
| accumulator / clock | 65 | 126 (63) | PARTIAL |
| threshold crossing | 60 | 96 (50) | PARTIAL |
| **belief / knowledge** | **58** | **105 (59)** | **SEVERED** |
| observability | 56 | 79 (41) | PRESENT |
| **roll / contest** | **51** | **89 (47)** | **ABSENT** |
| relationship / loyalty | 46 | 71 (33) | THIN |
| memory / persistence | 39 | 60 (29) | PRESENT |
| **investigation** | **37** | **63 (24)** | **INERT** |
| **social / speech** | **31** | **44 (12)** | **BINARY** |
| irreversibility | 25 | 27 (11) | PRESENT |
| **third-party substitute** | **22** | **25 (8)** | **BLOCKED by belief** |
| **DEGREE / partial outcome** | **19** | **27 (18)** | **ABSENT** |
| resource depletion | 16 | 21 (12) | PRESENT |

**113 of 143 cases (79%) touch at least one blocked family.**

### Per-case, and the lane split (ARM 11)

Full table: **`runs/CASE_PROFILES.md`**, one row per case.

- **Blocked `core` rows per case:** `0 → 59 cases · 1 → 37 · 2 → 27 · 3 → 10 · 4 → 6 · 5 → 1 · 6+ → 3`.
  **59 cases can be attempted for what they are for; 20 cannot be meaningfully attempted at all.**
  Worst: `NPC-086` Joren Bergvall, `ARC-06` The Debate That Won the Wrong Thing, `NSC-01` The
  Hunting Accident — 6 blocked core rows each.
- **The two lanes want different things.** NPC: *relationship/loyalty 46%, belief 41%,
  observability 37%, memory 35%* — an **interiority** profile. ARC: *accumulator 53%, threshold
  48%, roll/contest 43%, belief 40%* — a **machinery** profile. Both land at ~79% blocked, by
  different routes.
- **The demands that travel together** are the real throughlines: `accumulator + threshold` (34
  cases), `belief + observability` (33), **`belief + investigation` (24, both blocked)**,
  `accumulator + roll/contest` (24).
- **126 distinct demand signatures across 143 cases** — the corpus is genuinely diverse, not a set
  of variations on a few shapes. It is a real stress test, and that is why 79% coverage of its
  demand is a meaningful bar rather than an easy one.

---

## 0 · Scope — every case in the chain, and how that was checked

| | |
|---|---|
| **cases** | **143 — 46 NPC + 97 ARC**, from **all 11 case files** in the chain: `2026-08-31-shape-tracer/cases/{ARC1-3,NPC1-3}.yaml` and `2026-09-01-season-loop-tests/cases/{ARC4-6,NPC4-5}.yaml` |
| **runnable** | **89** (30 NPC + 59 ARC) — a case runs when its `scale:` is a rung kind, **after `apply_rescale`** |
| **unrepresentable** | **54** — `faction` and `world` are not rung kinds, so 38% of the corpus never enters the loop at all. ⚠ The per-scale split was previously quoted from `corpus_run.main()`, which `sweep.py` never calls — a number in this table with no instrument in the shipped run. Arm 0 prints it now. |
| **instrument** | `engine/season/` at `1e163ee` (PR #362), unmodified |

⚠ **`apply_rescale` is why this says 89 and an earlier draft said 86.** `corpus_run.run_case`
re-authors a case's `scale:` before testing it, so filtering the raw `scale:` silently measured a
smaller corpus than the instrument being audited. Caught by reconciling against `corpus_run.py`'s
own printed counts rather than trusting either number.

---

## 1 · THE FORKING EXERCISE — flip every decision, follow it three decisions on (ARM 9)

> ### ⚠ RE-MEASURED UNDER A SEASON-AWARE WINDOW — Jordan asked *"did you ensure that decisions bind in order?"* and the answer was NO. **The finding survives at full strength; the first version was partly entailed.**
>
> **`DELIBERATE` is a PARALLEL MAP OVER A FROZEN WORLD** — `shape.py:4204-4221` requires
> `w.frozen`, sets `w._in_parallel_map = True`, and the law reads *"the world is FROZEN from the
> end of MATTER to the start of RESOLVE. THIS IS WHAT MAKES THE MAP SAFE TO PARALLELISE."* So
> every person in a season deliberates against the identical pre-RESOLVE state: **decisions bind
> in order only ACROSS seasons, never within one.** Verified by printing the tick per
> deliberation — D0–D2 → tick 0, D3–D5 → tick 1, D6–D8 → tick 2.
>
> **Two ways that inflated the first result:**
> 1. a window counting same-tick decisions counts slots that **cannot** differ — with 3 persons, a
>    fork at a season's first deliberation had **2 of its 3 slots dead by construction**;
> 2. a fork in the **final season** had **zero** live slots and every one was scored
>    `reconverged`. **That is the larger half.**
>
> **The corrected run**, over 4 seasons with a window of 3 strictly-later-tick decisions:
>
> | | |
> |---|---|
> | forks probed | **3,204** (89 cases × 12 decisions × 3 alternatives) |
> | **excluded as `NO-LIVE-WINDOW`** | **801** — exactly the final season's forks, which the first version silently scored as reconverged |
> | scored, and genuinely changing the act | **2,403** |
> | **reconverged** | **2,403** |
> | **diverged** | **0** |
> | decisions changed within the window | `{0: 2403}` |
>
> **100%, now over a valid window.** The rate did not move; what moved is that it is earned. And
> the positional control is unchanged and independent of the window: **the acts differ at the fork
> index alone**, so every subsequent act by every person in every subsequent season is identical
> too.
>
> ⚠ One incidental: the claim-channel probe reports **4,800 claims at both 3 and 4 seasons**. That
> is not a copy-paste error — the per-person ledger is capped (§18's *at most K*), so it saturates
> and a fourth season adds no net claims. The disjointness result is unaffected, and is in any case
> a theorem rather than a sample (see the correction above).

**The ask, verbatim:** *"within each season for NPC or arc, there is a mechanical moment where x
occurs instead of y (and maybe z or more). I need you to explore what happens when each mechanical
that chooses x instead chooses NOT x, and then figure out how that will change the progression of
that simulation to the tune of three different mechanical decisions later each time."*

**The unit is a decision, not a season.** `make_chooser` (`shape.py:2447`) builds `ranked` — the
person's own scored, sorted candidate list — and `pack_scenes` consumes it. That is the only place
in the loop where a named alternative is passed over. So D0…Dn are the deliberations in order;
baseline takes `ranked[0]` at each; a fork takes `ranked[t]` at **exactly one** decision and
`ranked[0]` everywhere else; then the next **three** decisions are compared against the baseline's.

| | |
|---|---|
| cases | **89** |
| decision points forked | **every one**, up to 3 alternatives each |
| forks probed | **3,204** |
| excluded — no live window (final-season forks) | **801** |
| forks scored | **2,403** |
| forks that genuinely changed the act taken (control) | **2,403 of 2,403** |
| forks whose event log differs from baseline | **2,403** |
| **forks that changed any of the next 3 decisions** | **0** |
| **reconvergence rate** | **100%** |

### 1.1 · Why — and my first answer was wrong

I first wrote that the cause was *"the acts do not move that world"*. **Retracted.** The control
refutes it: forking D0 three ways moves the world fingerprint `b24bb0df` → `a0862f1e` and produces
three distinct log hashes. The fork is real in state *and* in narrative, and the next three
decisions are still identical — which is a stronger result than the one I first claimed.

The actual cause is in `Query.opening_set` (`shape.py:2220`), whose four clauses are the verb table
(static), `person_side_eligible(p, row)`, `q.referents`, and `belief_contradicts(p, row, subject)`.
**Not one consults world state.** That is §F1's deliberate epistemic design — Jordan, 2026-09-02:
*"our understanding of all other words and actions is subjective and singular."* The single channel
from what happened to what is decided next is therefore a **claim in the actor's own ledger**.

### 1.2 · That channel is closed, and it is measured

`belief_contradicts` (`shape.py:2537-2560`) returns True only for a claim with
`predicate ∈ PERSON_PREDICATES` **and** `value is False`.

| | |
|---|---|
| `PERSON_PREDICATES` | `church_standing · grade · heritage · office · residence` |
| predicates the corpus actually deposits | `claim.decayed · condition.worn · news.told · proposition.uttered · record.created · site.worked · speech.made · stores.changed · transfer.refused · travel.blocked · yield.taken` |
| claims examined | **4,800** |
| claims with `value is False` | **0** |
| …and predicate in `PERSON_PREDICATES` | **0** |

**The two vocabularies are disjoint and no claim is ever falsy.** Clause 4 cannot fire, so the
candidate set is invariant with respect to everything that happens. A person deposits thousands of
claims, the world moves, and not one claim can reach the function deciding what they may do next.

`H-72` registers exactly this — *"the mapping from a `requires:` note to a predicate"* — and
`F.24`/`H-94` is typing `requires`. Both unbuilt, the same class as §10's five.

## 2 · What the corpus reaches, and what it does not (ARM 0)

| decision site | firings | in cases |
|---|---|---|
| `E2/S27.1` | 3,426 | 89 |
| `S31.1` · `S27/S32` · `S28/S61` · `S29` | 482 each | 89 |
| `S24` | 22 | 11 |
| **`S39`** — the contest seam | **0** | **0** |
| **`S39.3`** — the depth cap | **0** | **0** |
| **`S39.4`** — the degree ladder's margin model | **0** | **0** |
| **`S27.4`** — the Ob/Pool refusal, the only other roll-shaped branch | **0** | **0** |

**Six sites reached, four never.** All four of the unreached ones are the roll-and-degree surface.

⚠ **The S39 counter alone cannot carry that conclusion, and an earlier draft rested it there.**
`S39` as a `TRACE.decision` exists at **one** site (`shape.py:4957`), reached only *after* a
personal-combat dispatch returns `RESOLVED`; the other three `S39` sites are raises. **`S39.4` has
no `TRACE.decision` at all** — it is only the `where` of a raise — so its zero is *vacuous* and
cannot observe the failure it excludes (§0.1 pt 2). And a contested act reaching `resolve()` would
raise `Forbidden` at `shape.py:4611` first, because `corpus_run` calls `season()` with no
`contest_max_depth`. All three are raises and produce no DECISION row.

**The load-bearing evidence is the status histogram**, which the README did not previously cite:
`{RUNS-UNDECLARED 59, UNREPRESENTABLE 54, SPAN-UNAUTHORED 25, RUNS-ALONE-UNDECLARED 5}` — **zero
`DESIGN-GAP` and zero `INSTRUMENT-DEFECT`**. `run_case` converts every `ShapeGap` and `Forbidden`
into one of those two, so zero of both rules out the raise paths the S39 counter cannot see.
Together with `S39 == 0`: no contest was dispatched **and** none was attempted-and-refused.

⚠ **Every count in the table above is double the corpus.** `corpus_run.run_case` folds the season
**twice** — the measured run and the `R4` determinism replay — and the census clears its trace once
per case. Signature: `S24` reads 22 firings in 11 cases, i.e. 11 × 1 × 2. Halve for a per-corpus
figure. Zero doubled is still zero, so the finding is unaffected; the denominators are not
per-corpus and saying so is cheaper than a second run. Also: `S27.4`'s zero is **entailed, not
discovered** — `shape.py:4592` in the file under test already states that `Act.obstacle` defaults
to `None` and the computed chooser never sets one.

## 3 · Why: the degree road is built and has no on-ramp (ARM 2a)

`kill / wound` is the **only** verb in the 32-row table declaring `contests:`, and it is not in
`resolvable_verbs()` (12 of 32) — so the chooser can never propose it and `contest()` is
unreachable from `season()`.

⚠ **My first statement of the reason was false and is retracted.** I wrote *"not foldable — no
predicate, no effect"*. It **has** an effect (`_eff_kill`, `shape.py:3847`) and its
`requires: "—"` is in `NO_PRECONDITION` (`shape.py:3651`), so both of those gates **pass**. The
exclusion comes entirely from the third gate, `contested = bool(row.contests)`
(`shape.py:2336-2337`). The distinction is load-bearing for a reader: acting on "add a predicate
and an effect" would change nothing, because what excludes the verb is precisely that it *is*
contested — the fold defers it to the seam by design. My own §6.2 analyses `_eff_kill` at length,
so the README contradicted itself. Found by the adversarial pass.

**Forced past the chooser, the seam works.** `combat_seam.resolve` loads
`systems/combat/combat_engine_v1` by path and the live engine really fights: `status=RESOLVED`,
`resolver=d_sigma`, a winner, a bout count and a full `wound_state`. The road is real. Nothing
drives onto it.

## 4 · Person-to-person: speaking, arguing, investigating, accusing (ARM 5)

### 3.1 The chain's interpersonal surface is degreeless

| verb | `contests:` | `writes:` | grade |
|---|---|---|---|
| `speak` | — | `[]` | assumption |
| `tell` | — | `[]` | ruled |
| `the six investigation acts` | — | `[]` | assumption |
| `refract` | — | `[]` | absent |
| `comply` · `evade / defy` | — | `[]` | ruled |
| `utter` | — | `Proposition.exists` | assumption |
| `petition` · `carry` · `oblige` · `repudiate` | — | one field each | ruled |
| `determine` | — | `Tenure.degree` | **absent** |

**12 of 12 carry no degree column. 6 of 12 — `speak`, `tell`, `the six investigation acts`, `refract`, `comply`, `evade / defy` — write no state at all.** An argument, an accusation, a
piece of news and an investigation finding are each one Event and nothing else.

### 3.2 The route is declared from one end and unclaimed from the other

`rosters.yaml` maps four prizes to subsystems. Verbs claim **one**.

| prize | routes to | claimed by a verb? |
|---|---|---|
| `the body` | `personal_combat` | ✅ `kill / wound` |
| `a standing` | `social_contest` | ❌ **nothing** |
| `a proposition` | `social_contest` | ❌ **nothing** |
| `a field` | `mass_battle` | ❌ **nothing** |

**3 of 4 declared prizes are unreachable.**

### 3.3 The four bands ARE live — on one wired game of an unfinished engine

⚠ **Jordan, 2026-09-04: *"Please note that social contest is an unfinished engine."*** Measured
from the wrapper's own `GAMES` table: `agon` **WIRED**; `consensus`, `negotiation`, `inquiry`
**STUB**. **One of four.** Every number below is the Persuasion Track only.

`resolver.py:307` calls `DEGREE_ORDINAL[degree_from_net(net, base_ob, extension=..., pool=pool)]`
— the owner's ladder from `engine/autoload/dice_engine.py`, with the contest's one declared
`BandExtension` consulted on the top band only. Over 120 seeded contests, **all four bands are
occupied**. The live figures are in `runs/SWEEP_LOG.txt`; read them there rather than from this
paragraph.

⚠ **Two corrections here, both from the adversarial pass.** (i) This arm was **unseeded** while
`sweep.py` logged *"every draw in this instrument is seeded"*; `resolver.py` draws from
module-level `random`, so its published distribution drifted between runs and the numbers I first
quoted matched no artifact. It is seeded now and the sweep's seed claim is narrowed to what it can
carry. (ii) I called the denominator *"exchanges"*. It is **`_reception` calls** — `resolver.py`
loops `for i in range(budget): for side in (A, B)`, two log rows per round, and `_reception` is
called only on the rebut and advance branches. `pass`, `support`, `shift`, evidence, `barred` and
irrelevant-ground mint no degree, so receptions < log rows and the two must not share a word.

⚠ **The stub that matters most is `inquiry`, and it compounds §3.1 rather than offsetting it.**
Investigation has no resolver at **either** end of the seam: a stub game on the subsystem side, an
inert one-row verb on the chain side.

## 5 · The depth-3 four-band exploration on a persuasion contest (ARM 5d)

A **decision point** is one `_reception` call — the single site that mints a degree. ⚠ **Not "one
per exchange", which is what I first wrote and is false**: `_reception` is skipped on `pass`,
`support`, `shift`, evidence, `barred` and irrelevant-ground moves. The first three **receptions**
are forced to each of the four bands — **4³ = 64 trajectories × 40 seeds =
2,560 contests.** The degree is *supplied*, never computed: `degree_from_net` still owns what a
band means and `_advance` still owns what it does.

| opening band forced to | A's win rate | mean exchanges | opponent's peak |
|---|---|---|---|
| Failure | **5.2%** | 15.74 | 8.711 |
| Partial | **11.1%** | 15.16 | 8.495 |
| Success | **24.1%** | 13.88 | 7.934 |
| Overwhelming | **46.2%** | 10.65 | 6.233 |

**The ladder discriminates strongly and is monotone in win rate** — roughly doubling per band —
and win rate across the 64 trajectories spreads the full 0.000–1.000.

⚠ **Whose bands these are, corrected.** The forcing hook is side-agnostic and `resolver.py:443`
iterates `for side in (A, B)`, so the three forced positions are **A's opening, B's opening, A's
second** — not three of A's own decision points, which is what I first implied. The axis-1 control,
which the adversarial pass ran from my own shipped data before I did, gives A's win rate
**46.9 → 23.8 → 10.3 → 5.6%** as *that* band rises — strictly decreasing, the mirror of the table
above, which is exactly what an opponent's band must do. Axis 2 rises again. That settles the
identification and **strengthens** the axis-0 reading rather than weakening it. The arm now runs
both controls.

⚠ **The baseline that belongs beside the table.** Unforced, with identical parties and identical
policies, **A wins 28.3%** — the engine is asymmetric before any forcing (A moves first each
round). So 46.2% is *well above* a 28.3% baseline and 5.2% *far below* it; I first printed the
marginal with no baseline at all.

⚠ **4 of the 64 trajectories are one trajectory.** `(Overwhelming, Failure, *)` ends after a single
round under `ProofBar(bar=2.0)`, so the third forced band is never consumed and those four rows are
byte-identical. Arm 3 tracks `reached_depth` for exactly this; arm 5d did not, and now says so.

⚠ **RETRACTED, and recorded rather than smoothed.** The first version of this control measured
*mean peak advance* and reported **NON-MONOTONE** (Failure 6.877 > Overwhelming 6.624). Withdrawn:
an Overwhelming opening **ends the contest sooner** (10.7 exchanges vs 15.7), so a running total
falls as the opening improves for a reason unrelated to the ladder's order. Caught by measuring
contest **length** per band, which the first control never looked at (§0.1 pt 1 — attack the
setup, not only the statistics).

⚠ **Seeded, and the first draft was not.** `resolver.py` draws from module-level `random`, so the
unseeded tree gave 49/64 then 52/64 for the same enumeration. A tree that does not replay is not
evidence.

## 6 · Forced onto the degree road, the code does not accept the result

Jordan, 2026-09-04, on combat: ***"the combat engine determines the result there. your code just
has to accept the result."*** Taking that as the test, **three independent mechanisms break it.**

### 5.1 `emits_at` has ZERO callers — so every degree emits the union

`VerbRow.emits_at` is defined at `shape.py:701` and **referenced nowhere else in the tracer**. The
fold emits from `row.emits` (`shape.py:4507`) — the flat union of all branches. Executed:

| forced degree | emitted | person deleted? |
|---|---|---|
| `Felled` | `person.died`, `body.changed`, `contest.undecided` | yes |
| `Wounded` | `person.died`, `body.changed`, `contest.undecided` | **yes** |
| `Untouched` | **`person.died`**, `body.changed`, `contest.undecided` | no |

**A contest resolved `Untouched` announces a death.** This is the same defect class the chain
already caught once — *"Artifact 2 published four fabricated deaths… `person.died` is one of the
three endings §6.3's own chain check accepts"* — returning through the degree door. The `earned`
guard does not catch it, because on `Untouched` `_pairs` is empty, so the effect never runs, so
the refusal branch inside `if _pairs:` is never evaluated.

⚠ **#362 applied `ID-13` — *a declared field reaching no reader is one that does not exist* — to
delete `Tenure.conferrer`. It did not apply the same test to `emits_by_degree`, which it added in
the same revision.**

### 5.2 The effect is degree-blind, and its default harm is the whole body

`_eff_kill(w, a)` takes **no degree parameter**, and `int(d.get("harm", p.body))` defaults harm to
the person's entire body — so body reaches exactly 0, `if p.body > 0: return None` is passed, and
`del w.persons[who]` fires. **`Wounded` deletes the person.** Even with the bands ruled, the effect
cannot honour them.

⚠ **A scope claim here was wrong and is narrowed.** I wrote *"every computed act omits `harm`, so
every kill/wound is lethal"*. A computed act omits `subject` **too**, so `w.persons.get(who)` is
`None`, `_eff_kill` returns early (`shape.py:3858-3859`), `changed` stays empty and the fold takes
the **refusal** branch (`:4480-4485`). A computed `kill / wound` is therefore *not* lethal — it
writes nothing and emits the refusal. The correct and weaker claim: **any `kill / wound` that names
a subject and no `harm` is lethal at every degree** — which is reachable from a hand-built act, and
is exactly what this sweep's own arm 3 constructs. Found by the adversarial pass.

### 5.3 The degree guard raises `SystemExit`, which the run cannot catch

`writes_at`/`emits_at` raise `SystemExit` — a `BaseException`. `corpus_run.run_case` catches
`InstrumentDefect` (`:343`) and the `ShapeGap` family (`:350`). Executed under those exact clauses:
**`ESCAPED BOTH CLAUSES`.**

The guard's *direction* is right and `shape.py:4441-4447` says so — loud beats a silent full kill.
Its *mechanism* is the finding: of 18 `SystemExit` raises in `shape.py`, **14 are load-time and
correctly fatal; the 4 run-time ones are exactly the degree branches** (`:708 :712 :728 :733`),
and they are the only run-time refusals that bypass the typed-gap taxonomy. They produce no
`DESIGN-GAP` row, no `kind` histogram entry and no §-citation, and they **end the process**, so a
one-case design gap becomes a whole-corpus run termination.

### 5.4 The seam returns two degree surfaces that contradict each other

`combat_seam.resolve` returns both `winner` and `wound_state`, and names the latter *"THE DEGREE
SOURCE"*. Over 300 seeded fights, **the reported winner is the FELLED fighter in 6.06%** —
`wrapper.py:493`, `if result!=0 and rng.random()<cfg['UPSET_FLOOR']: result = -result`, which
inverts the result after the fell was recorded and never touches the wound trackers. Independently
cross-confirmed from a different quantity: **28 of 595 "losers" are not at health 0 (4.7%)**.

The inversion is a deliberate designer rule (`UPSET_FLOOR=0.05`, ED-PC-0036).

⚠ **I wrote that the desynchronisation was "undeclared anywhere". False, and retracted.**
`config.py:295-304`, at the constant's own definition site: *"the trace stream emits
`engagement_end felled=X` and then `fight_result winner=X`, **with no in-model event corresponding
to the reversal**"*. I cited `wrapper.py:493` and never opened the constant I was naming. The
narrowed claim that survives: **`combat_seam` names `wound_state` THE DEGREE SOURCE and returns
`winner` beside it without repeating that warning**, so a caller reading only the seam would not
know the two disagree. Under Jordan's rule the resolution is not an escalation: accept
`wound_state`, which is what the seam's own docstring already says.

⚠ Also: the measured figure is **6.06%**, not "~5%". Rounding it to 5% made it agree with
`UPSET_FLOOR` and with the 4.7% cross-check more tightly than the data does.

## 7 · Ladder arity, and a retraction of my own (ARMS 1, 4b)

`kill / wound` declares **three** branches. Handed the canonical four
(`Overwhelming/Success/Partial/Failure`), it admits **0 of 4**; handed its own three, **3 of 3**.

⚠ **AN EARLIER READING OF THAT 0/4 AS A GAP IS RETRACTED (Jordan, 2026-09-04):** *"why would there
be four bands for combat data? the combat engine determines the result there."* The four bands are
for a roll **the loop itself** makes. A contested act **dispatches**; the subsystem decides. So
`Felled | Wounded | Untouched` mirroring the engine's own terminal states is **correct**, and the
0/4 refusal is correct behaviour. Arm 4b's original question — *"can four bands be read off the
combat data?"* — was the wrong question and is withdrawn with it.

⚠ **A stale count, found in passing:** `shape.py:4656` says *"`kill / wound` declares its **four**
branches in `verb_table.yaml`"*. It declares **three**.

## 8 · `content_hash` is a hash of the LOG, not of the WORLD (ARM 4a)

`shape.py:2026-2033` iterates `self.log` only — it reads `w.persons`, `w.tenures`, `w.sites` and
`w.rungs` **not at all**. Demonstrated: delete a person from one of two identical worlds with no
Event appended, and the hashes still match.

`R4` is named a **load-bearing control** in #362's body ("the byte-identical `corpus_run` output").
It pins that the **event stream** replays identically. It does not pin that the **world state**
does. That is a narrower guarantee than the name suggests.

## 9 · A second flexibility reading — whole-season substitution (ARM 7)

**The question Jordan put centrally:** *"mechanical explorations of alternative outcomes within
each arc/NPC season at a depth of three so that we can assess flexibility."*

**The branch.** `make_chooser` (`shape.py:2447`) scores every candidate person-side, sorts DESC by
score then verb then subject, and hands the ranked list to `pack_scenes`. Branch `k ∈ {0,1,2,3}`
makes the person spend the season on their **k-th-ranked option alone**. Depth 3 seasons →
**64 trajectories per case × 89 cases = 5,696 runs, all completed, none raised.**

⚠ **Nothing in the decision rule is replaced.** `score`, the sort key, `align`, `stance_toward`,
`urgency`, `ask_budget` and `pack_scenes` all run unmodified; the sweep narrows the slice to one
candidate the person's *own* ranking produced. That is a counterfactual, not a second policy.

| measure | result |
|---|---|
| distinct **LOG** futures per case | **64 of 64 — for all 89 cases** |
| distinct **WORLD** futures per case | **8 (17 cases) · 9 (18) · 10 (2) · 27 (16) · 28 (32) · 29 (4)** |
| distinct executed-verb sets per case | 7 (52 cases) · 14 (37 cases) |
| **mean flexibility** (distinct worlds / trajectories) | **0.3093** |

**Read it this way: the narrative layer is fully expressive and the world layer is not.** Every one
of the 64 alternatives writes a different event stream; between 12% and 45% of them land on a
different world. The corpus is bimodal — roughly half the cases reach ~8-10 distinct worlds, the
other half ~27-29.

⚠ **Measured on a world fingerprint, not on `content_hash`.** §7 showed `content_hash` hashes the
log only, so a flexibility number built on it would have reported **64 of 64** and called log
divergence world divergence. The two columns above are exactly that gap.

### 8.0 · ⚠ CORRECTED — the budget DOES bind, at a declared sweep point

I reported that the engine has *no* native x-instead-of-y moment and that exclusivity had to be
introduced by the instrument. **Half wrong.** At `DEFAULT_FIXTURES` the budget is
`scene_budget=5 × interactions_per_scene=3` = **15 slots** against ~7 candidates, so it does not
bind. But `interactions_per_scene` is **swept `1 / 3 / unbounded`** on `H-76`, and at the declared
`1` point the budget is **5 slots against 7 candidates — it binds natively.**

So the honest statement is: **the budget does not bind at the default fixture point, and does bind
at a declared alternative the register already carries.** My `H-117` row is mis-kinded as
`ABSENT_RULE`; the rule exists as data. The defect underneath is `H-96` — *which* candidates survive
is decided alphabetically.

⚠ **And a third correction that bears on this arm's design:** RESOLVE re-sorts every act by
`(stratum, hash)` (`shape.py:4570-4571`), so **within-budget rank order is inert at RESOLVE by
design.** A fork that reorders inside the budget changes nothing and must not be scored as
reconvergence — only a fork that changes the *set* is a fork. My substitution branch does change
the set, so the measurement stands; but the *native* fork is at the budget boundary and that is
what a future run should use.

### 8.1 · A null result this sweep produced, and why it was wrong (ARM 7c)

The first version of this arm **rotated** the ranked list so the k-th candidate *led*, and all four
branches produced byte-identical worlds — flexibility 0.0156, a clean and impressive-looking null.
**It was an artefact.** A spy confirmed the patch was firing (3 calls, ranked lists of 7), so the
cause was elsewhere: **the act budget is not binding.** Every person takes **all 7** of their ranked
candidates every season — 3 deliberations × 7 = 21 acts resolved, all of them, in **12 of 12**
sampled cases. Rotation therefore changed the *order* and never the *set*.

**That artefact is itself a finding.** §26.3 makes triage *"the PERSON's own choice of what to leave
undone"*. In 143 cases nothing is ever left undone, so the ranking **orders** acts and never
**selects** among them, and the person's convictions cannot express a refusal. Compounding it, the
ranking mostly ties: `align` is sparse with `default_cell: 0.0`, so only **2–7 of 22** candidates
carry a nonzero score and the rest sort alphabetically by verb name.

## 10 · The design's own counterfactual standard, and how much is reachable (ARM 8)

`tests/stress/emergent_arc_2026-04-17_batch8_counterfactual.md` at `v30-snapshot-2026-06-28` is 916
lines of this exact exploration, done by hand in 2026-04. Its declared method: *"takes the path NOT
taken (**alternate degree**, alternate NPC choice, alternate trigger), and traces the emergent
consequences forward."* Eleven scenarios, classified on their own verbatim `ALTERNATE PATH:` line:

| axis | scenarios | engine reach |
|---|---|---|
| **DEGREE** — a roll inverted, a contest lost, "Failure degree" | **7 of 11 (63.6%)** | ❌ **NO** — `S39` fires 0 times in 5,376 decision firings |
| CHOICE — an actor took the other option | 2 of 11 | ✅ yes, but the budget never binds (§8.1) |
| STATE — a stored quantity or type differed | 2 of 11 | ✅ yes — 8–29 distinct world futures |

**64% of the corpus's own counterfactual branches are unreachable**, and two of the seven name
subsystems that already exist: *"Player LOSES the bilateral personal combat"* is `personal_combat`,
which `combat_seam` really does call (§2) and which no verb routes to; *"Crown runs
counter-intelligence (Intel vs Ob 2) and SUCCEEDS"* is an investigation contest — **`HANDOFF_NEXT`
row 2b, the discovery model prescribed and not built (§10)**.

⚠ **The classification is a judgement and is printed per row with its evidence** so a reader can
disagree on any one of the eleven.

## 11 · Were the v2 systems marked for import actually imported? (ARM 6)

`HANDOFF_NEXT.md` §2 — which calls itself ***"this is the real backlog"*** — prescribes five
root-cause fixes. Checked against `verb_table.yaml`:

| row | prescribed | state |
|---|---|---|
| **2a** | a generic `release` verb — *without it a person cannot resign an office, a direct `T-m` violation* | **ABSENT** |
| **2b** | **`the six investigation acts` split into six rows with writes; #359's discovery model — a contest of capability against secrecy, EMITTING A DEGREE** | **NOT SPLIT** — one row, `writes: []`, no `contests:`, grade `assumption` |
| **2c** | `determine` graded, `judging_set` as a Query | present, grade **`absent`** |
| **2d** | a founding verb writing `Rung.exists`/`Site.exists` — *`F.20`: the world only decays* | **ABSENT — zero producers** |
| **2e** | ⚠ **NOT a `bargain` verb** — the handoff says *"test composability FIRST … adding a verb is the LAST resort, not the first"*. The deliverable is the composability test | **NOT TESTED** — no test of `utter`+`commit` anywhere in the chain, this sweep included |

**4 of 4 scorable rows unmet; the fifth was never tested.**

⚠ **An earlier draft said "0 of 5" and that scored 2e against the option the handoff explicitly
deprecates.** Counting the absence of a `bargain` verb as an unmet deliverable inverts the
prescription. Corrected. Two further probe weaknesses, disclosed: 2a is a substring match on a verb
name (the *concept* was checked by hand — `repudiate` closes only a `commit`, `revoke` needs a
remit, so no self-resignation path exists), and 2c originally checked only `determine`'s grade when
the prescription is `judging_set` as a Query in `shape.py`; both are now probed.

PRs #358, #361 and #362 all edited the meta-architecture **prose**; none touched
`verb_table.yaml` — `git diff 2c0ea60..1e163ee -- .../verb_table.yaml` is empty. #362 landed
thirteen edits to a document. The five mechanisms the same handoff calls the real backlog did not
land.

**2b is the one that answers Jordan's question directly.** The prescription was a discovery
*contest emitting a Degree*. Without it, investigating and accusing cannot carry a degree of
success no matter how well the ladder behaves.

---

## What this sweep does NOT claim

- **It mints no degree.** Every band reported is one the sweep *supplied*; `degree_from_net` and
  `_advance` are untouched. `H-98` is not closed and this does not close it.
- **It fixes nothing.** No file under test is edited. Every finding is a measurement with a
  reproduction command.
- **Arm 5's numbers cover the Persuasion Track only** — one of four games, on an engine Jordan
  states is unfinished.
- **Arm 8's classification of the eleven v30 branches is a judgement**, printed per row with the
  verbatim line it rests on so a reader can disagree on any of them.
- **This document was attacked by a structurally independent read-only critic** (`Read, Grep,
  Glob`, no write tools) that never saw the producer's reasoning. It returned 13 findings: **6
  overturns and 7 narrowings**, every one of which is applied above with its retraction left
  visible. It also listed the claims that **survived** — `emits_at` having zero callers, the
  `SystemExit` 14/4 split, `content_hash` reading the log only, the fold emitting the union, the
  stale "four branches", and that the sweep mints no degree. Those are the bankable ones.
- **Six confounds were found in this sweep's own setup and are recorded, not smoothed.** Each
  produced a wrong answer first:
  1. the unset `RESOLVE` step — reported a design refusal that was the harness's;
  2. `body_delta` indexing a deleted person — reported a `KeyError` as a design refusal;
  3. `runnable()` skipping `apply_rescale` — measured 86 cases where the instrument runs 89;
  4. the contest-length confound — reported the four-band ladder **NON-MONOTONE**;
  5. the rotation branch in arm 7 — reported flexibility **0.0156** where the working
     counterfactual reports **0.3093**;
  6. arm 9's first diagnosis — blamed "the acts do not move the world" when the world demonstrably
     moves; the true cause is that the deliberation never reads it.
  Five of the six were wrong in the direction that flattered the sweep's thesis. Numbers 4, 5 and 6
  would each have been the headline.

## Where these findings were digested (2026-09-04)

Per Jordan's direction — *"We have to digest all of these findings/takeaways too in both
meta-architecture and code design itself"* — the results are folded into the two surfaces that own
them, not left in this directory:

| surface | what landed |
|---|---|
| **code design** — `engine/season/hole_register.yaml` | **eight new rows, all grade `measured`**: `H-113` `emits_at` has zero callers · `H-114` `_eff_kill` is degree-blind · `H-115` the degree branches raise `SystemExit` · **`H-116` the severed belief→decision edge** · `H-117` the act budget never binds · `H-118` `content_hash` reads the log, not the world · `H-119` the seam's two degree surfaces contradict · `H-120` 3 of 4 prizes claimed by no verb. Register clean: `R0/R1/R3/G8/G12/G13` ok, transcription clean, citations all resolve, and `R2`/`G6`'s pre-existing violation counts (6 and 15) are **unchanged** — verified by stashing. |
| **meta-architecture** — `architecture/meta/HANDOFF_NEXT.md` | new **§2A, "THE BACKLOG, MEASURED"**. §2's five root causes were argued from reading; they are now executed against all 143 cases. The rows survive and **the ordering changes**: `H-72`/`F.24`/`H-94` moves ahead of all five, because a discovery model or a degree ladder that cannot reach a later decision is a better-labelled log line. |

⚠ **One finding indicts a habit rather than a row, and it is recorded in both places.** #362 applied
`ID-13` — *a declared field reaching no reader is one that does not exist* — to delete
`Tenure.conferrer`, and did not apply it to `emits_by_degree`, which the same revision added.
**Apply `ID-13` to what a revision ADDS, not only to what it inherits.**

## Reproduce

```bash
cd proposals/2026-09-04-degree-sweep
python sweep.py            # all nine arms; writes runs/SWEEP_LOG.txt + runs/results.json
```

Arm 8 reads the v30 snapshot through `git show` and needs the tag present:

```bash
git fetch --depth=1 origin refs/tags/v30-snapshot-2026-06-28:refs/tags/v30-snapshot-2026-06-28
```

| arm | question |
|---|---|
| **0** | which decision sites do the 143 cases reach? |
| **1** | does the only degree-keyed verb admit the canonical four bands? |
| **2** | can a season loop reach a degree at all; what does the guard cost? |
| **3** | the depth-3 degree tree over the corpus, both ladders |
| **4** | what does `content_hash` observe; what shape of result must be accepted? |
| **5** | person-to-person degrees — the live ladder, the chain's verbs, the depth-3 four-band tree |
| **6** | were the v2 systems marked for import actually imported? |
| **7** | **flexibility — alternative outcomes within each season, depth 3** |
| **8** | how much of the v30 corpus's own counterfactual axis is reachable? |
