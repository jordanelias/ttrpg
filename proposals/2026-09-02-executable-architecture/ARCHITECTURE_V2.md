# THE SEASON LOOP — AN **EXECUTABLE** HOLONIC ARCHITECTURE

## Status: **PROPOSED (2026-09-02). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** Under §0.2 **nothing in
## it runs.** Part X says what would make each claim done and which steps cannot be satisfied by writing.

> ## THE ONE-SENTENCE DIFFERENCE FROM ITS PREDECESSOR
> **#353 specified a season loop that cannot be executed without inventing, and this document
> closes every place where that was true — not by deciding what #353 deliberately left open, but by
> making each opening a ROW WITH AN OWNER, A GRADE AND, WHERE THE SHAPE IS RULED AND ONLY THE VALUE
> IS OPEN, A DEFAULT AN INSTRUMENT MAY INJECT WITHOUT INVENTING IT.**

---

# PART 0 · HOW TO READ THIS, AND WHAT IT INHERITS

## §0.1 · Scope — unchanged, and it still decides what counts as evidence

**The only admissible sources are the design chain PR #337 → now**, head = `ARCHITECTURE.md` (#353)
plus the executed session at `proposals/2026-09-01-season-loop-tests/`. No file under `engine/`, no
subsystem `sim/`, and **no decision ratified before #337** is authority.

**The three qualifications of #353 §0.1 carry unchanged** and are not restated. One is worth naming
because this document relies on it more heavily than its predecessor did: *a pre-#337 document may
be the **SUBJECT** of an in-chain claim, never the **REASON** one is correct.* The 46-NPC roster and
the 97-arc corpus are subjects in exactly that sense.

## §0.2 · What this document INHERITS UNCHANGED, and why that matters

> **Parts I–VI of #353 are RIGHT and are inherited whole.** This is not deference. It is the
> session's measured result: 121 probe executions produced **63 PASSes**, of which **43 were raised
> by a gate, a type or a law in the shape itself**, and an independent citation audit at ~40 sites
> across two adversaries found **every quotation verbatim and every section saying what was claimed**,
> with one wrong section number between them.

Specifically inherited, and **not** re-argued here:

| inherited | where it lives in #353 | confirmed by |
|---|---|---|
| **The one sentence**, the nine throughlines, the five laws | §1–§3 | the whole probe ledger |
| **L1** — the person is the only actor; obstruction falls out with no verb | §3, §11.1 | `P8` executed it: a stranger took the seat, no `obstruct` verb, no branch in the resolver |
| **L2** — `choose` sees no World, enforced by the parameter list | §3 | `P3` |
| **L3** — every aggregate is a function, **and its clause 1 permits a per-`(Person, axis)` counter** | §3, §22.4 | ⚠ this document's **D6**; the session refused clause 1 for four revisions |
| **L4** — the Partition, asymmetric by subject | §3 | ⚠ extended by **D1**; the column was unusable as stated |
| **L5** — the Edge Law: a crossing may change what may be chosen, never produce an outcome | §3 | `P18` executed both halves once **D22** landed |
| **The two module rules R-1/R-2 and the barrier-cache concession** | §4 | `A10`, `A13` |
| **The two topologies** — containment tree vs lateral graph, kept apart | §6, §38 | `A25` |
| **The six steps, four barriers, per-owner partition** | §23, §31 | `A22` |
| **`Event` carrying no actor and no target** | §19.3 | `P5`, `A20` |
| **`causes[]` required and non-empty, `[ROOT]` for antecedent-free** | §19.4 | `A1`, `A2`, `A28` |
| **One log, not two** | §19.5 | `A29` |
| **The seam: one resolver, one degree ladder, demote-only veto, caller-supplied `max_depth`** | §39 | `A8` |
| **No per-container clock** | §40.3 | `A16` |
| **Fixed point, determinism, the content hash** | §32, §33, §48 | `A4`, `A5` — with a control that fires |
| **The whole of Part VIII's refusals** | Part VIII | see §0.4 |
| **The Godot port, the autoload rule, the version floor ≥ 4.4** | Part VI | `A35` |

**A successor that rewrites Parts I–VI is a worse document.** The failures this one fixes are not in
the architecture; they are in what the architecture declines to say.

## §0.3 · What this document RETRACTS or AMENDS in #353

Fourteen changes. Each is a place where #353, read strictly, **cannot be executed** — established by
running it, not by reading it.

| # | #353 says | verdict | where |
|---|---|---|---|
| **1** | L4's `social:` is *"a static schema column"*, and the document states **two** rows | ⛔ **INSUFFICIENT.** Two rows and two declared-missing cannot type ~30 fields. The matrix names **things**, not fields, so `(Person, convictions)` rides on `stance`'s row | **D1** |
| **2** | §61: `q` has no producer | ⚠ **SHARPENED.** Not execution-defeating — a literal runs — but **NPC-loop-defeating**: every option set is authored, which is the property `Candidate[]` was chosen to protect | **D2** |
| **3** | §18.2: `Sensation` is *exactly two scalars*; `standing` is the gap between what everyone reads off you and what you hold | ⚠ **AMENDED, AND THE LAW WAS WRONG.** The bar is **§20** (*"Nobody else may read or write it"*), not §22.4 clause 2 — `sense()` is not a resolver-side Query | **D3** |
| **4** | §26: `budget : (Person, View) -> int`, no World; §26.3: it varies by office, condition, distance | ⛔ **COLLISION, answerable by precedent.** All three inputs are resolver-side; travel legs have no owner | **D4** |
| **5** | §26.3 *"the list is ORDERED"* vs §32 *"canonicalized… never by completion order"* | ⛔ **TWO ORDERS FOR ONE ARRAY** | **D5** |
| **6** | L3 clause 1: a counter per `(Person, axis)` on a closed registry | ⚠ **THE REGISTRY DOES NOT EXIST**, no matrix row admits the increment, and `exposure` collides with the need scalar | **D6** |
| **7** | §13: `Record` is a live carrier; §30.1: it has no Partition row | ⛔ **EVERY RECORD WRITE IS AN UNMARKED CELL** | **D7** |
| **8** | §30.1: `(Person, exists)` has no row | ⛔ **DEATH RAISES UNDER THE MATRIX'S OWN RULE** | **D8** |
| **9** | §27: `resolve : (Act[], World) -> Event[]` | ⛔ **THE RESOLVER HAS NO BODY.** What each verb *does* is prose scattered across §11, §36, §37, §54 | **D20** |
| **10** | §26: `choose` is the person's function | ⛔ **NO DECISION POLICY EXISTS.** `convictions`, `beliefs` and `stance` are consumed by nothing | **D21** |
| **11** | §12.1: a band crossing *"is an EMISSION"*; §19.4: `causes[]` non-empty | ⛔ **MATTER'S WRITES EMIT NOTHING**, so every crossing is a causal orphan | **D22** |
| **12** | §10 gives every Rung `matter.stores`; L3 refuses stored aggregates | ⚠ **AMBIGUOUS, AND IT COST TEN ARCS.** A treasury is **matter**; what L3 refuses is a pooled **social** quantity | **D26** |
| **13** | §42.2.1: *"the honest behaviour is to REFUSE, not to pick a plausible number"* | ⚠ **NARROWED TO ITS HONEST DOMAIN.** Kept for `absent`; replaced by inject-declare-sweep for `assumption`. **§G is the whole argument** | **§G** |
| **14** | §61–§62: two prose tables of open questions | ⛔ **REPLACED BY THE HOLE REGISTER.** #353 §63.2 makes this argument itself: *"prose registers are re-typed; rows are inherited"* | **Part VII** |

## §0.4 · What the session did **not** overturn, stated because a reader will assume otherwise

**Five refusals held under 143 cases and are not weakened here**, together with the honest count of
what they cost:

| refusal | § | cases that wanted it |
|---|---|---|
| a Rung storing a **social** aggregate | §10.1, L3 | ~8 |
| a threshold **producing an outcome** | L5 | ~4 |
| a **fourth clock** — a quantity advancing with no author | §25.1, L5 | ~4 |
| a **faction acting** as an actor | L1 | 3 |
| a **GM / referee** adjudicating | §1 | 3 |

**~22 core blocks, and the specification does not bend.** Those cases were authored against a
stat-track model the design replaced on purpose. §36.3 and §37 already give the *"a counter compels
a named person"* shape that the in-chain survey found **19 of 50 arcs** actually asking for.

> **A successor that runs more arcs by bending L1, L3 or L5 is worse than #353.** The increase this
> document claims comes entirely from closing holes, never from relaxing refusals.

## §0.5 · Vocabulary — additions only

#353 §0.4's table carries unchanged. Four terms are added, and each is an ordinary word.

| term | definition |
|---|---|
| **hole** | a place the specification does not say enough for an implementation to proceed. Part VII is the register of them. Not a coinage — the ordinary word, used because *gap*, *debt* and *open item* are all in use in the chain for other things |
| **default** | the value or rule an instrument may inject for a hole **whose shape is ruled and whose value alone is open**. It lives in the register, never in a body. §G |
| **fill** | an instrument supplying what the design withholds. A fill **on** the register is lawful and declared; a fill **off** it is an invention and is a defect |
| **verb row** | one line of §E's table: a verb, what it may write, what it requires, what it emits. The resolver's body |

---

# PART A · THE DIAGNOSIS THIS DOCUMENT IS BUILT ON

**Read this before Part D, or the tables will look like bureaucracy.** They are the answer to a
measured failure, and the failure is not the one it appears to be.

## §A1 · What was run

An instrument implementing #353 was built, attacked by three structurally-independent read-only
critics and one anti-fabrication auditor, and corrected four times.

| | |
|---|---|
| cases | **46 NPCs** (the registry, exactly) · **97 arcs** (the corpus; the in-chain run covered 51) |
| rows | **972** `season_requires` rows, written by lanes **blind to the shape** |
| probes | **120 executions**, each naming the section it exercises |
| adversarial findings | **56**, across four passes: 10 · 16 · 16 · 14 |
| **cases that ran end to end** | **ZERO** |

## §A2 · The loop the session was caught in, and its true extent

The repository owner diagnosed it mid-session:

> *"The agents are continually inventing work that is forbidden, because it is trying to resolve
> errors that prevent scripts — designed to adjudicate the project state — from executing.
> Consequently it is in a holding pattern: it fixes errors with scripts to make them run, followed
> by antagonists identifying that the scripts no longer possess fidelity to the ideal code shape."*

**The mechanism is real. Its extent was one hole, not fifty-four.** Adjudicated by tracing each
finding to whether removing the invention actually stopped execution:

| class | count | indicts |
|---|---|---|
| **FORCED** — the spec withholds something no season can run without | **16** | **THE SPECIFICATION.** This document. |
| **AVOIDABLE** — the instrument could have refused, reported and continued | **24** | the method. Not this document's to fix, and named in §A4 so it is not repeated |
| **NOT INVENTIONS** — refusals, correctly made | **29** | nothing |

**Only the Partition (§D1) forced the loop the owner described**, and it forced it twice — once in
revision 1, once in revision 2. Every other correction left the loop running.

> **THE PRODUCTIVE READING, AND IT IS WHY THIS DOCUMENT EXISTS:**
> **The set of things an instrument is FORCED to invent is the specification's execution gap,
> located precisely.** It cannot be found by reading. It was found by trying to run.

## §A2b · The two pathways are not one question — `01_NPC_VS_ARC.md`

**Measured, and it decides how this document's own claims should be read:**

> **0% of the NPC set's core blocks are design refusals. 33% of the arc set's are.**

The NPC pathway is blocked **entirely by holes** — all 25 core blocks are things this document now
carries a row for. The arc pathway is **a third refusals**: 22 core blocks are things the
specification declines on purpose, from arcs authored against a stat-track model with faction
meters, world tracks and a GM.

**The scale mix is the cause.** NPC cases are person-scale (21) and faction-scale (18); arc cases are
**realm-scale (43)**, and every refusal the design makes bites at aggregate scale.

> **CONSEQUENCE FOR THIS DOCUMENT: Parts D–G and the register are aimed at the NPC pathway and
> should largely clear it. THE ARC PATHWAY NEEDS A SECOND, DIFFERENT PIECE OF WORK THAT NO
> SPECIFICATION CHANGE DELIVERS** — an authoring pass re-expressing ~22 arcs against §36.3's
> petition chain and §37's dispensation-as-`tell`, where the *"a counter compels a named person"*
> shape already lives. **The two must not be averaged again**: a single headline over 143 cases
> hides that one set is blocked by SILENCE and the other by PRINCIPLE.

## §A2c · Two defects in the evidence base itself, which any re-run will hit

**Recorded because they are not this document's to fix and a second instrument will meet them:**

1. **Six of the seven in-chain case files are committed inside a markdown fence** with an
   agent-transcript preamble, and do not load with `yaml.safe_load`.
2. **`ARC3.yaml` is truncated at its head** — its first record's `- id:` was lost, orphaning a third
   emergent case. Recovery is partial and reports how many lines are unrecoverable.

**The committed corpus is the chain's evidence and an instrument must not edit evidence.** Strip at
load time, and say so in the output.

## §A3 · The three terms the diagnosis missed

**Term 1 — THE SIGN RUNS BOTH WAYS, and this was the costliest single error of the session.**
Seven findings were the instrument **refusing what the design permits** and charging the refusal to
the design. The largest ran for four revisions: L3 clause 2 raised on needs that never cross a
holder, when clause 1 calls such a counter *"legal, since every increment is in the holder's own
ledger"*. The last one **survived all four adversarial passes**: a pooled faction-wide *resource*
refused wholesale, when §10 gives every Rung `matter.stores` and §11 gives an office a stake — **a
treasury is matter**. Correcting it unblocked **ten arcs**. `CLAUDE.md` §0.1 point 4 governs:
*asymmetric skepticism is a bias, not a defence.*

**Term 2 — A REGEX ROUTER CANNOT CONVERGE, WHATEVER THE SPECIFICATION SAYS.** Five recurrences of
one class: `ambient` (8 arcs → 3) · `counter` inside *"counter-productive"* (10 → 8) · adjectival
`standing` (18 core rows) · `standing condition` escaping the whitelist built for the third ·
`age\w*` matching **agent/agency/agenda**, which produced the arc corpus's only PLAYABLE verdict.
**#353 §44.4's own ruling applies to the instrument: *don't route — declare.*** §H acts on it.

**Term 3 — THE FINDING-GENERATOR.** ~20 of the 56 were label, count and docstring hygiene; the
substantive per-round count **fell**. A claim of *"zero convergence"* over that series has no
control. This is `CLAUDE.md` §0.3's **T3** term, and the session's own 224-line findings ledger is a
fifth instance of it — a document produced by the adversarial pass, which §0's 2026-08-19 amendment
says the pass may not create. **This document is the last one; Part VII is rows, not prose.**

## §A4 · The method rules that follow, binding on any instrument built from this document

Stated here rather than left implicit, because 24 of the 56 findings were method, not design.

1. **A fill off the register is a defect.** An instrument may inject exactly what Part VII declares
   and nothing else. This makes the antagonist's question a grep rather than a judgement.
2. **A route may not be decisive on a single common word.** Forbid the shape, do not enumerate the
   words: a whitelist is what failed at recurrence four, and recurrence five was not on it.
3. **Prefer declaration to inference.** A case row carries the verb or contract it exercises;
   nothing reconstructs from prose what the author knew when writing it.
4. **A probe must declare how its verdict was reached** — the shape raised it, nothing was callable,
   only a reader stops it, or the probe supplied the model. §34's enforcement column, applied to the
   measuring device.
5. **A refusal is not an invention** and is not counted as one.
6. **An error against the design is as serious as one for it**, and is harder to see, because it
   looks like rigour.

---

# PART B · THE FOURTEEN DESIGN DEFECTS, AND WHAT EACH COSTS

**Twenty-six design defects were consolidated from the 56 findings; thirty findings were dropped as
instrument-only.** Sixteen of the twenty-six are already named in #353's own Part IX — the session
**confirmed them by execution**, which is worth having and is not new. **Ten are new**, and they are
the ones below marked ⊕. The rest are discharged in Parts D–G and Part VII.

| id | defect | new? | cases |
|---|---|---|---|
| **D1** | The `social:` column cannot be applied — two rows for ~30 fields, and the matrix names things, not fields | ⊕ | **all** |
| **D2** | `q` has no producer, so every option set is authored | | all NPC |
| **D3** | `standing` has no formula and the obvious one is barred by §20 | | 2 |
| **D4** | `budget`'s signature and its stated variation cannot both hold | | all |
| **D5** | Two orders specified for one act array | ⊕ | 2 |
| **D6** | L3 clause 1's registry does not exist and no row admits the increment | ⊕ | **~28** |
| **D7** | `Record` has no Partition rows | | ~13 |
| **D8** | `(Person, exists)` has no row | | every death |
| **D9** | `season_factor` unowned — blocks `yield` | | 1 |
| **D10** | Travel legs unowned | | 1 |
| **D11** | `judging_set_rule` unspecified — nothing is decided at a sitting | | 2 |
| **D12** | Establishment size unspecified — an office has no pool source | | 1 |
| **D13** | The degree ladder's margin model is absent | | every contest |
| **D14** | Five witness channels, no predicates — nothing is private | | 1 |
| **D15** | No termination argument per spiral | | ~4 |
| **D16** | *"No reaction inside a season"* vs the seam | | 1 |
| **D17** | Scene = act? Every count verdict flips with it | | 1 |
| **D18** | Refraction side and distortion magnitude | | 2 |
| **D19** | The budget is the whole of the pricing — a cheap act and a ruinous one cost the same | ⊕ | ~7 |
| **D20** | **The resolver has no body** — verb semantics are prose | ⊕ | **all** |
| **D21** | **No NPC decision policy** — `convictions`/`beliefs`/`stance` are consumed by nothing | ⊕ | **all NPC** |
| **D22** | MATTER emits nothing, so every band crossing is a causal orphan | ⊕ | every crossing |
| **D23** | No world-generation roster | | any run |
| **D24** | The argument layer's fault roster is absent | | 2 |
| **D25** | A person has no banded scalar; the verb gate's carrier is a Site | ⊕ | 2 |
| **D26** | **Material vs social pooling is ambiguous** — read as refusing a treasury | ⊕ | **~19** |

> **D1, D20 and D21 are the three that make the difference between a specification that grades cases
> and one that RUNS them.** Everything else is a row.

---

# PART D · THE WRITE MATRIX, KEYED ON `(kind, field)` — **D1**

## §D1 · Why #353's matrix cannot be applied

#353 §30 gives a matrix over **things** — `Date`, `stores`, `condition`, `Tenure`, `stance` — and
§0.4 defines the Partition as *"the `social: bool` column on **`(record-kind, field)`**"*. **Those
are different keys**, and the mismatch is not cosmetic:

- A gate looking up `(Person, convictions)` finds no row, falls back to the *thing* `stance`, and
  **admits a write the design never authorised**. The session did exactly this and turned a real gap
  into a PASS.
- §30.1 declares two rows MISSING and §63.1 says *"rule the row before adding it"* — correct, and it
  leaves **~28 fields** with no rule at all, of which the loop touches at least twelve every season.

## §D2 · The derivation rule — stated so no row needs guessing

**Two clauses, and they are read off §30's own step columns. Nothing here is a new decision.**

> **DR-1.** A field whose thing is admitted at a step **the world writes** (MATTER, or CENSUS's
> reconciliation) is `social: false` — **the world may write it, so an act is not required.**
>
> **DR-2.** A field whose thing is admitted **only at RESOLVE**, whose write class is ACTS, is
> `social: true` — **only an act may write it.**
>
> **DR-3.** Where neither applies — a thing admitted at CALENDAR and RESOLVE, or at WITNESS alone —
> **the derivation is silent and the row must be stated.** Part VII carries it with a grade.

**DR-3 is the clause that makes this honest.** #353's silence was not laziness; those cells
genuinely are not determined by the step columns. The answer is to state them, not to infer them.

## §D3 · The matrix

**`emits:` is new (D22): a write that emits names the Event kind it produces**, so a downstream
Event has an antecedent to cite and `causes[]` stops being `[ROOT]` for everything MATTER touches.

| `(kind, field)` | CAL | MAT | DEL | RES | WIT | CEN | class | `social:` | by | `emits:` |
|---|---|---|---|---|---|---|---|---|---|---|
| `(Date, fired)` | **y** | · | · | **y** | · | · | CALENDAR/ACTS | **false** | DR-3 · §24 has no actor | `date.fired` |
| `(Date, due_at)` | **y** | · | · | **y** | · | · | CALENDAR/ACTS | **true** at RES | DR-3 · `convene` is an act | `date.scheduled` |
| `(DocketItem, matter)` | **y** | · | · | **y** | · | · | CALENDAR/ACTS | **false** | DR-3 · §24 *"dockets form"*, no actor | `docket.formed` |
| `(ConveningCondition, attached)` | **y** | · | · | **y** | · | · | CALENDAR/ACTS | **false** | DR-3 | `condition.attached` |
| `(Rung, stores)` | · | **y** | · | **y** | · | · | MATTER/ACTS | **false** | DR-1 | `stores.changed` |
| `(Rung, envelope)` | · | **y** | · | · | · | **y** | MATTER | **false** | DR-1 | `envelope.changed` |
| `(Rung, yield)` | · | **y** | · | · | · | · | MATTER | **false** | DR-1 | `yield.taken` |
| `(Rung, dates)` | **y** | · | · | **y** | · | · | CALENDAR/ACTS | **false** | DR-3 | `date.scheduled` |
| `(Rung, stake)` | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `stake.changed` |
| `(Site, condition)` | · | **y** | · | **y** | · | · | MATTER/ACTS | **false** | DR-1 | `condition.worn` · `condition.band_crossed` |
| `(Site, drawers)` | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `drawers.changed` |
| `(Person, body)` | · | **y** | · | **y** | · | · | MATTER/ACTS | **false** | DR-1 | `body.changed` · `person.died` |
| `(Person, exists)` ⊕ | · | **y** | · | **y** | · | **y** | MATTER/ACTS | **false** | DR-1, **D8**; bounded by §15.3's causation rule | `person.died` · `person.individuated` |
| `(Person, stance)` | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `stance.moved` |
| `(Person, convictions)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2; §9.3 — moved by **argument and consequence**, never by evidence | `conviction.moved` |
| `(Person, beliefs)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2; §9.3 | `belief.revised` |
| `(Person, scar[axis])` | · | · | · | **y** | · | · | ACTS | **true** | **stated in chain** — §54 item 21 | `scar.taken` |
| `(Person, axis_count[axis])` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | **D6**. L3 clause 1's counter. `axis` on D6's registry | `axis.incremented` |
| `(Person, claim_ledger)` | · | · | · | · | **y** | · | INTERIOR | **false** | DR-3 · §20 makes `witness` the only minter, and it is not an act | `claim.deposited` |
| `(Person, capability)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `capability.advanced` |
| `(Person, marks)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `mark.changed` |
| `(Person, travel_leg)` ⊕ | · | **y** | · | **y** | · | · | MATTER/ACTS | **false** | DR-1, **D10** — see §D4 | `travel.moved` |
| `(Tenure, since)` | · | · | · | **y** | · | · | ACTS | **true** | DR-2 — `confer`, `commit`, `oblige`, `tie` | `tenure.opened` |
| `(Tenure, until)` | · | **y** | · | **y** | · | · | MATTER/ACTS | **false** | **stated in chain** — §15.3, the one declared seam, bounded by causation | `tenure.closed` |
| `(Tenure, degree)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `tenure.graded` |
| `(Record, exists)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | **D7** — `create` by an act (§13) | `record.created` · `record.destroyed` |
| `(Record, ttl)` ⊕ | · | **y** | · | · | · | · | MATTER | **false** | **D7** — §13's licensed clock | `record.expired` |
| `(Record, stages)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | **D7** — §13.1: terms are **act-declared**, never MATTER-advanced | `record.staged` |
| `(Record, matured)` ⊕ | · | **y** | · | · | · | · | MATTER | **false** | **D7** — MATTER **matures** a term the act declared; `causes[]` names that act | `term.matured` |
| `(Record, forgery_quality)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `record.forged` |
| `(Office, establishment)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 | `establishment.changed` |
| `(Office, remit)` ⊕ | · | · | · | **y** | · | · | ACTS | **true** | DR-2 — `establish` is an act | `remit.changed` |
| `(Proposition, *)` | · | · | · | · | · | · | — | **n/a** | §14 — **IMMUTABLE**. There is no write | — |
| `(Act[], returned)` | · | · | **y** | · | · | · | ACTS | **n/a** | DELIBERATE writes nothing else | — |

**ANY `(kind, field)` NOT ON THIS TABLE IS AN UNMARKED CELL AND THE WRITE RAISES.** That is #353
§30's rule, now applicable because the table is keyed the way the rule is stated.

## §D4 · Travel is a Tenure alter — **D10, answered by precedent, not by ruling**

§22.3 lists travel legs as unowned and §31.1 calls them a fourth cross-owner operation. **No new
owner is needed.** A person's location **is** their `contain` Tenure (§6.1), every Tenure is **owned
by its subject** (§15.1), so a leg is an `alter` on that edge, owned by the traveller.

The `(Person, travel_leg)` row above is the *movement in progress*; arrival closes the old `contain`
and opens a new one, both in the ACTS class at RESOLVE, stratum 0 (movement). **This is #353's own
§15.1 applied, and it removes an ownership hole without adding a carrier.**

## §D5 · What this costs

The matrix grows from 13 rows to 33 — **the single largest edit in this document, and the one that
makes `write()` stop needing an instrument to guess.** Nine rows are stated in chain or derived by
DR-1/DR-2 with no judgement; **thirteen are DR-3 rows** and each carries its reason in the `by`
column above. Every one is re-derivable by a reader from §30's step columns and §24/§20's text.

---

# PART E · THE VERB TABLE — THE RESOLVER'S BODY — **D20**

## §E1 · The defect this closes, and why it is the largest of the three

#353 gives `resolve : (Act[], World) -> Event[]` and **never says what any verb does.** The verbs
are named across §11 (`issue`, `determine`, `confer`, `revoke`, `dispatch`, `convene`), §36
(`carry`), §37 (`tell`, `comply`, `evade`, `defy`, `refract`), §13 (`open_case`), §54 (`transfer`),
§2 (six investigation acts) — as **prose, in nine sections, with no declared writes.**

**The consequence is exact and it is why zero cases ran end to end.** An instrument cannot resolve;
it can only be handed an `effect` callback per probe. So every case was *graded by routing* rather
than *run*, and "does this NPC's season execute" was never actually asked.

> **§42's descent, applied to acts.** #353 already rules that a module declares what it consumes,
> emits and owns. **A verb is the same object at a smaller scale**, and the table below is that
> declaration. It invents no verb: every row is a verb #353 already names.

## §E2 · The row shape

```yaml
verb: <name>
stratum:     0 movement | 1 binding_decision | 2 contested_physical | 3 uncontested_material | 4 social
eligibility: own | remit:<act> | hold:<object> | presence:<rung>   # NEVER capability (§9.2)
requires:    [<precondition>, ...]        # checked in the fold; failure emits, never raises
writes:      [(kind, field), ...]         # MUST be rows of Part D; anything else is unmarked
contests:    <prize> | none               # if set, routes to the seam at RESOLVE (§39)
emits:       [<family.type>, ...]         # on success
emits_on_refusal: [<family.type>, ...]    # THE SCARCITY CHANNEL (§27.1)
grade:       ruled | measured | assumption | absent
```

**`emits_on_refusal` is load-bearing and is new.** §27.1's whole scarcity argument — *"the second
claimant on an emptied granary gets a DIFFERENT Event"* — only works if a failed precondition
**emits**. A verb that raises produces no Event, no witness, and no arc.

## §E3 · The table

| verb | str | eligibility | requires | writes | emits | on refusal | grade |
|---|---|---|---|---|---|---|---|
| `move` | 0 | own | a `contain` path exists | `(Person, travel_leg)`, `(Tenure, until)`, `(Tenure, since)` | `travel.moved` | `travel.blocked` | assumption |
| `convene` | 1 | `remit:convene` | the venue's `container` resolves, or is NONE (§6.2) | `(Date, due_at)`, `(ConveningCondition, attached)` | `date.scheduled` | `convene.refused` | ruled §11 |
| `confer` | 1 | `remit:confer` + the office's `conferral` basis | **1-per-object**: no live `hold` on the object, **or** the holder-Proposition has zero live `commit` (§54 it. 20) | `(Tenure, until)`, `(Tenure, since)` | `tenure.opened`, `tenure.closed` | `confer.refused` | ruled §11 |
| `revoke` | 1 | `remit:revoke` + the office's `revocation` basis | a live `hold` exists | `(Tenure, until)` | `tenure.closed` | `revoke.refused` | ruled §11 |
| `dispatch` | 1 | `remit:dispatch` | the named person exists | — *(§11.1: it names a person; **their own `choose` decides**)* | `order.given` | `dispatch.refused` | ruled §11.1 |
| `issue` | 1 | `remit:issue` | `scope` enumerates **executors**, not places (§37.1) | — *(a Dispensation is not a state write — §37.3)* | `dispensation.issued` | `issue.refused` | ruled §37 |
| `determine` | 1 | `remit:determine` | a fired Date with a DocketItem; **`judging_set` — D11, `absent`** | `(Tenure, degree)` | `matter.determined` | `determine.refused` | **absent** |
| `carry` | 4 | own | a Petition exists; **costs budget like any act** | `(DocketItem, matter)` | `petition.carried` | `carry.refused` | ruled §36.1 |
| `petition` | 4 | own | — **no dedup, no cap, no per-venue limit** (§26.3) | — *(a Petition is created, not written)* | `petition.filed` | — | ruled §26.3 |
| `tell` | 4 | own | the teller holds a claim on the subject | — *(deposits at WITNESS, not here)* | `news.told` | — | ruled §37.1 |
| `transfer` | 3 | own \| `hold:<store>` | **`stores(hearth(giver), kind) >= amount`** (§54 it. 7) | `(Rung, stores)` ×2 | `transfer.made` | **`transfer.refused`** — §27.1's scarcity | ruled §54 |
| `levy` | 3 | `remit:issue` + `presence` | `stores(...) >= amount` | `(Rung, stores)` | `levy.taken` | `levy.refused` | assumption |
| `work` | 3 | own \| `presence:<site>` | `condition >= floor(verb)` (§12.1) | `(Site, condition)` | `site.worked` | `work.unavailable` | ruled §12.1 |
| `restore` | 3 | own \| `presence:<site>` | `Δ = +(1 − condition) × f(degree) × share` (§54 it. 7's mirror) | `(Site, condition)` | `site.restored` | `restore.refused` | ruled §54 |
| `create_record` | 3 | own | — | `(Record, exists)`, `(Record, stages)` | `record.created` | — | **D7** |
| `open_case` | 4 | `remit:determine` | **the act DECLARES the stages and their terms** (§13.1) | `(Record, exists)`, `(Record, stages)` | `case.opened` | `case.refused` | ruled §13.1 |
| `forge` | 3 | own | — | `(Record, exists)`, `(Record, forgery_quality)` | `record.created` | — | assumption |
| `destroy_record` | 3 | `hold:<record>` \| `presence` | — | `(Record, exists)` | `record.destroyed` | `destroy.refused` | **D7** |
| `commit` | 4 | own | the Proposition exists (immutable, §14) | `(Tenure, since)` | `commitment.made` | — | ruled §14.2 |
| `repudiate` | 4 | own | a live `commit` exists | `(Tenure, until)` | `commitment.ended` | — | ruled §14.2 |
| `oblige` | 4 | own | — | `(Tenure, since)` | `duty.taken` | — | ruled §15 |
| `tie` / `knot` | 4 | own | **stored once, on the lower id** (§15.1) | `(Tenure, since)` | `bond.formed` | — | ruled §15.1 |
| `comply` | 4 | own | a claim of the dispensation's terms is in the actor's **own** ledger | per the term's own row | `compliance.given` | — | ruled §37 |
| `evade` / `defy` | 4 | own | as `comply` | per the term's own row | `compliance.withheld` | — | ruled §37 |
| `refract` | 4 | own | as `comply` — ⚠ **emitter- or receiver-side is `absent`, D18** | — | `terms.distorted` | — | **absent** |
| **the six investigation acts** | 2 | own — **eligibility NEVER consults office** (T9) | per act | — *(they produce claims at WITNESS)* | `finding.made` | `finding.none` | assumption |
| `kill` / `wound` | 2 | own | `contests: the body` → **the seam** (§39) | `(Person, body)`, `(Person, exists)`, `(Tenure, until)` | `person.died` | — | ruled §30 |
| `speak` | 4 | own | — | — | `speech.made` | — | assumption |

## §E4 · Four properties this table must preserve, and how each is preserved

| property | § | how |
|---|---|---|
| **capability gates no verb** | §9.2 | `eligibility` admits `own`, `remit:`, `hold:`, `presence:` — **and never `capability`.** Rank supplies dice at the seam and appears in no row |
| **an office adds no verb and no modifier** | §11.1 | `remit:` makes an **ordinary** verb eligible. Every verb in the table is available to `own` or via a remit; **none exists only for office-holders**, and no row carries a modifier |
| **scarcity falls out of the fold** | §27.1 | `requires` is checked against the world **its predecessors left**, and failure **emits** rather than raising. No act knows another existed |
| **no second resolver** | §27.2 | the table is **data**. One `resolve` reads it. A verb needing behaviour the columns cannot express is **`grade: absent`**, never a special case |

## §E5 · What is honestly still open in this table

**Three rows carry `absent` and one carries a hazard**, stated rather than filled:

- **`determine`** cannot execute until `judging_set_rule` is stated (**D11**). *Nothing is decided at
  a sitting* until then — the single most consequential `absent` in the document.
- **`refract`** cannot execute until emitter-vs-receiver is picked (**D18**).
- **the six investigation acts** are `assumption`: T9 makes them first-class and no section says what
  they write.
- ⚠ **`create_record` and `forge` have no cost.** With **D19** unresolved a character may create
  arbitrarily many Records per act-budget slot. Named here so an implementer does not discover it.

---

# PART F · THE PERSON'S DECISION — `q`, `choose`, `budget`, `standing`

**Four holes, one subject: what a person actually does at DELIBERATE.** #353 types every signature
here and supplies no body for any of them, which is why the session's every option set was an
authored roster — the exact property §17 chose `Candidate[]` to protect.

## §F1 · `q` and the Candidate derivation — **D2**

> **A question is produced by exactly three sources, and by nothing else:**
>
> **Q1 · A Date coming due** whose DocketItem names a matter, for every person in its judging set.
> **Q2 · A claim landing in the holder's ledger** at WITNESS whose subject is that person, something
> they hold, or a Proposition they have committed to.
> **Q3 · A Sensation band change** — `subsistence` crossing a floor since last season.
>
> **All three are already produced by the loop.** Q1 is CALENDAR's own output; Q2 is WITNESS's
> deposit; Q3 is the person-side reading of D22's emission. **No new step, no new carrier, no clock.**

```
opening_set(p, view, q) -> Candidate[]
  = { Candidate(verb, subject, why) :
        verb        ∈ §E's table
      , eligibility(verb, p) holds        -- own | remit | hold | presence, NEVER capability
      , subject     ∈ referents(q)        -- what the question is ABOUT
      , requires(verb) not KNOWN-false FROM p's OWN CLAIMS
    }
```

⚠ **The third clause is the whole epistemic design and must not be softened to *"requires holds"*.**
The person filters on what **they believe**, so a person who *wrongly* believes the granary full
still forms the Candidate, acts, and gets `transfer.refused` from the fold. **That is T3 and L2
working; a filter on world truth would be `choose` reading the world.**

## §F2 · `choose` — the NPC decision policy — **D21**

`grade: assumption`. **The shape is ruled** (§3 L1, §9, §26); only the weighting is open, and §G's
discipline therefore applies: declare it, default it, sweep it.

```
choose(p, view, sensation, ask_budget) -> Act[]
  candidates = opening_set(p, view, q)
  score(c)   = Σ_axis  conviction[axis] · alignment(c.verb, axis)      -- §9's closed 13
             + stance_toward(c.subject, from p's OWN stance rows)      -- §9
             + urgency(sensation.subsistence)                          -- §18.2's computable half
  return the top `ask_budget()` candidates, ORDERED by score
```

**Four properties, each load-bearing:**

1. **Every input is person-side.** `convictions`, `stance`, the View's claims, and the two Sensation
   scalars. No World, no resolver-side Query. **L2 by parameter list.**
2. **It finally consumes `convictions` and `stance`**, which #353 declares as fields and no formula
   reads — a carrier nothing consumes is dead state, which is §22.1's own complaint.
3. **The person triages.** `ask_budget()` is asked, not imposed; over-budget is the *caller's*
   defect. **An engine that truncates has made the choice, which is L1.**
4. ⚠ **A lookup on one's own interior is indistinguishable from a deliberation at this boundary**,
   and the design does not claim otherwise. The corpus contains a source that calls one act **both**
   *"chooses"* **and** *"determined by a threshold lookup… a stat, not a deliberation"*. **The shape
   inherits the blur rather than resolving it**, and that is an accepted state, not an oversight.

## §F3 · `budget` — resolved by precedent, not escalated — **D4**

#353 §26 types it `(Person, View) -> int` with **no World**; §26.3 says it varies by **office,
condition and distance travelled** — all three resolver-side, and travel legs unowned. **Both cannot
hold.** `CLAUDE.md` §0's five tests resolve it at step 4, **precedent**, without a ruling:

> **`sense : (Person, frozen_world) -> Sensation` is #353's own precedent** — *"the ONE non-decision
> function permitted a `World`"*. `budget` is the same shape: a non-decision reading of the frozen
> world, computed **at the DELIBERATE barrier**, handed to `choose` as an integer.

```
budget(w, p) -> int          -- computed AT THE BARRIER, like sense()
  = base                                    -- params; the ruled ~5
  + office_bonus(hold Tenures p is subject of)
  − condition_penalty(p's body band)
  − distance_penalty(p's travel legs this season)      -- now owned, §D4
```

**`choose` still receives no World** — it receives the integer, by asking. The person still triages.
**§26's signature changes; §26.3's consequence 1 becomes true for the first time.**

## §F4 · `standing` — one formula, and the law #353 cites is the wrong one — **D3**

The session's ledger said the obvious computation is barred by §22.4 clause 2. **That is wrong**:
clause 2 governs **resolver-side Queries**, and `sense()` is explicitly not one. **The real bar is
§20** — *"Claims live in the holder's own ledger… Nobody else may read or write it."*

Which points straight at the answer:

```
standing(p) = agreement( claims in p's OWN ledger
                         where subject == p and source == told_by
                       , p's own convictions )
```

**What people have TOLD you they read off you, against what you hold.** §18.2's own words —
*"the gap between what everyone reads off you and what you hold"* — with *everyone* correctly read
as **everyone who told you**, which is the only version a person can have.

**Three properties it buys, and they are the reason to prefer it to deleting the scalar:**
it is computable **person-side**, it is **wrong-able** (a liar moves your standing, which is T3), and
it needs **no cross-holder read**, so clause 2 is untouched.

> **If this is refused, the honest alternative is to shrink `Sensation` to ONE scalar and stop
> saying "exactly two".** What is not available is keeping the sentence and supplying no formula:
> that is what made `standing` a blocker on 9 cases for a value nothing could produce.

---

# PART G · THE DELEGATION DOCTRINE — HOW A HOLE IS DECLARED — **D13 / §42.2.1**

**This Part is the hinge.** Everything else is content; this is the rule that stops the session's
loop from recurring.

## §G1 · The problem, stated as a contradiction

> 1. **#353 §42.2.1:** *"Where a value is genuinely undecided, the honest state is `grade: absent`
>    and the honest behaviour is to REFUSE, not to pick a plausible number."*
> 2. **An executable loop cannot refuse at sixteen forced holes** and still complete a season.
>
> **Therefore any instrument built from #353 must invent, and every invention is an antagonist's
> finding.** Four rounds; 56 findings; no fixed point. **The contradiction is in the specification,
> not in the instruments.**

## §G2 · The resolution — THE GRADE DECIDES THE BEHAVIOUR

**§42.2.1 is not repealed. It is narrowed to its honest domain, and the domain becomes a column
instead of a judgement.**

| grade | shape of the hole | behaviour | §42.2.1 |
|---|---|---|---|
| **`absent`** | **RULING-shaped**: two defensible options lead to **materially different games** (§62's own test) | **REFUSE.** No default. An instrument that fills it has invented | **unchanged, in full force** |
| **`assumption`** | NUMBER-, SCHEMA-ROW-, FORMULA- or PRODUCER-shaped: **the shape is ruled and only the value or the rule's instance is open** | **INJECT the register's default · DECLARE it a harness fixture · NAME the injection site · SWEEP it.** A verdict that flips across the sweep **is itself a finding, and a more important one than the verdict** | extended from numbers to rows, formulas and producers — **its own words, wider domain** |
| **`measured`** | an execution artifact establishes it | build on it; the command is on the row | unchanged |
| **`ruled`** | a ruling or in-chain adjudication decides it | build on it; the citation is on the row | unchanged |

**The sorting test is `CLAUDE.md` §0's five steps, applied to a hole rather than to a queue row:**
superseded · irrelevant · answered by a design document · **answered by precedent** · answered by
what makes sense for the architecture. **Only what survives all five is `absent`.**

Worked, from this document: **`budget` looked like a ruling and was answered at step 4 by `sense()`'s
precedent** (§F3). **Travel-leg ownership looked like a ruling and was answered at step 4 by §15.1**
(§D4). **Scene-versus-act survives all five and stays `absent`** — two readings, materially different
games, and no precedent reaches it.

## §G3 · Both sides, because the case against is real

**FOR.** The alternative is measurably untestable — this session is the evidence. §42.2.1 *already
contains this discipline* for numbers (*inject, declare, sweep, a flipping verdict is a finding*);
it simply stops at numbers. Extend it to rows, formulas and producers **with the design supplying
the default**, and the invention channel closes **by construction**: an instrument reads the
register, injects exactly what it says, and **an undeclared fill is a red test rather than an
argument**. Rows also survive a session boundary in a way prose does not — #353 §63.2's own finding.

**AGAINST, and it is not weak.** A default written by the design is *a number somebody made up with
better letterhead*. §39.3 is right that *"a default is a number somebody made up, and it will be
cited later as though it were measured."* §42.3 is right that *"configuring an unspecified thing
invents it."* And a default on a **ruling-shaped** hole — scene-vs-act, refraction's side — **silently
picks a game**.

**WHY THE RESOLUTION SURVIVES THE OBJECTION.** Every clause of the case against is an argument about
**`absent`-grade holes**, and `absent` keeps §42.2.1 whole. The objection does not reach a hole whose
*shape* is ruled and whose *value* is open — and §42.2.1's own sweep requirement is what neutralises
the letterhead problem: **a default that changes the verdict is reported as changing it.** The rule
becomes:

> **The honest behaviour is to REFUSE where the register carries no default, and to INJECT the
> register's default — declared, sited and swept — where it does. An instrument that fills anything
> not on the register has invented it, and that is a defect in the instrument.**

## §G4 · The register row

```yaml
- id:        H-NN
  hole:      <one sentence: what the specification does not say>
  kind:      NUMBER | SCHEMA_ROW | FORMULA | PRODUCER | RULING
  owner:     <the §22 row that will own it once filled>
  grade:     ruled | measured | assumption | absent
  default:   <the value/rule an instrument may inject>   # or `none` -> REFUSE
  site:      <where the default is injected; never a literal in a body>
  sweep:     [<three points>]                            # required when grade: assumption
  unblocks:  <count of NPC/arc cases>
  cite:      <§ or command>
```

> **THE POLARITY RULE STILL BINDS, AND HARDER.** §42.2 — *zero evidence maps to the verdict AGAINST
> the thing measured; a row with no grade FAILS THE EXPORT.* **A hole with no row is not
> `assumption` by default. It is a defect in this document.**

---

# PART VII · THE HOLE REGISTER — **replaces #353 §61–§62** — **D14**

**#353 §63.2 makes this document's argument for it:** *"Prose registers are re-typed; rows are
inherited. Fourteen-plus of the census's items were lost at a section restating its neighbours…
This is the argument for graded rows over any prose list of open items."* §61 and §62 were prose
lists of open items. **They are rows now.**

## §VII.1 · TIER 0 — required before ANY season completes

**Ten holes. Until every one is `ruled`, `measured` or `assumption`-with-a-default, no case runs.**

| id | hole | kind | owner | grade | default | unblocks |
|---|---|---|---|---|---|---|
| **H-01** | the `social:` value for every `(kind, field)` in Part II | SCHEMA_ROW ×33 | the design (a static column) | **ruled** — Part D | Part D's table | **all 143** |
| **H-02** | what each verb writes, requires and emits | PRODUCER | the resolver; writes owned per §22 | **ruled** for 24 rows, **absent** for 2, **assumption** for 3 — Part E | Part E's table | **all 143** |
| **H-03** | the NPC decision policy | FORMULA | Person (person-side only) | **assumption** | §F2's scoring function | **all NPC** |
| **H-04** | `q`'s producer and the Candidate derivation | PRODUCER | the date-holder (Q1) · Person (Q2, Q3) | **assumption** | §F1's three sources | **all NPC** |
| **H-05** | the world-generation roster — persons with zero `hold` | SCHEMA_ROW | params (a registry row) | **assumption** | a roster read from a registry row; **not a clock** (§29) | any run |
| **H-06** | the condition scale | NUMBER | params | **assumption** | `1000` | any Site |
| **H-07** | wear per site kind — **NO silent default; an unregistered kind RAISES** | NUMBER ×kinds | params | **assumption** | per-kind table; §42.2.1 names the silent default as the prior sin | any Site |
| **H-08** | band floors per site kind per verb | NUMBER ×kinds | params | **assumption** | per-kind table | L5, §12.1 |
| **H-09** | ledger cap `L` · View `K` · claim confidence | NUMBER ×3 | params | **assumption** | `200` · `12` · `100` | WITNESS, DELIBERATE |
| **H-10** | the **SCENE** budget as an **integer** of the ruled band `~5` *(⚠ **the unit was ruled 2026-09-02**: scenes, not acts — H-35)* | NUMBER | params | **assumption** | `5`; **swept 2·5·9 — the count verdict flips, which is the finding** | DELIBERATE |
| **H-11** | the subsistence formula over an **open** `MatterKind` registry | FORMULA | Rung (matter) + params | **assumption** | draw from the containing rung's stores, scaled by weight | `Sensation` |
| **H-12** | MATTER emits an Event per write so crossings have an antecedent | PRODUCER | the log | **ruled** — D22 | Part D's `emits:` column | every crossing |

## §VII.2 · TIER 1 — what the corpus then hits, ranked by core blocks

| id | hole | kind | owner | grade | default | unblocks |
|---|---|---|---|---|---|---|
| **H-20** | L3 clause 1's **closed axis registry**, and the row admitting the increment | RULING (roster) + SCHEMA_ROW | the design owns the registry; **Person owns the counter** | **assumption** for the row (Part D) · **absent** for the roster | the row is `(Person, axis_count[axis])`; ⚠ the axis must **not** be spelled `exposure` bare — §54 item 6's collision with the need scalar | **~28** |
| **H-21** | material vs social pooling | RULING — **answered by design document** | Rung / Office (matter) | **ruled** — D26 | *"a faction's treasury is matter at the rung or office that holds it; L3 refuses pooled **social** quantities"* | **~19** |
| **H-22** | `Record` rows: `exists`, `ttl`, `stages`, `matured`, `forgery_quality` | SCHEMA_ROW ×5 | Record; the `hold` Tenure is the holder's | **ruled** — Part D | Part D | **~13** |
| **H-23** | act cost beyond budget consumption | RULING → FORMULA | params | **absent** | none — §63.1 may accept it instead | ~7 |
| **H-24** | `(Person, exists)` | SCHEMA_ROW | the design | **ruled** — Part D, bounded by §15.3 | Part D | every death |
| **H-25** | a termination bound per self-feeding loop | RULING | — | **absent** | none. ⚠ **three of four in-chain feedback loops name no off-switch and the fourth's is self-defeating** | ~4 |
| **H-26** | `season_factor`'s distribution — **blocks `yield`** | SCHEMA_ROW | params | **absent** | none | 1 |
| **H-27** | travel-leg ownership | SCHEMA_ROW | **Person, as the Tenure's subject** | **ruled** — §D4, by precedent | §15.1 | 1 |
| **H-28** | `budget`'s placement | RULING — **answered by precedent** | resolver-side, barrier-computed | **ruled** — §F3 | `sense()` | every "wounded duke" |
| **H-29** | `standing`'s formula | FORMULA | Person | **assumption** | §F4's agreement over own `told_by` claims | 2 |
| **H-30** | person-order vs global canonical order | RULING — **answered by architecture** | the resolver | **assumption** | composite key `(stratum, actor-hash, intra-person position)` — honours both | 2 |
| **H-31** | the degree ladder's margin model | FORMULA | params (the one ladder) | **absent** | none. ⚠ **every contest is blocked** | every contest |
| **H-32** | `judging_set_rule` | RULING | Rung | **absent** | none. ⚠ **nothing is decided at a sitting** | 2 |
| **H-33** | the five witness channel predicates | FORMULA ×5 | the presence index (Nobody) | **absent** | none. ⚠ **fan-out is total; nothing said in private is private** | 1 |
| **H-34** | establishment size per office kind | NUMBER | params | **assumption** | a per-kind number | 1 |
| **H-35** | **does a scene equal an act?** | RULING | **Jordan** | ✅ **RULED 2026-09-02** — *"5 scenes for a character to play per season"* | **the SCENE is the budgeted unit; the number is 5; every character has it.** Interactions-per-scene (1–3) and extended-scene cost (2) become **`assumption` rows**, cited to `player_agency_v30.md` §6.3 and swept. See `PLAN.md` §3.4 and **W17** | 1 |
| **H-36** | refraction: emitter- or receiver-side, and by how much | RULING + FORMULA | the design; params | **absent** | none | 2 |
| **H-37** | the argument layer's named-fault roster | SCHEMA_ROW | the design | **absent** | none | 2 |
| **H-38** | does a person carry a banded scalar? | RULING | Person, or refused | **absent** | none | 2 |
| **H-39** | the cohort's construal spread — the rule is stated, the representation is not | SCHEMA_ROW | Person | **absent** | none | — |

## §VII.3 · What the register says about itself

| | count |
|---|---|
| holes total | **39** |
| `ruled` — decided here or in chain | **8** |
| `assumption` — default supplied, sweep required | **13** |
| **`absent` — REFUSE; §42.2.1 in full force** | **12** |
| mixed grade | 1 (H-20) |

> **TWELVE `absent` HOLES IS THE HONEST STATE, AND IT IS A BETTER STATE THAN #353's.** #353 had the
> same holes and did not enumerate them, so an implementer met them one at a time, at the keyboard,
> and filled them silently. **Twelve refusals a reader can count is worth more than an unknown
> number an instrument fills.**

⚠ **CORRECTED 2026-09-02 — ZERO of the twelve are live escalations.** `H-35` was **ruled by Jordan** (above); `H-36` closes receiver-side on architecture and `H-38` on precedent — see `PLAN.md` §3.1–§3.4, which runs `CLAUDE.md` §0's five tests over all twelve and closes or downgrades eleven **in chain**. The sentence below is the pre-adjudication claim, kept so the correction is legible.

~~**Three of the twelve are genuine escalations**~~ — H-35 (scene=act), H-36 (refraction's side), H-38
(a person's banded scalar): each is two defensible options leading to materially different games.
**The other nine are authoring work**, not decisions: someone must write a margin model, a judging
rule, five channel predicates, a fault roster, a distribution, a termination argument, a cost model.

---

# PART H · THE METHOD FOR THE NEXT INSTRUMENT

**24 of the session's 56 findings were method, not design.** A successor specification that fixes
only the design will be measured by an instrument that repeats them.

## §H1 · Declare, do not route — #353 §44.4, applied to the harness

> *"A 114-line regex router 'reconstructing a fact the case author knew at authoring time' produced
> eleven unreachable probes and a 46% miss rate. **The ruling is: don't route — declare.**"*

**The ruling governs key-type routing inside the engine. It describes the harness exactly.** Five
recurrences of the bare-token class; 60 of 143 cases NOT-ASSESSED; both surviving PLAYABLEs
artifacts. **Every `season_requires` row carries the verb or contract it exercises, authored with
the row.** NOT-ASSESSED then means *"nobody said what this needs"* — a fact about authoring, which
is fixable — instead of *"the regex missed"*, which is not.

## §H2 · Five rules, each earned by a specific failure

| rule | the failure that earned it |
|---|---|
| **A fill off the register is a defect** | 24 avoidable inventions across four revisions |
| **No route decisive on a single common word** — forbid the shape, never enumerate the words | five recurrences; the whitelist built for the fourth did not catch the fifth |
| **Every probe declares how its verdict was reached** — `construction \| no-signature \| convention \| probe-model` | eleven probes raised gaps by hand and reported them as the shape's |
| **A refusal is not an invention, and an over-refusal is a defect of equal weight** | seven over-refusals; one survived all four passes and cost ten arcs |
| **A test must assert the property, never the string** | a control that computed `differing=False` and asserted it had fired; a pin on `stated == [one row]` when the head states two |

## §H3 · What an instrument built from this document does differently

1. **Reads Part D** — no Partition to invent; an unmarked cell raises with the pair named.
2. **Reads Part E** — one `resolve`, no per-probe `effect` lambdas. **Cases RUN rather than being
   graded.**
3. **Reads Part VII** — injects exactly the defaults, at the named sites, and sweeps every
   `assumption`. **Anything else is a red test.**
4. **Refuses at the twelve `absent` holes and reports which case each stops.** That report is the
   next authoring queue, and it is the deliverable a second run should produce.

---

# PART I · WHAT THIS BUYS — the claim, and how to falsify it

**A specification does not become executable by being longer.** The claim is specific:

| change | mechanism | cases |
|---|---|---|
| **Part D** — the `(kind, field)` matrix | `write()` stops guessing; the forced Partition loop ends | **all**, and it is the precondition for the rest |
| **Part E** — the verb table | one resolver runs every case; **"executes end to end" acquires a meaning** | **all** |
| **§F1–F2** — `q` and `choose` | option sets are computed, not authored | **all NPC** |
| **H-20** — the axis registry + row | the corpus's largest non-refusal blocker | **~28** |
| **H-21** — material vs social | an over-refusal that cost ten arcs | **~19** |
| **H-22** — the five Record rows | every Record write stops being an unmarked cell | **~13** |
| **§H1** — declared routing | 60 NOT-ASSESSED become a fact about authoring | **60 assessable** |

**And what it does not buy, stated so the claim is falsifiable:** ~22 core blocks remain — a Rung
storing a social aggregate, a threshold producing an outcome, a fourth clock, a faction acting, a
GM. **Those stay refused.** The arcs that want them are re-authored against §36.3 and §37, which
already give the *"a counter compels a named person"* shape that **19 of 50 arcs** were asking for.

## §I1 · The falsifiers

| claim | what would prove it wrong |
|---|---|
| Part D makes `write()` total | one `(kind, field)` the loop touches that the table does not carry |
| Part E gives the resolver a body | a case whose season needs a verb the table has no row for **and** that #353 does not name |
| §F1's three sources produce every question | a case needing a question that is not a Date, a claim, or a band change |
| §F3 resolves `budget` by precedent | show `sense()` is not a precedent for a barrier-computed non-decision read |
| §F4's `standing` needs no cross-holder read | show that agreement over one's own `told_by` claims reads another ledger |
| §G's grade-decides rule preserves §42.2.1 | an `absent` hole this document supplies a default for |
| **the register is complete** | **a hole an instrument must fill that carries no row.** This is the falsifier that matters; it is the session's failure restated as a test |

## §I2 · What would make this DONE — §0.2's standard, unchanged

**Nothing here runs.** Under `CLAUDE.md` §0.2 a juncture is done when the behaviour **executes**.

| # | artifact | proves | satisfiable by writing? |
|---|---|---|---|
| **0** | **Part VII has no `absent` row in Tier 0** | a season can complete without inventing | yes — and it is the only one that can |

> ⚠ **ARTIFACT 0 IS UNMET, AND THIS DOCUMENT DID NOT SAY SO — corrected 2026-09-02 by `W0`.**
> It is unmet on this document's **own `H-02`**, which is Tier 0 and carries `absent` for two of
> its rows, and — once the twenty-two holes `PLAN.md` §1.4 found with no row at all are carried —
> on eight more. The register is data now, so the claim is no longer a sentence to be trusted:
> `python proposals/2026-09-01-season-loop-tests/tracer/register.py --counts` computes it and
> **names every Tier 0 row that keeps it unmet.** `W1` and `W3` are the items that close them.

| 1 | `Event :=` mapped onto the log, `source_actor` absent, `causes: [ROOT]` for antecedent-free | §19, #353 §54.4 — **still the first thing to do** | no |
| 2 | **One NPC's season runs end to end from Parts D+E+F, emitting a log whose `causes[]` chain walks** | the three that matter | ⚠ **no** |
| 3 | The same for one arc | | ⚠ **no** |
| 4 | A seeded 2-season run twice, byte-identical including the hash, **with a float build producing a DIFFERENT hash** | §32/§48 — the control must fire | ⚠ **no** |
| 5 | Every `assumption` swept 3 points; **every verdict that flips is reported** | §G, §42.2.1 | ⚠ **no** |
| 6 | An instrument run with **zero fills off the register** | §G's central claim | ⚠ **no** |
| 7 | The 46 NPCs and 97 arcs re-run with **declared** routing; NOT-ASSESSED explained per case | §H1 | ⚠ **no** |
| 8 | **The twelve Jordan trajectory transitions as executable cases** | #353 §66 artifact 10 — **the only supplied acceptance set in the chain, and a runner has still never run it** | ⚠ **no** |

> ### **ARTIFACT 2 IS THE BAR. THE TESTED VERSION RAN ZERO CASES END TO END.**
> **One is an infinite improvement over zero**, and it is the only number in this document that
> would prove any of it. Artifact 8 remains the one that would settle the most, and this session —
> having run 143 cases — did not run the twelve that were actually supplied.

---

## §J · WHAT THIS DOCUMENT DOES NOT DO

- **It does not decide the twelve `absent` holes.** Three are genuine escalations; nine are
  authoring work. Filling them here would be the invention it was written to end.
- **It does not re-argue Parts I–VI of #353**, which the session confirmed by execution.
- **It does not weaken a single refusal in Part VIII.** The ~22 cases those cost are named, counted,
  and left refused.
- **It does not claim the case verdicts of the session it rests on.** Two independent auditors ruled
  them uncitable in either direction; **only the probe ledger is cited here**, and every count above
  traces to a probe execution or to a mechanical extraction from the tree.
- **Nothing in it runs.** Part I §I2 says what would change that, and marks the seven steps that
  cannot be satisfied by writing.

**No `ED` allocated.** A gap in a PROPOSED architecture gets no ID; the adoption decision gets one.
