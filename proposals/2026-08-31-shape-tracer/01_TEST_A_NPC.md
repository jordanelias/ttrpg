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
| verdict | **20 BLOCKED · 7 DEGRADED · 0 PLAYABLE** |
| probes | 55 executed attempts against the shape — **17 PASS, 1 PARTIAL, 37 gaps** |
| trace | 68 acts, 98 events, 284 class-checked writes |
| gap kinds | 22 NO-PRODUCER · 10 UNSPECIFIED · 3 COLLISION · 3 FORBIDDEN |

**A case is BLOCKED when a need its own lane graded `core` maps to a probe that could not execute.**
Not one of twenty-seven named characters has a season that runs end to end.

⚠ **THE PROBE VERDICTS ARE THE HARD RESULT. THE CASE VERDICTS ARE ADVISORY.** Needs are routed onto
probes by keyword, and keyword routing is crude: it mis-fired twice in ways I caught (§5) and is
certainly still mis-firing in ways I did not. **83 needs are reported `UNMAPPED`** rather than
silently passed. Read a case verdict as "this character's season met a wall", not as an exact count.

---

## §2 · WHAT SUCCEEDED — and one of these is excellent

Seventeen probes pass, and they are not trivial passes; each is an execution.

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
| **A4** | **4** | `resolve()` emits Events with an **empty `causes[]`**. Nothing in the specified loop populates the causal edge that `06` §1 calls *"the arc itself"* |
| **P29** | **3** | A `Record` is homed as **Rung matter** — it sits at a *place*, never in a person's hands. *"She was found with it"* is not expressible |
| **A2** | **3** | A threshold firing with nobody deciding is **FORBIDDEN** — correctly, and it costs |
| **F6** | **3** | A sitting convenes; `judging_set_rule` is a named Rung field that **no document specifies**, so nothing is decided there |
| **P4** · **P18** · **P28** · **P30** · **W2** | 2 each | conviction motion · staged institutional judgement · making a durable thing · work spanning seasons · band strobing |

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

### 3.2 The King is blocked, and on what

Almud's lane graded five needs `core`. Three of them fail:
- *his standing army gradually reassessing its loyalty in stages that do not revert* — **`P18`**;
- *his long-held private doubt persisting for seasons, that persistence itself being a choice* —
  **`P19`**: a person who chooses nothing produces no Act, so no Event, so **nothing enters anyone's
  ledger. A king's sustained refusal to decide is invisible and indistinguishable from his absence**;
- *being more constrained by visibility than a private person would be* — **`P21`**: the same act by
  a king and by a copyist produces Events identical in scope, because nothing in `Act`, `Event` or
  `witness()` reads the actor's office.

**What passes for him is the delegation half** (`P9`, `P20`, `P24`). **What fails is the interior
half** — doubt, publicness, and an institution's slow judgement of him.

### 3.3 One declared seam, reached by execution

`A12` kills a person and tries to end their tenures. Death is churn row 3, an **Event** at MATTER.
A `hold` on an office is a **`social: true`** row, which an Event may not write. So **a dead king
still holds the crown.** The suite declares this itself in `05` §7 — *"a death DOES end a tenure,
and the column alone does not explain why a storm may not"* — and churn row 3's own N-line is
*"succession never fires; every office is held forever."* **The Partition as keyed blocks the
mechanism row 3 exists to provide.** The tracer reaches it by execution and prices it.

---

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

**Known remaining weakness, stated rather than hidden:** routing is still keyword-based and still
imperfect — `NPC-005`'s *"a capability she secretly has"* routes to `A2`, which is not what that need
is about. **This is why §1 marks case verdicts advisory and probe verdicts hard.** The honest
instrument reports 83 `UNMAPPED` needs rather than pretending to cover them.

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
