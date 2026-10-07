---
name: ners
description: >
  THE NERS PASS — the cut test on any design object, mechanism or suite: propose the cut and name
  what dies. Graded on FALSE N-LINES — cuts that turn out free because something already ruled in
  provides the lost possibility. The definitions live in CLAUDE.md §0.06; this skill owns the method.
  For anything resolved by a draw, run `resolution-diagnostic` and bring its findings back here as
  evidence. Use for: NERS audit/pass/review, "is this necessary/elegant/robust", false N-line, "does
  this add a system", "is one option dominant", "does this propagate across scales", grading or
  auditing a mechanic or design. Not for internal-consistency checks with no cut question
  (valoria-mechanic-audit), contract/seam closure (read `references/module_contracts.yaml`
  directly), or stressing a draw on its own (resolution-diagnostic).
---

# NERS

## THE THROUGHLINE — one operation, four times

**NERS is a cut test**, graded on the cuts that turn out free (§3). Each axis proposes a cut:

| axis | the cut you propose | what must die, or the axis fails |
|---|---|---|
| **N** | remove the object | **a thing the game could do and now cannot** — an emergent possibility, a robust choice, a clean integration; never a number or a feature (§2) |
| **E** | remove **more** | **nothing** — and what is left must still be simple to read and to intuit from, not merely small (§5) |
| **R** | remove the alternatives | **the choice, and the drama.** One dominant option makes the seat a corridor; a seat that emits nothing unwatched is dead (§6) |
| **S** | remove the rung, or the seam | **the propagation** — up, down, or across a scale transition that must pause and hand off cleanly (§7) |

**Three properties keep the pass honest:**

1. **A PASS is licensed by a NAMED FAILED ATTACK, not by the absence of a finding** — *"I attacked X
   as a violation of Y and it holds, because Z."* Every verdict names what would overturn it
   (CLAUDE.md §0.1 pt 3) and states its **residual**, the qualification that survives it. A clean
   result stands only **on its trail**.
2. **Withholding is symmetric.** A precondition that blocks an unfavourable verdict blocks the
   favourable ones too; banking those is **asymmetric skepticism** (CLAUDE.md §0.1 pt 4).
3. **The pass fires on itself, and on the tree as well as the shape.** A pass that did not RUN §9
   has not run; §9 owes its trail, not a finding — a required finding is manufacture. A shape that
   passes while nothing executes is **paper** (§10).

## THE CHARTER — where the definitions live

**The four definitions are canon in `CLAUDE.md` §0.06 — READ THEM THERE.** This file owns the
method; each test quotes the clause it is run against, since a test whose criterion is elsewhere is
not a test. It argues two readings: **E as a ratio** (Rule 1) and **R's player half scoped to
occupiable seats** (Rule 3). **Where a quotation here and §0.06 diverge, §0.06 is right and this
file is the defect.**

## THE FOUR RULES — how to SCORE the charter (CLAUDE.md §0.06) without mis-scoring it

### RULE 1 — E IS SCORED AS A RATIO AGAINST N AND R, NEVER AS AN INDEPENDENT AXIS

Score E **last**, against what N and R found (CLAUDE.md §0.06): *distil as far as possible **without
losing emergent possibilities or robust choosing for the player**.* "Ratio" is an ordering rule, not
arithmetic — E has no value until you know what the cuts cost. **An audit that scores four axes and
averages them rates an amputated design as elegant.**

### RULE 2 — S IS PROPAGATION IN ALL SIX DIRECTIONS, NOT A STYLISTIC JUDGMENT

"Integrates cleanly" is not a test. Run the directions — **S-UP** and **S-DOWN**, the ladder readings
of top-down and bottom-up (§7.1), then the other four (§7.2) — and the charter's two extras as tests,
not adjectives (§7.3).

### RULE 3 — R-PLAYER BINDS AT SEATS A PLAYER CAN OCCUPY; R-WORLD BINDS EVERYWHERE

- **R-PLAYER** — strategy, customization, variety, feeling important and impactful — binds **at
  seats a player can occupy**; answer *"is this seat playable?"* **per seat** first (§6.1).
  Elsewhere a dominant act is a **portrait** (a duke who always does the same thing), not a defect.
- **R-WORLD** — *"emergent and compelling narrative hooks and scenarios without player involvement"*
  — binds **everywhere**. A portrait passes **only while it still throws hooks**; a seat resolving
  the same way every season with nothing coming out of it is a **dead seat**, and fails R-WORLD.

### THE META-RULE — A FIX THAT ADDS A SYSTEM HAS FAILED

The remediation standard: **a few edits, most of them deletions, leaving the vocabulary shorter.**
A remedy adding an object, store, gauge, table or guard is presumed failed, must argue its way out,
and must be load-bearing on the game, the exported params, the port or a Jordan decision (CLAUDE.md
§0.1 pt 5). Apparatus that guards apparatus is refused outright. A fix that adds overhead cannot
improve E.

## §1 · SCOPE — two instruments, one verdict

The pass applies to any design object, mechanism, act, verb, gauge, edge or suite; it needs no draw.

| instrument | when | produces |
|---|---|---|
| **A — the object ledger** (§2–§9) | always | N-lines, false N-lines, the E ratio, the R gain/cost tables, the S traces |
| **B — the `resolution-diagnostic` skill** (Phases 0–6) | the target resolves an outcome by a **draw** | stress points and property violations against the **one** engine: σ-leverage μ-shift over the d10 substrate, fractional pool and fractional Ob |

B is **evidence, not a verdict**: its findings enter A's ledger. A target with no draw runs A alone —
a normal pass, not an out-of-scope one.

**Routes elsewhere.** Consistency with no cut question (formula gap, dangling cross-reference,
redundant definition) → `valoria-mechanic-audit`; contract/seam closure → read
`references/module_contracts.yaml` directly; corpus vocabulary and isolates → `valoria-vector-audit`.

**Resolve the canonical head first** (`CURRENT.md`, then its `## Status:` line); **a superseded
head produces a void pass.** Read the target from the working tree; it need not be canon. Where canon
and code disagree, audit the code (CLAUDE.md §0.05) and record the disagreement as a defect in one
of them.

**Cite `file:line`.** A claim with no locus is `[UNGROUNDED]` and cannot carry a verdict.

## §2 · N — THE N-LINE LEDGER

> **No object enters the shape without an N-line.**

An N-line has exactly one form:

```
<object> — cut it and the gameplay experience is worse, because <WHAT THE GAME CAN NO LONGER DO>.
```

The loss may be an emergent possibility or robust choice (R), a clean integration (S), or a
simplification the object was buying (E) — never a *representation*. **Test it from all six
directions** (CLAUDE.md §0.06; §7.2 glosses them for a seam) and name the direction the loss falls
in; an N-line that holds in exactly one direction is **narrowed**, not passing.

| not an N-line | why |
|---|---|
| "it stores X" | a store is not a possibility. Name what the world can no longer *do* |
| "the design references it in four places" | reference count is coupling, not necessity |
| "it makes X legible/tunable/explicit" | an argument for a *representation*, not for the object |
| "without it, Y has no home" | **the load-bearing false-N pattern.** Check whether Y already has one — §3 |
| "it would be needed if Z were built" | an object with **no producer** cannot have an N-line |

- **N HOLDS** — the possibility dies with the cut, and an attack failed to save it.
- **N HOLDS, NARROWED** — it partly survives via something else, or holds in one direction only. ⚠
  **RESTATE the N-line in its narrowed form**; never leave the headline standing (§9a).
- **FALSE N-LINE** — the possibility survives the cut. Go to §3.

**The attack on every N-line:** assume the object gone; walk the claimed loss step by step, naming
the object that carries each step. Every step carried by something else: the N-line is false. A step
with nothing to name: N holds, and **that step is the N-line** — restate it narrowly.

## §3 · THE FALSE N-LINE — the highest-value finding this pass can produce

> **An object whose claimed lost possibility ACTUALLY SURVIVES THE CUT, because something already
> ruled in provides it.**

**The signature:** a mechanism was named · a **store** was proposed for it · the store's job was
**already being done by an object the design had ruled in**.

**Any one of five disqualifiers fires a false N-line:**

| # | disqualifier | the question that detects it |
|---|---|---|
| 1 | **the carrier already exists** | is this already stored, on an object that can also be *contested, planted or refuted*? Knowledge on the thing known is two owners and no knower |
| 2 | **no producer** | who writes this, by what act? An object nothing produces has an unreachable possibility |
| 3 | **already cut, and the cut applied** | proposed and rejected before? A re-addition names the prior cut and what changed; re-adding **without mentioning the cut existed** is the failure |
| 4 | **a reward for a behaviour the ranking already weights** | if convictions already weight the choice and stance already gates salience, a bonus on top is a second thumb on one scale |
| 5 | **the residue is a flat bonus** | stripped of everything else, does it reduce to "+X"? A flat pool bonus is the shape a design refuses; the object was the wrapper |

### §3.1 The two evasions that get an addition out of the dock

- **"It is only a NAMING of what the corpus already does."** ⚠ **Produce the exact shipped
  instances.** Shipping the **halves** of a composition — a predicate here, a scheduler there — is
  not shipping the composition. **Zero exact instances: it is an addition, and must win on its N-line.**
- **"It is free — it costs no code."** Check the **denominator** (§5.1): what must be *attached, set
  or authored* has a cost even when its implementation is empty.

### §3.2 The null result

No false N-line is legitimate **only with its trail** — the N-lines examined, the walk run on each,
at least one attack named and failed. **Never manufacture a false N-line to have produced one.**

## §4 · THE FIVE CROSS-CUTTING CHECKS

Run these while you read, not at a stage.

### C1 — CLAIM → MECHANISM. *Is this claim carried by an object, or is it prose?*
For every behavioural promise ("neglect becomes attributable"), name the carrying object and the act
that emits it. **A promise with no carrier is unmechanized.** Sweep every section advertising it.

### C2 — TYPE SIGNATURE. *Does the type admit the input the claim requires?*
If the claim needs `witness` to see an omission, `witness` takes **events**, and **an omission emits
none**, the claim **contradicts the signature**. Read the signature, not the description.

### C3 — EPISTEMIC FEASIBILITY. *Who evaluates this, and from what they can actually know?*
A predicate must be evaluable by a named party from state that party can reach. A world-scale
semantic judgment ("the matter is no longer live") in a per-person-claims design is **either a
forbidden stored world-condition or an omniscient oracle**. The repair: **evaluate it at a venue,
from claims a named person holds, contestable like any other claim.**

### C4 — CONTRADICTION SWEEP. *Do two sections rule the same fact pattern opposite ways?*
Match the fact pattern, not the wording: §A forbids deduplication as "an engine deciding a person's
options" while §B expires an item because another resolved the same need. Check for a missing
evaluator (C3) behind it. **Include contradictions you introduced.**

### C5 — PATH CONSTRUCTION. *Trace the emergent path; name a shipped object at every step.*
Walk the design's own showcase. A shipped object at every step **constructs**; a step needing an
object that does not exist is **asserted**. Claim the constructing half and state the rest as a
limit, or specify the missing object. **Downgrade the verb too** — *implementable* → *expressible*.

## §5 · E — TWO TESTS, SCORED AS A RATIO

E has **two tests**; a mechanism can pass one and fail the other. Score both after N and R (Rule 1).

- **E-OVERHEAD** — *logically simple, clear approach, no unnecessary overhead.* **Count, don't
  characterise:** objects in vs out · verbs added vs folded · whether the biggest moves are
  **deletions** · whether the **vocabulary got shorter**. An "elegant" verdict with no counts is not
  an E-OVERHEAD verdict.
- **E-LEGIBILITY** — *easy to understand; the player can **intuit complex outcomes from simple
  choices**.* Counting cannot reach it: *can the player predict the outcome's shape from the choice
  without simulating the engine?* It fails on a choice whose consequence is knowable only by running
  it, or an outcome emerging from opaque interaction of simple parts — even when nothing could be cut.

### §5.1 The denominator is the half that gets understated

Find every "free" mechanism's denominator by asking where its inputs come from.

- A predicate must be **set by someone**: by persons **by an act** — what does the act cost, and does
  setting it freely become a denial-of-service on the office that must service it? — or by an
  **authored inventory** the design ships.
- **If the design boasts of needing no authored inventory and its mechanism requires one, the boast
  is false as filed.** Say so in those terms — the highest-yield E finding, invisible to an object
  count.
- A new owner of state is a **new owner**: if the compliance table admits four owners and the
  mechanism gives a fifth durable state, add that row explicitly.

### §5.2 Over-distillation — the ratio cuts both ways

Keep an explicit watchlist: for each unification or removal, name **the N it protects** and give a
verdict with confidence.

| watched | the N it protects | verdict |
|---|---|---|
| *(two channels unified onto one type)* | *(the distinct depth each channel had)* | kept, at MEDIUM confidence — the payload split is real and the unification may be one step too far |
| *(a three-state domain collapsed to a boolean)* | *(the third state)* | cut — nothing produced the third state |

**"Kept, at MEDIUM confidence" is a real verdict**, reported under E-OVERHEAD in §10's table with the
watchlist. A watchlist of only `kept — fine` rows means the watch was not run.

## §6 · R — FOUR TESTS, ONE INSTRUMENT

| test | the question | fails when |
|---|---|---|
| **R-COMPLETE** | are the mechanics **fully formed, error-free and complete**? | it breaks at its extremes, has an unwritten branch, or a claimed behaviour has no carrier (§4 C1/C2). For anything that rolls, `resolution-diagnostic`'s **P-iii and P-iv** are this test; its other properties land on E-LEGIBILITY and S (that skill's §6 maps them) |
| **R-VARIETY** | does it permit **customization** and **creativity/variety in approach and resolution**? | one build, one line of play, or one right answer to every situation |
| **R-WORLD** | does it produce **emergent hooks and scenarios WITHOUT player involvement**? | a **dead seat** — the portrait defence does not cover it (Rule 3) |
| **R-CHOICE** | does the player **think strategically** and **feel they impact the world**? | **one option dominates** — the instrument below |

**R-CHOICE's instrument.** For each **seat a player can occupy** and each **intent** available
there, tabulate the acts that reach it and read dominance off the table in one of three shapes:

```
SEAT: <who>                 INTENT: <what they want>
| act | gain | cost |
```

| shape | what it looks like |
|---|---|
| **strict** | one row's gain ≥ every other row's, and its cost is strictly lower |
| **decaying cost** | identical gain; one row's cost **depends on someone choosing to report it**, so it decays toward zero — the table reads balanced at a point |
| **shape mismatch** | gain decays over time while cost compounds (or the reverse): dominance over the horizon, invisible at a point. **Compare the shapes, not the values** |

> **SILENCE BEATS REFUSAL.** Where two options reach one outcome and only one emits an event, **the
> silent one dominates** — costs attach only to events. A **design failure under Rule 3, not a
> balance note**; repair: a lapse, a supersession, a quiet expiry each **emits a witnessable event at
> the venue** — the precedent is normally already there (§12).

### §6.1 The precondition — and the line where it becomes an evasion

**Rule 3's seat question gates R-CHOICE and R-VARIETY only.** ⚠ "R: NOT SCORABLE" with R-COMPLETE
and R-WORLD unattempted is the precondition used as cover. Nor does an unanswered precondition
license stopping on the two it gates:

- **Where the design's own laws answer it, it is answered** — e.g. the player is an ordinary Person,
  a played-flag is a fidelity setting, player-only mechanisms are refused, every rung is occupiable.
- **Escalate only what remains** — *which seats a campaign OFFERS AT START* — never the general
  question.
- ⚠ **Favourable R findings made under an unanswered precondition are PROVISIONAL.**

### §6.2 The two rules that keep an R verdict honest

- **Any "no dominant option" claim is an UPPER BOUND, not an estimate.** You looked and did not find
  one; that is not the same as there not being one. Say *upper bound*.
- **Do not bank R without two-arm artifacts.** A number with no control is not a measurement in
  either direction (CLAUDE.md §0.1 pt 4). For a campaign-level R question the two-arm instrument is
  `tools/balance_oracle.py` — but note it is a **campaign** instrument: for a change that is
  campaign-unreachable both arms are identical by construction, and running it would be a fake
  control.

### §6.3 R verdicts carry their dependency

**The act economy is the denominator of nearly every R verdict.** Under one act per person per
season, three petitions cost three seasons; under a multi-act reading the same set is petition-spray
and one row dominates. **State the dependency** — *"R for X cannot be ruled until the act economy
is"* — rather than scoring around it.

## §7 · S — SIX DIRECTIONS, PLUS TWO TESTS THE SHORTHAND DROPS

### §7.1 The two directions a design most often only claims

**S-UP.** Can a demand travel up and be **filtered by a named person at a rung**? It passes when the
demand is a **real object**, carried by an **accountable party** who **spends something to carry
it**, and **droppable only by someone who pays for dropping it** — never a threshold, never a
probability. In the season loop: a demand on a **dated docket**, dropped by a **convener** who pays.

**S-DOWN.** Can an opportunity reach **a party that holds no post**? It passes when the opportunity
is **published, not addressed**, **distorts in transit**, and is picked up through the recipient's
**own** perception — **nobody authors an opportunity for anybody**, so one routed to a recipient by
name fails. In the season loop: a **telling**.

⚠ **A target with no ladder at its scale scores `N-A`, not FAIL** (a dice resolver has no docket).

### §7.2 The coverage sweep — all six

Run the other four directions as a table, naming the seam that carries each or recording the gap:

| direction | what it means here | carried by |
|---|---|---|
| **vertical** | a cross-scale handoff | |
| **diagonal** | cross-scale **and** cross-family | |
| **lateral / horizontal** | same-scale edges between siblings | |

⚠ The **aggregate** senses of top-down and bottom-up — an aggregate constraining its substrate, the
substrate recomputing the aggregate — are a second live reading of §7.1's words. Say which you ran.

A direction with **no** carrier is an S finding. A carrier whose targets are unpopulated **delivers
blind** — the same defect one step later.

### §7.3 The charter's two extra tests

- **PAUSES CORRECTLY.** When another system or scale is called for, does this one **stop**, hand off
  and resume? Ticking on through a scale it should yield to fails S even when every edge is wired.
- **CALCULATIONS CONSISTENT IN METHODOLOGY.** Do sibling mechanics compute the same *kind* of thing
  the same way? Two ladders, two leverage conventions or two bandings of one quantity is an S defect
  even when each is individually correct.

### §7.4 Attacks worth running on S, both of which can legitimately fail

- *"It is identically zero at the bottom"* — fails if the mechanism **mints its own surface** at the
  bottom rung rather than dividing an existing one.
- *"It stores a world condition"* — fails if the predicate is scoped to the holder's **own state** or
  to a **compute-on-demand aggregate** rather than a stored gauge.

> ⚠ **SCORE THE SHAPE AND THE TREE SEPARATELY, AND SAY BOTH** — a shape can pass S while the tree
> scores **zero** (no demand object, no persons). Name the execution step that is the difference.

## §8 · RUN THE DESIGN'S OWN FALSIFIER

A design's stated discipline — *every effect traces to a self-interested act*, *no engine decides a
person's options*, *no authored trigger inventory* — is **run, not cited**.

1. **Enumerate the hits** — the places the discipline is broken.
2. **Classify each:** clean hit · borderline · **passes by tracing** (looks engine-supplied but
   traces back to an act, possibly seasons earlier — say which act).
3. **Cluster the clean hits into families.** Few, scattered hits: the discipline is real. Few hits
   **all in one family**: the discipline is real *and* the design's own exception list is
   incomplete — name the missing family.
4. ⚠ **License the settled member narrowly; make the live ones trace to persons** — never license
   the whole family. If the repair is not a free one-liner, say so.

## §9 · THE SELF-AUDIT — terminal, and not optional

Run both sweeps and report what each turned up. Never invent a finding to fill this stage.

**9a — BACKWARD PROPAGATION.** **Did later corrections propagate backward?** The residue:
- an early summary table still printing a figure a later section corrected;
- an early section claiming a benefit a later narrowing downgraded (*restored* → *reachable*;
  *implementable* → *expressible*) — §2's restatement rule;
- a claim derived for a form you withdrew, never re-derived for the form you kept;
- a count ("four shipped instances") a later section reduced to zero.

**A self-retraction in one section obliges the same operation on every other section.**

**9b — TURN §3 ON YOUR OWN ADDITIONS** — the pass itself and any object **this** work added, first
of all one the source had already cut (disqualifier 3). If any disqualifier fires, **delete it in
this commit.**

Prepend `[SELF-AUTHORED — bias risk]` when auditing this or a prior session's work, and say what an
independent reviewer would add — or, if honestly nothing, what you looked for.

## §10 · THE VERDICT

The deliverable is **two lists and a table** — never a score, never an average. **This template is
the shape of your REPLY**; nothing is written to a file.

```
NERS PASS: <target>          INSTRUMENTS: A | A+B

MUST BE STATED AS A LIMIT
  - <claim>  — <why it is not carried>  [C1..C5 / §3 / §6]
MAY BE CLAIMED, HAVING SURVIVED
  - <claim>  — <the attack run against it, and why it failed>

| axis / test | verdict | what would overturn it |
|---|---|---|
| N (six directions)  | PASS / FINDINGS | <a specific object, named, and the direction> |
| E-OVERHEAD          | PASS / FINDINGS | evidence a cut object's loss does NOT survive — an amputation scored as elegance |
| E-LEGIBILITY        | PASS / FINDINGS | an outcome the player cannot intuit from the choice |
| R-COMPLETE          | PASS / FINDINGS | an unwritten branch, or a claim with no carrier |
| R-VARIETY           | PASS / FINDINGS | a single build or a single line of play that answers everything |
| R-WORLD             | PASS / FINDINGS | a seat that resolves identically and emits nothing |
| R-CHOICE            | PASS / FINDINGS / NOT SCORABLE | <the dominant act and the seat it dominates at; or the seat question, or the prior ruling it waits on> |
| S-UP                | PASS / FAIL / N-A | a demand that cannot be carried by a person. `N-A` where the target has no ladder at its scale |
| S-DOWN              | PASS / FAIL / N-A | <the named test, and its result> |
| S — coverage · pause · methodology | PASS / FINDINGS | <an uncarried direction; a system that ticks through a yielded scale; a second convention for one quantity> |
| the design's own falsifier (§8) | HOLDS / HITS | <the family the hits cluster into, or the missing family> |
| self-audit (§9) | <both sweeps, and what each turned up> | <what an independent reviewer would add> |

REPAIRS (worst first — the one whose absence changes the game most, then the rest;
        each a deletion or one object, never a system)
  <finding> → <fix>

GRADE: paper | runs — <the execution artifact, or its absence>
```

- **`NOT SCORABLE` is a verdict.** An axis blocked on a precondition is reported blocked, with the
  precondition named — not a fail, and not quietly a pass.
- **The grade is the one row you cannot fill in by writing** (CLAUDE.md §0.2). **Run something and
  paste what it said:** `python tools/m1_acceptance.py --summary` for a milestone juncture,
  `python -m engine.season.harness.register --requirements` for the season loop, otherwise the test
  that exercises the target. A shape with nothing running stays **paper**.
- **This pass produces EDITS, not a document** — CLAUDE.md §0's bound on the adversarial pass binds
  unchanged, including at most one `needs_jordan: true` ledger row, after §0's five answer-it-first
  tests. **A finding that needs no ruling is fixed in this commit or dropped.**

## §11 · GUARDRAILS

- **The pass discipline** (THE THROUGHLINE): a named failed attack licenses a pass, withholding is
  symmetric, a clean verdict stands only on its trail. **Never manufacture a finding, and never
  sham-clear.**
- **Edits, not documents** (§10): no `audit/` directory, no verdict file, no unconditional ledger
  append, no registry logging.
- **A fix that adds a system has failed** (THE META-RULE). Prefer the deletion; never mint a guard
  whose subject is this repository's own process (CLAUDE.md §0.1 pt 5).
- **Never defend prior output** (§9's `[SELF-AUTHORED — bias risk]`).
- **No false universals.** A linear clock is not a cliff; a multi-threshold tracker is not a
  violation; a deliberate absolute effect with a safeguard is not a finding; **a dominant act at a
  seat no player occupies is a portrait — but only while that seat still throws hooks** (R-WORLD,
  Rule 3). Check scope, and on a target that rolls the intent gate (`resolution-diagnostic` Phase 5),
  before flagging.
- **Parameters are Jordan's.** Tuned numbers → `[OPEN — Jordan tuning]`, not a structural defect:
  the *form* is the audit's business, the *values* are not.
- **Ground every claim at `file:line`** (§1); never lift numbers from the frozen prose capture.

## §12 · WORKED EXAMPLE — the move this skill exists to make

*A design promises that burying a matter is now visible and attributable.*

1. **C1/C2.** Three sections advertise it; none has a carrier. The one naming a mechanism names
   `witness`, which takes events — and an omission emits none.
2. **§6**, at the convener's seat, intent *"this matter dies"*:

   | act | gain | cost |
   |---|---|---|
   | refuse publicly | the matter dies | an act → witnessed → a grievance deposits |
   | **say nothing** | the matter dies, **faster** | **no act, no event, no claim** |

   Identical gain, cost decaying to zero: **dominance at a playable seat — R-CHOICE fails (Rule 3).**
3. **The repair — one object, not a system:** a lapse and a supersession **emit a witnessable event
   at the venue**, on the precedent that a date passing is a resolution and resolutions are events.
4. **State the residual.** The event makes burial *visible*, not *costly* — whether a grievance
   deposits depends on who learns. **"Attributable"** may be claimed; **"punished"** is a limit.
