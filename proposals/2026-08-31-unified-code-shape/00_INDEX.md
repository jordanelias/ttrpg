# THE IDEAL UNIFIED CODE SHAPE — INDEX

## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 every document here is **REFERENCE, never mechanism.** No behaviour is
## correct because a row here says so. Under §0.2, **done means it runs — and almost none of this runs.**

> **WHAT THIS IS.** One code shape for Valoria's **season loop**, its **world churn**, its **emergent
> narrative**, and **persons and the player as the throughline that runs through all three**. It is
> reconciled from eight merged pull requests, fourteen trace logs, five prior adjudications and the
> executing tree, by eight read-only adjudication lanes and one execution pass.
>
> **It is IDEAL and NOT BOUND TO PRECEDENT.** It takes only what is best. Where the running tree already
> holds the best answer it is adopted **because it is best** — six such places, named in `15` R-1 — and
> where it does not, the shape takes the better answer **and prices what walking away costs.**

---

## THE ARCHITECTURE ON ONE PAGE

```
Person · Rung · Office · Site                 the four carriers — identity-bearing, MUTABLE
Proposition                                   the fifth identity-bearing record — IMMUTABLE
Tenure                                        THE one edge · seven kinds · cardinality on the schema
StateChange := (subject, mode, driver)        mode ∈ create|alter|destroy   driver ∈ Act|Event
Query                                         never stored, always recomputed, two sides

Claim        what a person holds TRUE     — moved by EVIDENCE, at WITNESS
Conviction   the moral AXES (13, closed)  ┐
Belief       what a person holds RIGHT    ├ moved by ARGUMENT and CONSEQUENCE, at RESOLVE
Duty         what a person OWES           ┘   — an `oblige` Tenure; no new record

choose  : (Person, View, Sensation) -> Act        NO World, ever
resolve : (Act[], World)            -> Event[]    NO Person
witness : (Person, Event)           -> Claim[]    per person; a collection is not spellable

CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS
   nested in the tick that already runs:  SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY
```

**Four laws, and everything else is derivable from them:**

1. **THE PERSON IS THE ONLY ACTOR.** Not a faction, not a settlement, not an institution, not a clock.
2. **NOBODY IS OMNISCIENT, AND THE SIGNATURES ARE HOW** — by what they omit.
3. **EVERY AGGREGATE IS A FUNCTION, NEVER A FIELD.** Nobody owns an aggregate.
4. **EVERY STATE CHANGE IS PARTITIONED BY ITS SUBJECT** — and the test is a static schema column keyed
   on `(record-kind, field)`, which is what dissolves the mixed case *"both"* leaves open.

---

## HOW TO READ THIS — holistic to granular

| layer | documents | what it settles |
|---|---|---|
| **L0** | **`00_INDEX.md`** (this) | the whole shape, the reading order, the status |
| **L1** | **`01_THROUGHLINE.md`** | the four laws · the nine throughlines made structural · the player model · what is refused and what covers each refusal |
| **L2** | **`02_ONTOLOGY.md`** · `03_OWNERSHIP.md` · **`04_THE_SEASON_LOOP.md`** | every type and field · who owns every value · the six steps, four barriers, four write classes and the write matrix |
| **L3** | `05_WORLD_CHURN.md` · `06_EMERGENT_NARRATIVE.md` · `07_THE_PLAYER_AND_THE_PERSON.md` | one step each, elaborated: what happens with nobody acting · how a story arises with nobody authoring · how a person decides and what a player touches |
| **L4** | `08_FUNCTION_SURFACE.md` · `09_THE_SEAM.md` · `10_GODOT_4_6.md` | every signature and the Query catalogue · how a contest plugs in · the port |
| **L5** | `11_PARAMS.md` · `12_TESTS.md` · `13_EXECUTION.md` | every constant and its grade · every structural claim and its falsifier · the ordered build |
| **registers** | `14_NERS.md` · `15_ADJUDICATIONS.md` · `16_PROVENANCE.md` · `TRACE_REGISTER.md` · **`ADVERSARIAL.md`** | the audit · every ruling with its falsifier · how this was made · every verified `path:line` · **and the adversarial pass that found 16 MAJOR defects in the above, 0 fatal** |

> **Read `01`, then `04`, then `13`.** `01` is what the shape believes, `04` is the thing itself, and
> `13` is the only document whose purpose is to stop being a document. The rest is reference for the
> reader who needs it.

---

## THE SIX RULINGS THAT SHAPE IT MOST

Each is argued in `15_ADJUDICATIONS.md` with its ground and its falsifier.

1. **The event log is the Event mechanism; it is NOT the Claim/witness/Query mechanism.** Two competent
   sweeps reached opposite headlines from one tree and **neither survives whole.** Compose Event onto
   the executing log; build the epistemic layer fresh. **And WITNESS carries a real precondition: an
   ordering rule that is drafted, unratified, and cannot be coded around.**
2. **The six steps are a REFINEMENT of the running three-phase tick**, verified this pass, including
   that the middle phase's body is caller-supplied by design — which is exactly the seam they need.
3. **A `Belief` is about MORALS, not veracity** [Jordan, this session]. What a person holds **true** is a
   `Claim`; what they hold **right** is a Belief backed by Convictions. **Evidence moves the first;
   argument and consequence move the second. WITNESS never touches a Belief.**
4. **A Proposition of mood `OUGHT` is an uttered Belief** — so **a faction is somebody's morals, said out
   loud, that other people signed.** The political layer is grounded in one person having said what they
   think is right.
5. **The degree ladder is four bands, and the corpus's five-band table describing itself as shipped is
   overturned.** **Neither trace log recorded the collision.**
6. **The world's trajectory is an OUTPUT** — `wear` against tending — and the world-substrate hole three
   arc lanes found independently **closes as a `Site` kind, with zero new objects.**

---

## WHAT THIS SUITE REFUSES TO DO

- **It proposes almost no apparatus.** Four guards are licensed and named, each load-bearing on the game
  or the port; **everything else is forbidden**, including any validator whose subject is this
  repository's own process.
- **It claims no measurement.** Every number is quoted from a cited line, or graded **ASSUMPTION** in
  `11_PARAMS.md`. **Eleven of twenty-five parameter rows are assumption-grade, and the ledger says so.**
- **It does not treat itself as mechanism.** If a table here and the code disagree, that is a defect in
  one of them, resolved by deciding and then **changing the code.**
- **It does not settle the engine version by fiat** — and it re-labels the fork, because **nothing here
  needs 4.6**; two things need ≥4.4 and ≥4.5, so the real question is **4.3 versus ≥4.5**.
- **It says almost nothing about personal combat, social contest or mass battle.** They appear at one
  place — the seam — by instruction, and `09` is four pages rather than forty because of it.

---

## THE HONEST STATE

**Nothing in this architecture has been executed.** The structural claims it rests on — **no decision
function can see the world · two witnesses of one event can disagree · a person with no office can act,
petition and receive an opportunity · order independence** — **have never been run.** `12_TESTS.md`
specifies all four precisely enough to implement; `13_EXECUTION.md` names the step at which each first
becomes runnable.

**And the tree it composes on is further from this than the design line believed.** Measured this pass,
much of it by running rather than reading: **the campaign resolves with zero people in it · 2 of 55
registered event types are ever emitted · 30 of 31 faction-stat writes bypass the event log · 71 of 140
non-test modules are never loaded · a campaign-length parameter is dead · four malformed registry fields
make two event types unemittable · fifteen modules annotate a type they never import.**

**The strongest results here are the ones rediscovered independently**, because agreement between
documents that read each other is **correlated error, not corroboration** — which is exactly the failure
the design line diagnosed in its own process. Those are flagged throughout with the lanes that found
them, and `16` §3 says why each is not seeded.

**The weakest part is the same as every predecessor's:** the corpus is large and most of it is unread.
**The sweep instrument, run against current `main` this pass, reports 162 documents swept, 24 cited, 138
uncited.** This suite has not read the 138 either — **and the coverage figure is itself a measurement
that changed what it measured**, which `16` §4 states rather than hides.

> ⚠ **AND THIS SUITE WAS WRONG ABOUT ITSELF IN SIX PLACES, RECORDED AT `15_ADJUDICATIONS.md` §4 RATHER
> THAN QUIETLY FIXED.** An adversarial pass with execution found **16 MAJOR and 14 MINOR defects, none
> fatal**. The three that changed a ruling: the flagship `0.671` "arithmetic error" is **a different
> die, exact for its own model** — a departure this suite had to declare rather than a constant to
> correct; **`Momentum` was re-added after the source cut it twice as a false N-line**; and *"the ten
> LOST arcs are one loss"* is **the exact conflation a source lane forbids by name**, overstating the
> cost of the design's central refusal roughly threefold. **All three are folded in above.**

> **Until `13_EXECUTION.md` step 1 lands, the correct description of this entire suite — every document
> in it — is that it is prose.** That is not false modesty. It is the standard, and the only reason `13`
> exists is to be the shortest path out of it.
