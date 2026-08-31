# THE AUTHORITATIVE ARCHITECTURE — INDEX

## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 every document here is **REFERENCE, never mechanism.** No behaviour is
## correct because a row here says so. Under §0.2, **done means it runs — and almost none of this runs.**

> **THE ONE-LINE STATE OF THE WORLD.** Eight merged pull requests (#337–#344) produced roughly 90,000
> lines of design across four mutually incompatible primitive sets. **Every core object of the winning
> set — `Person`, `Rung`, `Office`, `Site`, `Tenure`, `Query`, `Act`, `Claim` — is absent from
> `engine/` and `systems/` as a named identifier.** `tools/m1_acceptance.py --summary` reports M1 at
> **0/7 junctures, verdict NOT MET.** This suite does not change that. It makes the next commit that
> *would* change it obvious, ordered, and small.

---

## Why this suite exists

`proposals/2026-08-31-ideal-v2/` is the current design head and it is good work. It also opens by
confessing that it was built on a minority of the corpus and re-invented mechanisms already designed
elsewhere. Jordan directed a full reconciliation: trace every instance of code architecture across
#337–#344, sweep the repository for the corresponding design and code, adjudicate the result, and
produce one authoritative suite.

**The method, so its limits are legible.** Eight tracing agents (one per PR) and six repository sweeps
(`engine/`, `systems/`, `godot/`, the registries, the corpus, the execution surface) ran read-only and
could not see each other. Their fourteen logs are committed at
`proposals/_session_provenance/2026-08-31-architecture-reconciliation/` and are the evidence base for
everything below. Five adjudicators then ruled on the logs and on the tree. **Where two lanes that
could not see each other found the same thing, that is flagged — per `CLAUDE.md` §10 it is the
strongest signal available. Where they conflicted, the conflict was ruled rather than averaged.**

---

## The eight documents

| # | file | what it owns |
|---|---|---|
| **01** | `01_THE_ARCHITECTURE.md` | **The primitive set.** Four carriers · the fifth identity-bearing record · one edge with seven kinds · one state change under Jordan's Partition · identity and ids · the ownership table · the three signatures · the Query category · what is excluded and what already covers it |
| **02** | `02_THE_LOOP.md` | **The season, nested in the tick that already runs.** Six steps inside three phases · four barriers · four write classes · the write matrix · order independence · determinism · what the loop refuses |
| **03** | `03_CODE_SHAPE_GODOT_4_6.md` | **The port.** Project layout · the autoload rule · carrier placement · the purity problem and what actually enforces it · fixed-point arithmetic · save/load · ids-not-pointers · the seam · the version question, handled honestly |
| **04** | `04_THE_REGISTER.md` | **Names and keys.** The executing Key substrate · the key namespace · the completed collision register · the naming rules · the closed sets · ED-IN-0200 discharged |
| **05** | `05_COVERAGE_AND_SUPERSESSION.md` | **What to read and what to ignore.** Coverage measured · the supersession map · the duplication register · the gap register |
| **06** | `06_ADJUDICATIONS.md` | **Every ruling, with its ground and its falsifier** · what was overturned · the three escalations that survive all five tests |
| **07** | `07_EXECUTION_PATH.md` | **The ordered build plan in which every step ends in something running**, with the execution artifact named for each · the four structural tests, specified |
| **08** | `08_PROVENANCE.md` | Where every claim came from · the fourteen logs · the method's own limits |

**Read 01, then 02, then 07.** The others are reference for the reader who needs them.

---

## The architecture in one page

```
Person · Rung · Office · Site                    -- the four carriers (mutable, identity-bearing)
Proposition                                       -- the fifth identity-bearing record (immutable)
Tenure                                            -- THE one edge, seven kinds, per-kind cardinality
StateChange := (subject, mode, driver)            -- mode ∈ mint|alter|efface, driver ∈ Act|Event
Query                                             -- never stored, always recomputed

choose  : (Person, View, Sensation) -> Act        -- no World
resolve : (Act[], World)            -> Event[]    -- no Person
witness : (Person, Event)           -> Claim[]    -- per person; never a collection

CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS
```

**Jordan's Partition governs every state change.** A change whose subject is peninsular human society
— polities, institutions, offices, occupations, religion, settlements, marriage — is driven by a
character's choice, always. A change whose subject is anything else — weather, the non-peninsular,
tears in the substrate — is an event acting on the world. **Creation and destruction included.** A
plague may kill bodies; it may not efface a settlement. The village empties and still legally exists
until an office strikes it from the roll.

---

## The four rulings that changed the head

Each is argued in `06_ADJUDICATIONS.md` with its ground and its falsifier.

1. **This is not greenfield, and it is not a refactor.** It is a **greenfield carrier-and-edge layer
   composed on top of a kept, executing substrate.** The Key substrate (`engine/substrate/keys.py`)
   *is* the design's Event mechanism in substance — append-only, id-unique, referentially checked,
   content-hashed, running default-ON in every seeded campaign. It is **not** the Claim/witness/Query
   mechanism: those exist only as pseudocode, and the substrate's own docstring says so. Two
   independent sweeps reached opposite verdicts on this and both were half right.
2. **The six-step loop is a refinement of the running three-phase tick, not a replacement.**
   `engine/autoload/engine_clock.py` runs `SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY` today, pinned
   by tests and byte-exact goldens. The six steps nest inside it. The seven-phase season of #343 is
   retired.
3. **The port is written to Godot 4.6 as directed, and exactly two things depend on the choice.**
   Typed `Dictionary` (4.4+) and `@abstract` (4.5+), each with a fallback. Everything hard about the
   port is version-independent. **But the 84-error compile ratchet is a property of the 4.3 binary,
   and under a 4.6 ruling it is void until re-measured.** That is an escalation, not a decision this
   suite may take.
4. **The design's own coverage confession is itself stale, and the true numbers are worse.** 133
   documents over 200 lines, not 123; **103 uncited, 67.7% of the corpus by line weight.** The head
   touches 0% of `research/` and neither of the two governing Jordan rulings.

---

## What this suite refuses to do

- **It proposes no apparatus.** No validator, guard, register, checker or process document. Nothing in
  the architecture requires one, and `CLAUDE.md` §0.1 point 5's load-bearing predicate would forbid
  most of them anyway.
- **It claims no measurement.** Every number is quoted from a cited line or is a design proposal.
  Nothing here was computed by running the game.
- **It does not treat itself as mechanism.** If a table here and the code disagree, that is a defect in
  one of them, and it is resolved by deciding and then **changing the code** — never by declaring the
  prose authoritative.
- **It does not settle the engine version by fiat.** `CLAUDE.md` §3 forbids it. The suite is written to
  4.6 as directed and marks every place the choice is load-bearing.

---

## The honest state of the evidence

**Nothing in this architecture has been executed.** The four structural tests it rests on — no
decision function can see the world · two witnesses of one event can disagree · a person with no
office can act, petition and receive an opportunity · order independence — **have never been run.**
`07_EXECUTION_PATH.md` specifies all four precisely enough to implement, and names the step at which
each first becomes runnable. That is the difference this suite is trying to make.

**The strongest results here are the ones that were rediscovered independently**, because agreement
between documents that read each other is correlated error, not corroboration — which is exactly the
failure the head diagnosed in its own process. Those are flagged throughout with the lanes that found
them.

**The weakest part is the same as the head's:** the corpus is large and most of it is still unread.
`05_COVERAGE_AND_SUPERSESSION.md` says how much, names what to read next, and ranks it by how much it
would change the architecture.
