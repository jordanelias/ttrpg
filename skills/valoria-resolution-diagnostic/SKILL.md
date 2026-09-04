---
name: valoria-resolution-diagnostic
description: >
  THE NERS PASS — the repo's cut test on any design object, mechanism or suite, plus the
  rolling-engine stress diagnostic that feeds it. NERS is not four scores. It is ONE operation
  applied four times: propose the cut, and name what dies. N — remove it and the gameplay
  experience is worse, checked from all six directions (top-down, bottom-up, vertical, diagonal,
  lateral, horizontal). E — remove MORE; logically simple, no unnecessary overhead, and the player
  can intuit complex outcomes from simple choices; scored as a RATIO against N and R, never as an
  independent axis, because scored alone it is satisfiable by amputation. R — remove the
  alternatives; strategy, customization, variety, felt impact, emergent hooks WITHOUT player
  involvement, and mechanics fully formed and error-free. S — remove the rung or the seam;
  friction-free integration, clean scale zoom, correct pausing, and calculations consistent in
  methodology. The pass is graded on the cuts that turn out to be FREE — an object whose claimed
  loss survives its own removal (the false N-line), which is the highest-value thing it produces.
  The definitions themselves are canon and live in CLAUDE.md §0.06 — read them there; this skill
  owns the METHOD, not the definitions. Two evidence instruments, one verdict: (1) the object
  ledger, for any design shape; (2) the
  Phase 0-6 resolution diagnostic, run against the ONE engine — the sigma-leverage mu-shift layer
  (engine/autoload/sigma_leverage.py) atop the d10 substrate (engine/autoload/dice_engine.py), with
  FRACTIONAL dice pools and FRACTIONAL obstacles — for anything that resolves by a draw.
  ALWAYS use for: "NERS audit", "NERS pass", "NERS review", "is this NERS compliant", "is this
  necessary", "is this elegant", "is this robust", "false N-line", "does this add a system",
  "is this seat playable", "is one option dominant", "does this propagate across scales",
  "engine audit", "resolution audit", "resolution diagnostic audit", "diagnose this resolver",
  "stress test this roll", "sigma leverage", "mu-shift vs Ob-shift", "leverage non-uniformity",
  "fractional pool", "fractional obstacle", "sub-1D pool", "soft cap saturation". Do NOT use for pure internal-consistency checks with no cut question (formula gaps,
  redundancy) — that is valoria-mechanic-audit; or for contract/seam closure — that is
  valoria-module-adjudicator, which defers behavioural NERS back here.
---

# NERS

## THE THROUGHLINE — one operation, four times

**NERS is a cut test.** Every axis asks the same question of a different thing, and the answer is
always a loss you can name:

| axis | the cut you propose | what must die, or the axis fails |
|---|---|---|
| **N** — NECESSARY | remove the object | **the gameplay experience gets worse** — an emergent possibility, a robust choice, a clean integration. Not a number, not a feature: a thing the game could do and now cannot, **checked from all six directions** |
| **E** — ELEGANT | remove **more** | **nothing.** E is what is left when every free cut has been taken — and it must still be **simple to read and to intuit from**, not merely small |
| **R** — ROBUST | remove the alternatives | **the choice, and the drama.** If one option dominates, the others were already cut and the seat is a corridor. If nothing comes out of a seat unwatched, it is a dead seat |
| **S** — SMOOTH | remove the rung, or the seam | **the propagation.** A demand that can no longer travel up, an opportunity that can no longer travel down, a scale transition that no longer pauses or hands off cleanly |

**The product of the pass is not the passes. It is the cuts that turned out to be free** — objects
whose claimed loss survives their own removal. Everything else in this file exists to make that
finding reachable and to stop the pass from congratulating itself.

**Three properties make the pass honest rather than performative.** They are the parts a session
skips first, so they are stated before the method:

1. **A PASS is licensed by a NAMED FAILED ATTACK, not by the absence of a finding.** State the
   attack you ran, and that it failed and why. *"I attacked X as a violation of Y and it holds,
   because Z"* is a pass. *"I found nothing"* is not. Every verdict additionally names what would
   overturn it (CLAUDE.md §0.1 pt 3). And every finding carries its **residual — stated, not
   hidden**: the qualification that survives the verdict.
2. **Withholding is symmetric.** A precondition that blocks an unfavourable verdict blocks the
   favourable ones too. Banking the good ones and holding the bad one for want of the same
   precondition is **asymmetric skepticism** (CLAUDE.md §0.1 pt 4) — the single most likely way this pass
   goes wrong, because it feels like rigour.
3. **The pass fires on itself, and on the tree as well as the shape.** A NERS pass that produced no
   finding against its own work has not run — §9 is that stage and it is not optional. A shape that
   passes N/E/S on paper while nothing executes is graded **paper** (CLAUDE.md §0.2).

---

## THE CHARTER — where the definitions live

> **The four definitions are canon and they live in `CLAUDE.md` §0.06. READ THEM THERE.**

They are **not** reproduced here, deliberately. They were homeless until 2026-09-04 —
`canon/definitions.yaml` was cited as their source by this skill and by
`valoria-module-adjudicator` and **never existed** (ED-929, filed 2026-06-11) — and the fix for a
homeless definition is one home, not a second copy. A copy here would be a second owner and would
drift, which is the defect this repository keeps filing.

**Division of ownership, so neither file grows into the other:**

| | owns |
|---|---|
| `CLAUDE.md` §0.06 | **the definitions** — what N, E, R and S mean, the six directions, and the three ways the shorthand is narrower than the text |
| **this file** | **the method** — how a pass is run, what it produces, and the discipline that keeps it honest |

Two things from §0.06 are restated below only because the *method* is built on them and would be
unreadable without them: **E is scored as a ratio, never as an independent axis** (Rule 1), and **R's
player half alone is scoped to occupiable seats** (Rule 3). Everything else, read there.

---

## THE FOUR RULES — how to SCORE the charter (CLAUDE.md §0.06) without mis-scoring it

The definitions say what the letters mean. These four say how a pass goes wrong, and each exists
because a pass went wrong that way.

### RULE 1 — E IS SCORED AS A RATIO AGAINST N AND R, NEVER AS AN INDEPENDENT AXIS

E *means* legibility and no unnecessary overhead. But **scored on its own it is satisfiable by
amputation**: cut enough and what remains is simple, clear and cheap. So E is scored **last**, and
always against what N and R found:

> *Distil as far as possible **without losing emergent possibilities or robust choosing for the
> player**.*

**An audit that scores four axes and averages them rates an amputated design as elegant**, and that is
the only reason this rule exists. E has no value until you know what the cuts cost.

### RULE 2 — S IS PROPAGATION IN ALL SIX DIRECTIONS, NOT A STYLISTIC JUDGMENT

"Integrates cleanly" is not a test. Run the directions. **The two sharpest, because they are the two
a design most often only claims:**

- **S-UP:** can a demand travel up the ladder and be **filtered by a named person at a rung**?
- **S-DOWN:** can an opportunity travel down and reach **a person who holds no post**?

The other four (lateral, horizontal, vertical, diagonal) are §7's coverage sweep, and the charter's
own two extras — **pauses correctly**, and **calculations consistent in methodology** — are tests, not
adjectives.

### RULE 3 — R-PLAYER BINDS AT SEATS A PLAYER CAN OCCUPY; R-WORLD BINDS EVERYWHERE

The charter's R has two halves and they scope differently:

- **R-PLAYER** — strategy, customization, variety, feeling important and impactful. This binds **at
  seats a player can occupy**. Everywhere else, a dominant act is a **portrait**, not a defect: a duke
  who always does the same thing is characterisation.
- **R-WORLD** — *"emergent and compelling narrative hooks and scenarios without player involvement."*
  This binds **everywhere, including at seats no player will ever hold.** So the portrait defence has
  a limit: a dominant act at an unplayable seat is a portrait **only while it still throws hooks**. If
  the seat resolves the same way every season and nothing comes out of it, that is not a portrait, it
  is a **dead seat**, and it fails R-WORLD.

Rule 3 makes ***"is this seat playable?"*** a load-bearing question that must be answered **per seat**
before R-PLAYER can be scored at all. §6.1 is where that precondition turns into an evasion if you
let it.

### THE META-RULE — A FIX THAT ADDS A SYSTEM HAS FAILED

The remediation standard is the best repair this corpus has produced: **three edits, two of them
deletions, and the vocabulary got shorter.** A remedy that adds an object, a store, a gauge, a table
or a guard is presumed failed and must argue its way out — under CLAUDE.md §0.1 pt 5 it must
additionally be load-bearing on the game, the exported params, the port, or a Jordan decision.
Apparatus that guards apparatus is refused outright. **This is also E's own test applied to the
repair:** a fix that adds overhead cannot improve E.

---

## §1 · SCOPE — two instruments, one verdict

**The NERS pass applies to any design object, mechanism, act, verb, gauge, edge or suite.** It does
not require a draw. What requires a draw is the *second* instrument.

| instrument | when | what it produces |
|---|---|---|
| **A — the object ledger** (§2–§9) | always | N-lines, false N-lines, the E ratio, the R gain/cost tables, the S traces |
| **B — the resolution diagnostic** (§11, Phases 0–6) | the target resolves an outcome by a **draw** | stress points and property violations, against the **one** engine: σ-leverage μ-shift over the d10 substrate, fractional pool and fractional Ob |

Instrument B is **evidence, not a verdict.** Its Phase 0–6 findings enter the ledger; they do not
short-circuit it. A target with no draw runs instrument A alone — that is a normal NERS pass, not an
out-of-scope one.

**Routes elsewhere.** Internal consistency with no cut question (a formula gap, a dangling
cross-reference, a redundant definition) → `valoria-mechanic-audit`. Contract/seam closure — does
module X emit what module Y consumes → `valoria-module-adjudicator`, which defers behavioural NERS
back here. Corpus vocabulary and isolates → `valoria-vector-audit`.

**Read the target from the working tree, never from memory** (CLAUDE.md §2). The target need not be
canon: a design can be NERS-audited *en route to* canon, which is the only way the bootstrap breaks.
Where canon and code disagree, **the code is the mechanism and the prose is reference** (CLAUDE.md §0.05) —
audit the code, and record the disagreement as a defect in one of them.

**Cite `file:line`.** Every claim about the target names where it lives. A claim with no locus is
`[UNGROUNDED]` and cannot carry a verdict.

---

## §2 · N — THE N-LINE LEDGER

> **No object enters the shape without an N-line.**

An N-line has exactly one form:

```
<object> — cut it and the gameplay experience is worse, because <WHAT THE GAME CAN NO LONGER DO>.
```

The loss may be of any of the other three — an emergent possibility (R), a robust choice (R), a
clean integration (S), or a simplification the object was buying (E) — because **the charter defines
N through them.** What it may never be is a *representation*.

**And it is tested from all six directions.** An object may be necessary looking up the ladder and
free looking down it. Name the direction the loss occurs in: top-down · bottom-up · vertical ·
diagonal · lateral · horizontal. An N-line that holds in exactly one direction is a **narrowed**
N-line (below), not a passing one.

**What is and is not an N-line:**

| not an N-line | why |
|---|---|
| "it stores X" | a store is not a possibility. Name what the world can no longer *do* |
| "the design references it in four places" | reference count is coupling, not necessity |
| "it makes X legible/tunable/explicit" | that is an argument for a *representation*, not for the object |
| "without it, Y has no home" | **the load-bearing false-N pattern.** Check whether Y already has one — §3 |
| "it would be needed if Z were built" | an object with **no producer** cannot have an N-line at all |

**Three verdicts, and the third is the one sessions skip:**

- **N HOLDS** — the possibility dies with the cut, and you ran an attack that failed to save it.
- **N HOLDS, NARROWED** — the possibility partly survives via something else, so the N-line shrank.
  ⚠ **A narrowed N-line MUST BE RESTATED in its narrowed form.** Leaving the original headline
  standing while the ground under it shrank is how a design keeps advertising a benefit it no longer
  delivers — and it is the defect §8's self-audit catches most often.
- **FALSE N-LINE** — the possibility survives the cut. Go to §3.

**The attack to run on every N-line:** *assume the object is gone. Now walk the loss it claims — the
possibility, the choice, the integration — step by step, and at each step name the object that
carries it.* If you reach the end with
every step named by something else, the N-line is false. If you stall at a step with nothing to name,
N holds and **that step is the N-line** — restate it as the narrow thing it actually is.

---

## §3 · THE FALSE N-LINE — the highest-value finding this pass can produce

> **An object whose claimed lost possibility ACTUALLY SURVIVES THE CUT, because something already
> ruled in provides it.**

**The signature is uniform, and recognising it is most of the skill:**

> a mechanism was named · a **store** was proposed for it · and the store's job was **already being
> done by an object the design had ruled in**.

**Five disqualifiers. Any one of them fires a false N-line:**

| # | disqualifier | the question that detects it |
|---|---|---|
| 1 | **the carrier already exists** | is the thing this stores already stored, on an object that can also be *contested, planted or refuted*? Knowledge on the thing known is two owners and no knower |
| 2 | **no producer** | who writes this, by what act? An object nothing produces cannot have an N-line — its possibility was never reachable |
| 3 | **already cut, and the cut applied** | has this been proposed and rejected before? A re-addition must name the prior cut and say what changed. Re-adding a previously-cut object **without mentioning the cut existed** is the failure |
| 4 | **it is a reward for a behaviour the ranking already weights** | if convictions already weight the choice and stance already gates salience, a bonus on top is a second thumb on one scale |
| 5 | **the residue is a flat bonus** | when everything else is stripped, does what remains reduce to "+X"? A flat pool bonus is the shape a design refuses; if that is all that is left, the object was the wrapper |

### §3.1 The two evasions that get an addition out of the dock

Both appear as *arguments*, which is why they work. Refuse both by construction.

- **"It is only a NAMING of what the corpus already does."** ⚠ **Then produce the exact shipped
  instances.** The corpus routinely ships the **halves** of a composition and never the composition
  — a predicate here, a scheduler there — and a name for the unshipped composition is an **addition**
  wearing a uniform. **Zero exact instances = it stands in the dock like anything else, and must win
  on its N-line.** It may well win; it does not get to skip the hearing.
- **"It is free — it costs no code."** Check the **denominator** (§5.1). A thing that must be
  *attached, set, or authored* by someone has a cost even when its implementation is empty.

### §3.2 The null result

A pass that fires no false N-line is a legitimate outcome **only with the trail behind it** — the
N-lines examined, the walk run on each, and at least one attack named and failed. A bare "all N-lines
hold" is incompletion wearing a finding's clothes. Equally: **never manufacture a false N-line to
have produced one.** Report exactly what is there (user preferences, `honest_findings`).

---

## §4 · THE FIVE CROSS-CUTTING CHECKS

These do not wait for a stage. They fire while you read, and in practice they produce most findings.

### C1 — CLAIM → MECHANISM. *Is this claim carried by an object, or is it prose?*
For every behavioural promise the design makes ("neglect becomes attributable", "burial is now
visible", "stalling is punished"), name the object that carries it and the act that emits it. **A
promise with no carrier is unmechanized** — and the failure mode is that several sections advertise
it independently, so cutting one leaves the rest still promising. Sweep them together.

### C2 — TYPE SIGNATURE. *Does the type admit the input the claim requires?*
The sharpest form of C1. If a claim requires `witness` to see an omission, and `witness` takes
**events**, and **an omission emits none**, the claim does not merely lack a mechanism — it
**contradicts the signature**. Read the signature, not the description.

### C3 — EPISTEMIC FEASIBILITY. *Who evaluates this, and from what they can actually know?*
A predicate must be evaluable by a named party from state that party can reach. A predicate phrased
as a world-scale semantic judgment ("the matter is no longer live") in a design whose discipline is
per-person claims is **either a forbidden stored world-condition or an omniscient oracle**. Neither
is shippable. The repair direction is always the same: **evaluate it at a venue, from claims a named
person holds, contestable like any other claim.**

### C4 — CONTRADICTION SWEEP. *Do two sections rule the same fact pattern opposite ways?*
Find the fact pattern, not the wording. If §A forbids deduplication because "that would be an engine
deciding a person's options", and §B expires one item because another resolved the same need, the two
rule one pattern opposite ways. **The contradiction is usually a symptom** — most often a missing
evaluator (C3) showing through. Include contradictions **you introduced**; those are the ones nobody
else will find.

### C5 — PATH CONSTRUCTION. *Trace the emergent path; name a shipped object at every step.*
Take the design's own showcase example and walk it. A path where every step names a shipped object
**constructs**. A path that needs an object which does not exist is **asserted**. Most showcase
examples are **half mechanism, half hope** — and the honest output is to claim the constructing half
and state the other as a limit, or specify the missing object. **Downgrade the verb, too:** if the
path makes something *expressible* rather than *implementable*, take the overclaim off.

---

## §5 · E — TWO TESTS, SCORED AS A RATIO

The charter gives E **two tests**, and a mechanism can pass one and fail the other:

- **E-OVERHEAD** — *logically simple, clear approach, no unnecessary overhead.* Counted.
- **E-LEGIBILITY** — *easy to understand; the player can **intuit complex outcomes from simple
  choices**.* This is about the player's head, not the object count: a design with three objects and
  an unreadable interaction between them fails E even though nothing could be cut.

Then **Rule 1**: score both **against what N and R found**, never in parallel with them.

```
        what survived removal          (N and R, already scored)
  E  =  ─────────────────────
        what the shape costs           (objects, verbs, stores, vocabulary, authoring, overhead)
```

**Count and report, don't characterise:** objects in vs objects out · verbs added vs verbs folded ·
whether the biggest moves are **deletions** · whether the **vocabulary got shorter**. An "elegant"
verdict with no counts is not an E-OVERHEAD verdict.

**And test E-LEGIBILITY separately, because counting cannot reach it.** The question is: *can the
player predict the shape of the outcome from the choice they are making, without simulating the
engine?* Failing looks like a simple choice whose consequence is only knowable by running it, or an
outcome that emerges from opaque interaction between several individually-simple parts.

### §5.1 The denominator is the half that gets understated

**Every "free" mechanism has a denominator somewhere.** Find it by asking where its inputs come from:

- A predicate must be **set by someone**. Either persons set it **by an act** — then what does the
  act cost, and does setting them freely become a denial-of-service on the office that must service
  them? — or the design ships an **authored inventory** of them.
- **If the design boasts of not needing an authored inventory, and its mechanism requires one, the
  boast is false as filed.** Say so in those terms. This is the single highest-yield E finding, and
  it is invisible if you only count objects.
- A new owner of state is a **new owner**. If the compliance table admits four owners and the
  mechanism gives a fifth one durable state, that row is missing and must be added explicitly.

### §5.2 Over-distillation — the ratio cuts both ways

E can fail by cutting too much. Keep an explicit watchlist: for each unification or removal, name
**the N it protects** and give a verdict with confidence.

| watched | the N it protects | verdict |
|---|---|---|
| *(two channels unified onto one type)* | *(the distinct depth each channel had)* | kept, at MEDIUM confidence — the payload split is real and the unification may be one step too far |
| *(a three-state domain collapsed to a boolean)* | *(the third state)* | cut — nothing produced the third state |

**"Kept at MEDIUM confidence" is a real verdict** and belongs in the output. A watchlist of only
`kept — fine` rows means the watch was not run.

---

## §6 · R — FOUR TESTS, ONE INSTRUMENT

The charter's R is the widest axis. Run all four; the fourth has the instrument.

| test | the question | fails when |
|---|---|---|
| **R-COMPLETE** | are the mechanics **fully formed, error-free and complete**? | it breaks at its extremes, has an unwritten branch, or a claimed behaviour has no carrier (§4 C1/C2). **Instrument B's P-i…P-v is this test for anything that rolls** |
| **R-VARIETY** | does it permit **customization** and **creativity/variety in approach and resolution**? | one build, one line of play, or one right answer to every situation |
| **R-WORLD** | does it produce **emergent hooks and scenarios WITHOUT player involvement**? | the seat resolves identically every season and nothing comes out of it — a **dead seat**, and the portrait defence does not cover it (Rule 3) |
| **R-CHOICE** | does the player **think strategically** and **feel they impact the world**? | **one option dominates** — the instrument below |

**R-CHOICE has the concrete instrument, and it is small.** For each **seat a player can occupy**, and
each **intent** available at that seat, tabulate the acts that reach the intent:

```
SEAT: <who>                 INTENT: <what they want>
| act | gain | cost |
```

**Dominance is read off the table, and it has three shapes:**

| shape | what it looks like | verdict |
|---|---|---|
| **strict** | one row's gain ≥ every other row's, and its cost is strictly lower | dominance |
| **decaying cost** | identical gain; one row's cost **depends on someone choosing to report it**, so it decays toward zero | dominance — and the more dangerous shape, because the table reads balanced at a point |
| **shape mismatch** | gain decays over time while cost compounds (or the reverse) | dominance over the horizon, invisible at a single point. **Compare the shapes, not the values** |

> **The recurring instance, worth memorising: SILENCE BEATS REFUSAL.** Refusing publicly is an act →
> witnessed → a grievance deposits. Saying nothing reaches the same end, often faster, and emits **no
> act, no event, no claim**. Generalised: **wherever two options reach one outcome and only one emits
> an event, the silent one dominates**, because events are the only thing costs can attach to. This
> is a **design failure under Rule 3, not a balance note.**
>
> **And the repair is one object, not a system:** make the omission emit. A lapse, a supersession, a
> quiet expiry — each must **emit a witnessable event at the venue**. The precedent is normally
> already there (a date passing is a resolution; resolutions are events), which is why it is one
> sentence rather than a mechanism.

### §6.1 The precondition — and the line where it becomes an evasion

**Rule 3 gates R-CHOICE and R-VARIETY: answer "is this seat playable?" per seat first.** ⚠ **It does
not gate R-COMPLETE or R-WORLD**, which bind everywhere — so a blocked precondition never makes *R*
unscorable, only two of its four tests. Reporting "R: NOT SCORABLE" when R-COMPLETE and R-WORLD were
never attempted is the precondition being used as cover. And an unanswered precondition is not a
licence to stop even on the two it does gate:

- **Where the design's own laws answer it, it is answered.** If the player is an ordinary Person, a
  played-flag is a fidelity setting, player-only mechanisms are refused, and every rung is
  occupiable, then *which seats are playable* is settled by those laws. Do not re-open it.
- **What genuinely remains is narrower and content-shaped** — *which seats a campaign OFFERS AT
  START.* That is a real question for a person; escalate **that**, not the general one.
- ⚠ **And the half that goes wrong most:** having declared R unscorable for want of the precondition,
  **do not then bank the favourable R findings anyway.** That is asymmetric skepticism by name — an
  unfavourable result withheld for want of a precondition the favourable ones are not held to. Either
  the precondition binds all of them or none. Favourable closures made under it are marked
  **PROVISIONAL**.

### §6.2 The two rules that keep an R verdict honest

- **Any "no dominant option" claim is an UPPER BOUND, not an estimate.** You looked and did not find
  one; that is not the same as there not being one. Say *upper bound*.
- **Do not bank R without two-arm artifacts.** A number with no control is not a measurement in
  either direction (CLAUDE.md §0.1 pt 4). For a campaign-level R question the two-arm instrument is
  `tools/balance_oracle.py` — but note it is a **campaign** instrument: for a change that is
  campaign-unreachable both arms are identical by construction, and running it would be a fake
  control.

### §6.3 R verdicts carry their dependency

An R verdict is usually conditional on a rule that has not been ruled — and **the act economy is the
denominator of nearly every one of them.** Under one act per person per season, three petitions cost
three seasons and every option has a true price. Under a multi-act reading, the same option set is
petition-spray and one row dominates. **State the dependency in the verdict** — *"R for X cannot be
ruled until the act economy is"* — rather than scoring around it.

---

## §7 · S — SIX DIRECTIONS, PLUS TWO TESTS THE SHORTHAND DROPS

### §7.1 The two directions a design most often only claims

**S-UP.** Can a demand travel up the ladder and be **filtered by a named person at a rung**? It
passes when the demand is a **real object** carried by a **named person** who **spends an act**,
placed on a **dated docket**, and **droppable by a convener who pays for dropping it**. *Filtering is
a real act by a real person at a rung — never a threshold, never a probability.*

**S-DOWN.** Can an opportunity travel down and reach **a person who holds no post**? It passes when
the opportunity is published as a telling, **distorts in transit**, and reaches the postless person
through **their own** perception set — i.e. **nobody authors an opportunity for anybody**. An
opportunity routed to a recipient by name is authoring, and fails.

### §7.2 The coverage sweep — all six

Run the other four as a coverage table, not as prose. For each, either name the seam that carries it
or record the gap:

| direction | what it means here | carried by |
|---|---|---|
| **top-down** | an aggregate reads or constrains its substrate | |
| **bottom-up** | the substrate recomputes the aggregate | |
| **vertical** | a cross-scale handoff | |
| **diagonal** | cross-scale **and** cross-family | |
| **lateral / horizontal** | same-scale edges between siblings | |

A direction with **no** carrier is an S finding. A direction whose carrier exists but whose targets
are unpopulated **delivers blind** — the consequence is intended and unreached, which is the same
defect one step later.

### §7.3 The charter's two extra tests

- **PAUSES CORRECTLY.** When another system or scale is called for, does this one **stop**, hand off,
  and resume — or does it keep resolving underneath? A mechanism that continues to tick through a
  scale it should have yielded to is an S failure even when every edge is wired.
- **CALCULATIONS CONSISTENT IN METHODOLOGY.** Do sibling mechanics compute the same *kind* of thing
  the same way? Two ladders, two leverage conventions, two ways of banding one quantity — each is an
  S defect regardless of whether either is individually correct. This is the axis on which
  dice-on-a-deterministic-ledger failed.

### §7.4 Attacks worth running on S, both of which can legitimately fail

- *"It is identically zero at the bottom"* — fails if the mechanism **mints its own surface** at the
  bottom rung rather than dividing an existing one.
- *"It stores a world condition"* — fails if the predicate is scoped to the holder's **own state** or
  to a **compute-on-demand aggregate** rather than a stored gauge.

> ⚠ **SCORE THE SHAPE AND THE TREE SEPARATELY, AND SAY BOTH.** A shape can pass S structurally while
> the executing tree scores **zero** on both directions — because the demand object does not exist,
> or because there are no persons at all. Both statements are true simultaneously and reporting only
> the first is the failure. Name the execution step that is the whole difference.

---

## §8 · RUN THE DESIGN'S OWN FALSIFIER

Most designs state a discipline they claim to hold to — *every effect traces to a self-interested
act*, *no engine decides a person's options*, *no authored trigger inventory*. **Run it. Do not cite
it.**

1. **Enumerate the hits** — the places the discipline is broken.
2. **Classify each:** clean hit · borderline · **passes by tracing** (it looks engine-supplied but
   traces back to an act, possibly seasons earlier — say which act).
3. **Cluster the clean hits into families.** Few, scattered hits mean the discipline is real. Few
   hits that are **all one family** mean the discipline is real *and* the design's own list of
   exceptions is incomplete — name the missing family.
4. ⚠ **Scope the repair narrowly.** Licensing the whole family waves through exactly the members that
   are live questions. **License the settled member narrowly; make the live ones trace to persons.**
   "The repair is not a free one-liner" is the honest report when it is not.

---

## §9 · THE SELF-AUDIT — terminal, and not optional

A NERS pass that produced no finding against **its own work** has not run. Two sweeps, in order:

**9a — BACKWARD PROPAGATION.** Your later sections corrected your earlier ones. **Did the corrections
propagate backward?** The characteristic residue:
- an early summary table still printing the figure a later section corrected;
- an early section claiming a benefit a later narrowing downgraded (*restored* → *reachable*;
  *implementable* → *expressible*) — see §2's restatement rule;
- a claim derived for a form you subsequently withdrew, never re-derived for the form you kept;
- a count ("four shipped instances") a later section reduced to zero.

**A self-retraction in one section is the pass at its best. The same operation not run on the other
sections is the pass at its most misleading**, because the retraction buys credibility the rest of
the document has not earned.

**9b — THE SEVENTH FALSE N-LINE.** Turn §3 on the pass itself, and on any object **this** work added.
The uncomfortable row is the one to record: an object re-added here that the source had already cut,
twice, independently, with the cut applied. If §3's five disqualifiers fire on your own addition,
**delete it in this commit.**

Prepend `[SELF-AUTHORED — bias risk]` whenever auditing work from this or a prior session, and
surface at least one limitation an independent reviewer would add.

---

## §10 · THE VERDICT

The deliverable is **two lists and a table** — never a score, never an average.

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
| R-CHOICE            | PASS / NOT SCORABLE | <the seat question, or the prior ruling it waits on> |
| S-UP                | PASS / FAIL | a demand that cannot be carried by a person |
| S-DOWN              | PASS / FAIL | <the named test, and its result> |
| S — coverage · pause · methodology | PASS / FINDINGS | <an uncarried direction; a system that ticks through a yielded scale; a second convention for one quantity> |

REPAIRS (worst first, each a deletion or one object — never a system)
  <severity> <finding> → <fix>

GRADE: paper | runs — <the execution artifact, or its absence>
```

**Three rules on the output:**

- **`NOT SCORABLE` is a verdict.** An axis blocked on a precondition is reported blocked, with the
  precondition named. It is not a fail, and it is not quietly a pass.
- **The grade is subordinate to everything above it.** N, E and S can all pass as *arguments about a
  text*. Under CLAUDE.md §0.2 a juncture is done when the behaviour **executes**; a shape with nothing running
  is graded **paper**, and it stays paper until something runs. Say which execution step is the whole
  difference.
- **This pass produces EDITS, not a document.** Per CLAUDE.md §0 the adversarial pass is a **stage,
  not a deliverable**: its output is edits to the thing under review plus **at most one paragraph in
  the commit message**. It creates no directory and no audit file. It may append **at most one ledger
  row, and only if that row needs a human decision** (`needs_jordan: true`) — and only after the row
  has failed all five of CLAUDE.md §0's tests (superseded · irrelevant · answered by a design document ·
  answered by precedent · answered by what the architecture obviously wants). **A finding that needs
  no ruling is fixed in this commit or dropped.**

---

## §11 · INSTRUMENT B — THE RESOLUTION DIAGNOSTIC (the σ-leverage engine)

Run this when the target resolves by a draw. Its output is evidence for §2–§9, not a verdict.

> **THERE IS ONE ENGINE.** *"d10 everywhere, fractional, σ-leveraged"* — Jordan, 2026-08-14, cited at
> `systems/factions/sim/faction_action.py:126`. The **deterministic-odds / stochastic-resolution**
> resolver that this file used to carry as a co-equal "Instance B" **has no implementation anywhere in
> `engine/` or `systems/`** — its constants (`BASE`, `SLOPE`, `OVW_OFFSET`, `PARTIAL_BAND`,
> `FAIL_FLOOR`) appear in no live module, its spec is at the fork, and the faction layer it was
> written for now resolves through σ-leverage on a fractional pool. Under CLAUDE.md §0.05 the code is
> the mechanism, so it is **dead canon** and is not an engine to diagnose against.

### §11.1 The stack, and its live owners

Two layers, deliberately separated (D0-2) — diagnose them separately:

| layer | owner | what it does |
|---|---|---|
| **substrate** | `engine/autoload/dice_engine.py` | pool and degree primitive. `roll_pool` (discrete), `continuous_engine_sample` (fractional), `degree_from_net` (**the** ladder, single owner for every scale) |
| **advantage** | `engine/autoload/sigma_leverage.py` — `[CANONICAL — Stage 1a port 2026-06-30]` | turns signed advantages in σ-units into a **μ-shift** on the roll. Stdlib only. Single-sources σ-leverage for **combat and social contest both** |
| pinned by | `engine/tests/test_sigma_leverage_parity.py` + `engine/tests/goldens/sigma_leverage_parity.json` | the execution artifact. Read it before claiming behaviour |

**The API you are auditing against** — read it, do not restate it from memory:
`sigma_n(pool)` = `0.8·√max(1,pool)` · `soft_cap(σ)` = `M_MAX·tanh(σ/M_MAX)`, `M_MAX = 1.5` ·
`levels_to_net_sigma(agg, def)` · `net_boost(σ, pool)` · `p_success(base_ob, pool, net_sigma)` ·
`roll_net_continuous(pool)`.

### §11.2 ⚠ ADVANTAGE IS A μ-SHIFT. IT IS NOT AN Ob REDUCTION.

This is the single most-drifted fact about this engine, and the previous revision of this file taught
the retracted form.

```
net_boost(σ, N) = soft_cap(σ) · σ_per_die · √N        # boosts the ROLL
p_success       = 1 − Φ( (base_Ob − (μ·N + net_boost)) / (σ_per_die·√N) )
```

**`base_Ob` and TN are never modified.** The earlier `Eff_Ob = base_Ob − eff_σ·σ_N` form drove
effective Ob below 1, violating **P-232** (*Ob minimum 1*) and making the old `2·Ob` Overwhelming bar
nonsensical at negative Ob. That was **F1, resolved by ED-884** with this reformulation.

**Two consequences that change what you look for:**

- **The `Ob ≥ 1` floor is unreachable by advantage, by construction.** "An Ob-shift collides with the
  P-232 floor" is no longer a live hazard on this engine — do not go looking for it, and treat a
  document that describes advantage as an Ob reduction as **stale**, not as a second design.
- **`eff_ob()` / `effective_ob()` are DISPLAY ONLY** and say so in their own docstrings. A caller that
  resolves on `eff_ob` instead of `p_success` has reintroduced the retracted form — **that** is the
  finding to look for.

**Uniform impact is exact, not approximate, and it is worth verifying rather than assuming.**
`σ_per_die·√N` cancels in the z-score, so `Δz = soft_cap(net_σ)` at *every* pool size and every TN.
Measured this session across pool ∈ {0.5, 1, 4, 9, 16, 25} at `net_σ = 1.0`: **Δz = 0.874174 at all
six**, equal to `soft_cap(1.0)` to six decimals. P-ii holds **by construction here**, so a
P-ii finding on this engine means a caller bypassed `net_boost`, not that the engine drifted.

**The bypass to hunt for:** a flat `+X` to net or `−X` to Ob that is *not* σ_N-scaled gives
`Δz = X/(0.8·√pool) ∝ 1/√pool` — hot at small pools, the exact non-uniformity this engine exists to
kill, re-imported through a bonus. Advantage enters through `levels_to_net_sigma` → `net_boost`, or
it is a defect.

### §11.3 Fractional pools and fractional obstacles

Both are canonical, and they are at different stages of reality. **Say which you are looking at.**

**Fractional POOL — live.** `continuous_engine_sample(pool: float)` and
`roll_net_continuous(pool: float)` take floats; `faction_action.py` already passes 4.3, 4.6, 4.9, 5.3.
`roll_pool` is the **discrete** path and keeps `int(round(pool))`, correctly — it deals actual dice
rather than sampling their limit distribution. A fractional pool routed to `roll_pool` is a finding.

**Fractional Ob — RULED, and the derivation is IMPLEMENTED NOWHERE.** Jordan ruled 2026-08-14 that an
obstacle rolled against a character or faction is *"their corresponding score/2 plus whatever specific
modifiers exist for them in that instance."* **Every call site in the tree still passes a hand-set
Ob.** `degree_from_net`'s own docstring flags this, and the distinction matters more here than
anywhere, because this is the function a reader consults to learn what an obstacle *is*. Treat "Ob is
derived" as **a ruling awaiting execution**, never as an accomplished fact.

What *is* live and verified this session:

| claim | verified |
|---|---|
| fractional Ob is **strictly monotonic** — no integer collapse | ✅ pool 9: Ob 1.4 → 0.8203, Ob 1.6 → 0.7977. `Ob 1.4 ≢ 1.6` |
| the degree ladder bands a fractional Ob correctly | ✅ net 1.9 / Ob 1.4 → margin +0.50 → **Partial** |
| the **whole-success-wide Partial window** (`0 ≤ margin < 1`) is what keeps Partial reachable | ✅ on point-equality (`margin == 0`) Partial would essentially never fire against a fractional Ob |

### §11.4 The pool floor is 1D, and it applies to the MEAN as well as the VARIANCE

**RULED 2026-09-04 (Jordan): "1D is floor."** `params/core.md §Pool Floor (all systems)`.

This is worth stating in a diagnostic because the engine got it wrong in a way that only fractional
pools could expose. `p_success` floored the **spread** and not the **location**:

```
was:   shifted_mean = mu * pool                        # NOT floored
       z = (ob - mean) / (sigma * sqrt(max(1, pool)))  # floored
now:   effective_pool = max(1.0, float(pool))          # floor once, use everywhere
```

while `roll_net_continuous` — the sampler the game actually draws from — floored both. **Two
flooring conventions in one module**, disagreeing by up to ~10 pp below 1D:

| pool | before: `p_success` vs sampled | after |
|---|---|---|
| 0.25 | 0.1303 vs 0.2275 — **9.7 pp** | 0.2266 vs 0.2275 — noise |
| 0.50 | 0.1587 vs 0.2275 — **6.9 pp** | 0.2266 vs 0.2275 — noise |
| 1.00 | 0.2266 vs 0.2275 — noise | unchanged |

**Fixed** in `engine/autoload/sigma_leverage.py::p_success` and, byte-identically, in the
`m1_dice_sigma_core` seed the parity goldens are generated from. **The control:** no golden row
carries a sub-1D pool (`p_success` pools are 1/5/10/26) and `max(1.0, pool) == pool` for all of
them, so the change is **value-identical at and above 1D** — 901 parity assertions pass against
**byte-unchanged** goldens.

**What this leaves for a diagnostic to check, which is the reusable part:**

- **A floor applied to one moment of a distribution and not the other is a defect that hides above
  the floor.** Every pool ≥ 1 agreed to noise, so no test, golden or campaign could see it; it was
  reachable only by evaluating below the floor. When you meet a clamp, ask **which terms it reaches**
  — not whether it exists.
- **`dice_engine.continuous_engine_sample` is the raw primitive and does NOT floor**, deliberately:
  it is the mathematical sampler, and the floor is a game rule its callers apply
  (`roll_net_continuous`, `p_success`, and `tools/balance_oracle.py` all do). That is fine while
  every caller floors — **a new caller reaching the primitive directly bypasses the floor**, and
  that is the thing to check at Phase 0, not a defect in the primitive.
- **`roll_pool` is the discrete path and keeps `int(round(pool))`.** Whole dice are correct there; it
  deals actual dice rather than sampling their limit distribution. A fractional pool sent to
  `roll_pool` is a P-v finding.

### §11.5 The five properties, on this engine

| # | property | what failing looks like HERE |
|---|---|---|
| **P-i** | **Legible odds** | the player cannot read their chance; advantage surfaced only as an opaque roll modifier rather than a named level (minor/moderate/strong/major) |
| **P-ii** | **Uniform leverage** | exact by construction — so a failure means a **caller bypassed `net_boost`** with a flat bonus (§11.2), not engine drift |
| **P-iii** | **Bounded, monotonic** | resolving on `eff_ob` (display) instead of `p_success`; a discrete boundary jumping a continuous input; a clamp that reaches one moment of the distribution and not the other (§11.4) |
| **P-iv** | **Graded, recoverable** | a bare binary on an irreversible outcome where `degree_from_net` was available; a Partial band collapsed to point-equality against a fractional Ob |
| **P-v** | **Right engine** | anything resolving by a bespoke draw instead of this stack; a fractional pool sent to `roll_pool`; a second degree ladder |

### §11.6 Phases

| phase | do |
|---|---|
| **0** | Draw present? Decompose. Every rolled component routes to `dice_engine` + `sigma_leverage`; anything else is a P-v finding. Flag bare-pool-vs-flat-Ob leftovers |
| **1** | Locate the stress point — the **low-pool end** (and the floor itself, §11.4), the **soft-cap saturation** region (`net_σ` well past `M_MAX = 1.5`), and any fractional-Ob call site. **1b:** how often is it reached? A fractional pool is routine; a sub-1D pool is not — yet |
| **2** | What does it decide? Outcome type · stakes & reversibility · (impact, exposure, irreversibility) each H/M/L against numbers. Two H = candidate finding |
| **3** | **3a** advantage enters via `levels_to_net_sigma`→`net_boost`, not a flat bonus · **3b** nothing resolves on `eff_ob` · **3c** the fractional-pool and fractional-Ob paths agree with the closed form · **3d** role conflation on a variable feeding or reading the roll |
| **4** | Loops running through the engine's output or gating its input, cross-scale included. Defect = **both undamped and unbounded** — damper and cap are two separate checks |
| **5** | **Intent gate.** Deliberate + adequate safeguard → pass. Deliberate without → finding. Accidental or undetermined → finding, `[INTENT UNDETERMINED]`. Do not guess |
| **6** | Score and triage, worst first. Carry findings into §2–§9 |

### §11.7 What is NOT a defect on this engine

- **The level values** (minor 0.25 / moderate 0.50 / strong 0.75 / major 1.00) are **Class B draft
  sim-seeds, explicitly NOT canonical** and sim-tunable. A level number you disagree with is
  `[OPEN — Jordan tuning]`, not a structural finding. Same for `M_MAX = 1.5`.
- **Soft-cap saturation is the design**, not a cliff: `M·tanh(net/M)` has no hard ceiling and no
  dead-zone. Check it is smooth, not that it is absent.
- **TN never varies.** `PER_DIE` is a one-key dict so a stray TN raises `KeyError` **loudly** rather
  than silently resolving as TN 6 or 8. A mechanism that wants a varying difficulty wants an **Ob**.
  (ED-IN-0196: *"TN7 always. Never change TN anywhere ever."*)
- **`systems/combat/combat_engine_v1/core.py`'s second, `2·Ob`-keyed ladder** is a **declared HELD**
  exception guarded by `tests/valoria/test_degree_ladder_single_owner.py`. Known, tracked, **not yours
  to re-file** — though it is a live instance of the charter's *calculations consistent in
  methodology* (S) defect, and worth naming as such rather than as news.

## §12 · GUARDRAILS

- **The pass produces edits, not documents.** No `audit/` directory, no verdict file, no unconditional
  ledger append, no registry logging. (`tools/audit_registry.py` no longer exists; the mandatory-append
  block that invoked it is deleted, not made conditional.)
- **A fix that adds a system has failed.** Prefer the deletion. A guard is minted only where the
  defective artifact is load-bearing on the game, the exported params, the port, or a Jordan decision
  (CLAUDE.md §0.1 pt 5) — never on this repository's own process.
- **Never defend prior output.** `[SELF-AUTHORED — bias risk]` on any self- or prior-session work.
- **No false universals.** A linear clock is not a cliff; a multi-threshold tracker is not a
  violation; a deliberate absolute effect with a safeguard is not a finding; **a dominant act at a
  seat no player occupies is a portrait — but only while that seat still throws hooks** (R-WORLD,
  Rule 3). Check scope and the intent gate before flagging.
- **Parameters are Jordan's.** Tuned numbers → `[OPEN — Jordan tuning]`, not a structural defect. The
  *form* is the audit's business; the *values* are not.
- **Ground every claim at `file:line`,** read from the working tree. No memory, no `[UNGROUNDED]`
  assertions, no lifting numbers from the frozen prose capture.
- **Never manufacture a finding, and never sham-clear.** A short honest null with its trail beats a
  padded list; a clean verdict with no trail is incompletion wearing a finding's clothes.

---

## §13 · WORKED EXAMPLE — the move this skill exists to make

*A design promises that burying a matter is now visible and attributable.*

1. **C1 · claim → mechanism.** Three sections advertise it independently ("must convene or visibly
   refuse" · "stalling and calendar-packing, previously invisible" · "neglect becomes attributable").
   Look for the carrier. **There is none** — all three are prose.
2. **C2 · type signature.** The third names the mechanism that would see it: `witness`. **`witness`
   takes events, and an omission emits none.** The claim does not merely lack a carrier; it
   contradicts the signature.
3. **§6 · the gain/cost table.** At the convener's seat, intent *"this matter dies"*:

   | act | gain | cost |
   |---|---|---|
   | refuse publicly | the matter dies | an act → witnessed → a grievance deposits |
   | **say nothing** | the matter dies, **faster** | **no act, no event, no claim** |

   Identical gain; cost decaying to zero because it depends on someone choosing to tell. **Dominance
   at a playable seat: R-CHOICE fails under Rule 3 — a design failure, not a balance note.** (Had the
   seat been unplayable, the same table would be a portrait — and would then have to answer R-WORLD
   instead: does anything come out of the burial?)
4. **The repair, under the meta-rule: one object, not a system.** A lapse and a supersession **emit a
   witnessable event at the venue.** The precedent already exists — a date passing is a resolution,
   and resolutions are events — so this is one sentence, not a mechanism. **No new system; the three
   prose promises become carried.**
5. **The residual, stated rather than hidden.** Emitting the event makes burial *visible*; it does not
   make it *costly*. Whether the grievance deposits still depends on who learns — so the claim that
   may be made is **"attributable"**, and **"punished"** must be stated as a limit.

Steps 1–3 are the pass. Step 4 is what distinguishes a NERS repair from a redesign. Step 5 is what
distinguishes a finding from an advertisement.
