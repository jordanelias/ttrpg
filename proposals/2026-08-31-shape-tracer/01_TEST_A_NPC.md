# TEST a:NPC — a season loop for every named NPC, from a copyist to a King

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**
## This test RAN. `TRACE.txt` is the sequence; `results_npc.json` is the data; `tracer/` is the
## instrument, and `tracer/test_tracer_is_honest.py` is the instrument's own adversarial test.

> **THE TEST.** Take PR #350's idealized code shape, implement it faithfully enough to execute,
> and run a season for every named NPC in `references/npc_registry.yaml` across the full spectrum
> of agency — a copyist who holds nothing, a hedge-school teacher, a surveyor, a covert operative,
> a broker, an inquisitor, a spymaster, a governor, a clerk, cardinals, dukes, a grandmaster,
> a queen, an heir, and the King. Log every gap, conflict and error, and log the sequence.

---

## §1 · THE RESULT

| | |
|---|---|
| cases | **27 named NPCs**, specs written by three lanes **blind to the shape** |
| verdict | **22 BLOCKED · 4 NOT-ASSESSED · 1 DEGRADED · 0 PLAYABLE** |
| probes | 65 executed attempts against the shape — **19 PASS, 1 PARTIAL, 45 gaps** |
| trace | 80 acts, 117 events, 337 class-checked writes |
| gap kinds | 29 NO-PRODUCER · 11 UNSPECIFIED · 4 FORBIDDEN · 3 COLLISION |

**A case is BLOCKED when a need its own lane graded `core` maps to a probe that could not
execute.** Not one of twenty-seven named characters has a season that runs end to end.

⚠ **THE PROBE VERDICTS ARE THE HARD RESULT. THE CASE VERDICTS ARE ADVISORY.** Needs are routed onto
probes by keyword, and keyword routing is crude: it mis-fired six times (§5), two of them caught only by audits and
is certainly still mis-firing in ways I did not. **`NOT-ASSESSED` is the instrument admitting it
did not aim** — a case more than half of whose `core` needs failed to route is reported as untested
rather than graded, because grading it PLAYABLE would be the instrument flattering the shape by
failing to point at it. Read a case verdict as *"this character's season met a wall"*, never as an
exact count.

## §2 · WHAT SUCCEEDED — and one of these is excellent

Nineteen probes pass, and they are not trivial passes; each is an execution.

**The three that matter most:**

- **`P12` — obstruction needs no verb.** *Verified by execution, not asserted.* A stranger takes the
  seat Maret Uln needed; her ambition progress moves `1.0 → 0.0`. There is **no `obstruct` verb, no
  knowledge of Maret anywhere in the stranger's decision, and no branch in the resolver.**
  Derived-at-read does the whole job. **This is the best property in the shape and the test confirms
  it.**
- **`P1` — a person holding no office acts.** Carin Vedel, who has no post, no command and no
  faction rank, produces an Act that reaches RESOLVE and emits an Event. The shape's central
  democratic claim holds at the entry point.
- **`P9`/`P20` — an order is the subordinate's own choice.** `dispatch` names one person, that
  person runs their **own** `choose`, and they may refuse or do something adjacent instead. The
  King's reach really is other people's decisions, mechanically and not by description.

**Also passing:** a faction as an uttered `OUGHT` plus its commit edges (`F1`); a claim pressed
across seasons (`F4`); conferral and revocation as acts with a per-office basis (`F5`); a site
decaying until a verb leaves its set (`W1`); the world churning with nobody in it (`W3`); an
institution acting only through a named person at a venue (`A7`); a false conclusion that its holder
cannot distinguish from a true one (`P5`); legitimacy flipping per-knower at telling speed (`A6`);
the substrate as a `Site` kind (`A3`); a subordinate silently underperforming, discoverable only by
investigation (`P25`).

---

## §3 · WHAT FAILED — ranked by how many characters it stops

| probe | core-blocks | what breaks |
|---|---|---|
| **P36** | **5** | `choose` returns **one** Act and the loop calls it **once per person per season**. There is no action budget, so nobody triages and a King's scarcity equals a copyist's |
| **A4** | **4** | `resolve()` emits Events with an **empty `causes[]`**. Nothing in the specified loop populates the causal edge that `06` §1 calls *"the arc itself"* |
| **P29** | **3** | A `Record` is homed as **Rung matter** — it sits at a *place*, never in a person's hands. *"She was found with it"* is not expressible |
| **A2** | **3** | A threshold firing with nobody deciding is **FORBIDDEN** — correctly, and it costs |
| **F6** | **3** | A sitting convenes; `judging_set_rule` is a named Rung field that **no document specifies**, so nothing is decided there |
| **P4** · **P18** · **P26** · **P28** · **P30** | 2 each | conviction motion · staged institutional judgement · accumulated harm crossing a limit · making a durable thing · work spanning seasons |
| **P31** · **P33** · **P3** · **P19** · **P21** · **P16** | 1 each | worn by where you stand · two standings at once · covert action · restraint that emits · the cost of being watched · feeding yourself |

### 3.1 The four that recur across the whole spectrum

**(a) `causes[]` is never written.** The suite rests its narrative layer, audit trail and arc model
on the provenance chain. The loop as specified emits Events with `causes=[]`. **The substrate of the
entire emergent-narrative claim is declared and never populated.** This blocks Joren Bergvall's
evidence changing anyone's mind, and three other cases besides.

**(b) Nobody can hold anything.** `03` §1.3 rules a `Record` to be Rung matter. So a copy, a
register, a charter and a forged deed all sit *at a settlement*, and no person possesses one.
This kills Carin Vedel's entire vocation — *possession is a heresy charge* — and it is **the same
hole `P10` found from the custody side**. `01` §3.1 names **custody** as one of four things that
make an ordinary person matter, and no field carries it. **P10 and P29 are one gap, not two.**

**(c) A conviction cannot move.** `02` §5.5 says convictions move *"slowly, by scar and crisis"*;
nothing specifies a scar or a crisis, and **no formula anywhere consumes a conviction**. The suite's
own `ADVERSARIAL.md` says so — the scar has *"no object, no owner, no N-line"*, and
`convictions`/`beliefs`/`Duty` have *"no rows in the write matrix at all"*. Himlensendt's crisis of
faith and Sæmund's unrecognised perception both stop here.

**(d) Nothing accumulates that does not also decay.** Edeyja's patience (`P26`), Sigrid's covert
risk (`W2` routing), Baralta's pressed claim (`A11` passes but reports `OK-BUT`), the army's staged
reassessment (`P18`) — every one needs a quantity that **only goes up**. The shape offers exactly
one accumulator, the claim ledger, and it **decays by universal rule and evicts at a cap**. So
accumulation is a race against forgetting, and the ratchet the cases need is precisely the stored
state Law 3 forbids.

### 3.2 The King is blocked, and on what — **corrected after an independent audit**

⚠ **This section originally named `P18`, `P19` and `P21` as Almud's three failures. At the time it
was written the instrument supported only `P18`.** A read-only comparative audit that had never seen
my reasoning checked the claim against `results.json` and found that Almud's doubt need had routed
to `A17` and come back **PASS**, and his publicness need was **UNMAPPED** — *"report prose overriding
its own instrument, in the direction §1 of the same report warns against."* **It was right.** The
cause was a fourth greedy-keyword defect: `A17` is *winning versus enforcing are two events*, and
the bare word **`enforce`** in *"a policy he enforces"* matched it, manufacturing a PASS on a probe
about implementation failure. Four other needs were caught the same way.

**With the route fixed, the corrected picture is worse than the claim it replaces, not better.**
Almud's lane graded five needs `core`. **Four fail; one passes.**

| his need | probe | verdict |
|---|---|---|
| facing several ongoing pressures and **only being able to address a subset**, the rest compounding | **`P36`** | NO-PRODUCER |
| a long-held private doubt persisting for seasons, **that persistence itself a choice** | **`P19`** | NO-PRODUCER |
| a standing army **gradually reassessing** its loyalty in stages that do not revert | **`P18`** | NO-PRODUCER |
| being **unable to act on private knowledge without a cost a lower-status person would not pay** | **`P21`** | NO-PRODUCER |
| acts taken in his name **diverging** from what he intended | `P20` | **PASS** |

**`P36` is new, and it is now the single largest blocker on the NPC side (5 cases).** It is the
action budget: `choose(Person, View, Sensation) -> Act` returns **one** Act, and the loop calls it
**once per person per season** — asserted by execution in `test_tracer_is_honest.py`. So nobody
triages, nothing is left undone, and **a King's scarcity is identical to a copyist's.** Against
Jordan's stated player model — *~5 playable scenes per season, which may mean ~5 actions* — the shape
is out by a factor of five, and the gap is not the count. **It is that triage is the whole game at
high office and the shape has no object for it.** Note what a budget above one also voids: `14`
records the petition-spray defect as *"closed — PROVISIONALLY by one act per person"*, a fix that
does not survive the stated model.

**What passes for him is still the delegation half** (`P20`, and `P9`/`P24` at the probe level).
**What fails is the interior half and the scarcity half** — doubt, publicness, triage, and an
institution's slow judgement of him.

### 3.3 ⚠ RETRACTED — the declared seam is CLOSED, and this probe was measuring my own bug

**This section previously reported that a dead king still holds the crown.** It said `A12` kills a
person, tries to end their tenures, finds `(Tenure, hold)` is `social: true` so an Event may not
write it, and concluded *"the Partition as keyed blocks the mechanism churn row 3 exists to
provide."* It cited `05` §7's residual caveat.

**It is wrong, and the error was mine.** `02` §5.1 rules the seam closed, in terms:

> **"RULED: `(Tenure, until)` is `social: false`.** Otherwise death cannot end a tenure and the
> entire succession mechanism has no producer." … **"This is a RULE, not a column, and it is the
> Partition's one declared seam."**

Death writes **`until`**, not `hold`. `04`:167 calls it *"the only Tenure write in the MATTER
class"*, and the `04` §4 matrix carries the row. **My tracer's Partition table simply omitted
`(Tenure, until)`**, and the probe wrote the wrong key — so a closed seam reported as open.

**And the suite's answer is better than the one I was about to propose.** What stops a storm
vacating a praefecture is not the column; it is a causation rule — *an actorless row may write
`until` only on a `(Person, exists)` change the same row also caused.* A plague that kills the
praefect ends his tenure through the death; a storm cannot touch it. That is keyed on causation
within the row rather than on the instance, which is what keeps it from being the "death may,
storms may not" special case the suite's own falsifier forbids.

`A12` now implements the ruled row and the causation rule, tests both directions, and **passes**.

> ⚠ **THIS IS INSTRUMENT DEFECT FIVE AND IT IS THE FIRST TO POINT THE DAMNING WAY.** The other
> four flattered the shape. This one made a closed seam look open, and it slipped through *because
> the guard I had written was asymmetric* — `test_rows_the_suite_lacks_stay_absent` catches an
> **invented** row and nothing caught an **omitted** one. A guard against the failure you already
> made does not catch the failure you have not. There is now a `RULED_ROWS` table asserting the
> rows the suite has explicitly ruled are present **and correct**, which is the symmetric half.

## §4 · LESSONS

1. **The shape is strong at the moment of action and weak at everything around it.** A person
   decides, acts, and is witnessed — that path is clean, and `P12` shows it producing real emergence.
   What is missing is the *connective tissue of a life*: making a thing, holding a thing, working at
   something for longer than a season, being worn down by where you stand, being changed by what
   happened to you.
2. **Refusing stored state has a bill, and the cases present it.** Law 3 is right about aggregates
   and wrong-by-omission about **ratchets**. Five separate characters need a quantity that only
   climbs. The shape has no such object and forbids the obvious one.
3. **The low-agency end is not the hard end — the *interior* end is.** I expected the copyist to be
   the stress case and the King to be comfortable. Both are blocked, and Almud's blockers are all
   about *what is inside him and what others slowly conclude about him*, not about power.
4. **"A person with no office can act" is necessary and nowhere near sufficient.** The shape wins
   its own stated test (`P1`) and still cannot run Carin Vedel's season, because acting once is not
   having a life.
5. **The scarcity is missing, and it was invisible until the King.** One act per person per season
   means the only thing anyone ever chooses is *what to do*, never *what to leave undone*. Triage —
   which pressure gets this season and which one compounds — is most of what it is to hold high
   office, and it costs the shape one field to have. **This is the finding that a reader of the
   documents could not reach**, because every document is written about the act that happens.
6. **The report was wrong about the King and an audit that never saw my reasoning caught it.** §3.2
   claimed three blockers the instrument had produced one of. The relay works: structural
   independence — a critic with no write tools and no access to the producer's thinking — found in
   one pass a defect that four self-review passes had missed.

---

## §5 · ISSUES IN THE INSTRUMENT — found, fixed, and regression-tested

Every one of these **flattered the shape**, which is the dangerous direction. They are recorded
because the tracer gates every finding above.

| defect | effect | fix |
|---|---|---|
| `W2` counted only `resolve()`'s return | band events are emitted at **MATTER** and are not in it, so a site strobing **6 times in 6 seasons** reported clean | count from the log; test asserts it |
| the Partition table carried rows for `Person.capability`/`convictions`/`beliefs` | **rows the suite does not have** (`ADVERSARIAL.md` 14/15/16), turning a real gap into a PASS | rows removed; a test asserts they stay absent |
| greedy keyword routing | *"degrade his **personal** condition"* → site decay; *"maintenance labor"* → substrate. **Two BLOCKED cases became false PLAYABLE** | specific person-scale patterns now precede generic world ones |
| the loader dropped truncated lane output | a whole arc lane's cases lost | repair to whole entries, discarding partial edges without inventing content |
| the bare words **"threshold"** and **"condition"** routed to `W2` (band strobing) and `W1` (site decay) | **16 and 5 core needs** attributed to the wrong mechanism, and several cases graded PLAYABLE off a harbour probe. Found only when the corpus grew from 47 to 78 cases | both regexes narrowed to their real subjects; **two probes added** (`P34`, `P35`) for what the mis-routed needs were actually asking; four router self-tests |
| a case whose `core` needs mostly failed to route was graded **PLAYABLE** | the instrument flattering the shape **by failing to aim at it** — the same direction as the other four | fourth verdict `NOT-ASSESSED`; a self-test asserts the three-way grading cannot come back |
| the bare word **`enforce`** routed to `A17` | *"a policy he **enforces**"* came back **PASS**, so this report claimed the King was blocked on a probe his own case had passed. **Five needs.** Found by an audit, not by me | `A17` narrowed to require the *separation* structure; four router self-tests |
| **`(Tenure, until)` was MISSING from the Partition table** — a row the suite explicitly RULES | `A12` wrote `(Tenure, hold)` instead and reported a **closed seam as open**: *"a dead king still holds the crown."* **The first defect to point the DAMNING way**, and the guard I had written was asymmetric — it caught invented rows, not omitted ones | the ruled row added with its causation rule; `A12` rewritten to test both directions and now **passes**; a `RULED_ROWS` table asserts ruled rows are present and correct |
| the bare words **`counter`** and **`ambient`** | `counter` matched inside *"counter-productive"*; `ambient` matched *"ambient environmental quality"*, which is **matter, and already served**. These two regexes price Law 1's central refusal and the question that goes to Jordan — **`A13` fell from 8 arcs to 3** when they were narrowed | both keyed on their real subjects; a self-test names them as the two most expensive routes in the file |

**Six defects, and the last three were found by audits that never saw my reasoning.** That is the
relay working exactly as `CLAUDE.md` §10 describes it — structural independence, not a declared
posture. It is also the honest reading of the self-review I did before them: four passes of my own
adversarial checking did not find any of the three.

**Narrowing a bad route is only half a fix.** Cutting `W2`'s regex without adding `P34` would have
turned sixteen real findings into `UNMAPPED` — silence that reads as absence. The rule this build
ended on: **when a route is wrong, read what it was catching before you cut it**, because the
mis-catch is usually a capability the probe set does not have.

**And the direction of the error matters more than the count.** Four defects flattered the shape,
one damned it, one did both. **Every time the measurement got more careful, the shape's bill got
smaller** — the arc-ending refusal fell from 40% to 16%, `A13` from 8 arcs to 3, and `A12` from
FORBIDDEN to PASS. That is a fact about instruments as much as about this shape: **a crude
instrument systematically overstates a strict design's cost**, because a strict design refuses
precisely-specified things and a crude instrument matches imprecisely.

**Known remaining weakness, stated rather than hidden:** routing is still keyword-based and still
imperfect — `NPC-005`'s *"a capability she secretly has"* routes to `A2`, which is not what that need
is about. **This is why §1 marks case verdicts advisory and probe verdicts hard.** The honest
instrument reports **243 `UNMAPPED` needs of 527** rather than pretending to cover them, and marks
15 cases `NOT-ASSESSED` rather than passing them. At 78 cases keyword routing is at its ceiling; a
larger corpus needs the lanes to emit a capability tag, not prose the runner greps.

---

## §6 · WHAT THIS TEST SAYS IS REQUIRED

Ordered by how many characters it unblocks. Each composes on primitives the shape already has.

1. **Write `causes[]`.** `resolve()` must attribute each Event to the claims and events that
   motivated its act. Nothing else in the suite can be evaluated until the provenance chain exists.
2. **Let a person hold a thing.** One `hold` Tenure whose object is a `Record` closes `P29` and
   `P10` together, and gives `01` §3.1's *custody* a carrier.
3. **Give the moral layer its motion.** A per-conviction scar counter, written at WITNESS, is an
   INTERIOR row of exactly the shape the write matrix is missing.
4. **Admit one ratchet.** Some quantity must be allowed to accumulate without decaying, or five
   characters lose their arcs. This is a **bounded, named exception to Law 3**, not its abandonment.
5. **Specify what a sitting decides.** `judging_set_rule` is named and empty; three cases stop there.
6. **Decide what a death does to an office**, and say why a storm may not do the same.
7. **Make deferral visible.** An abstention that emits, so that a ruler's refusal to decide is
   witnessable and chargeable rather than indistinguishable from absence.
8. **Let work span seasons**, and let a person make a durable thing.

**Not on this list, deliberately:** a stored aggregate, a second resolver, a threshold that fires an
outcome with nobody deciding. `A2`'s FORBIDDEN is the shape working, and three cases pay for it —
that is a price, not a defect.
