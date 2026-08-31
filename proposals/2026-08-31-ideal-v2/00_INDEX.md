# THE IDEALIZED SYSTEM, v2 — INDEX

## Status: **PROPOSED (2026-08-31). NOTHING HERE HAS EXECUTED.**
## No simulation was run, no test was written, no number was measured, no season was ticked.
## `CLAUDE.md` §0.2 applies in full: **done means it runs, and none of this runs.**
## Nothing ratifies on merge.

---

## The three documents

| # | file | what it owns |
|---|---|---|
| **1** | **`01_ARCHITECTURE.md`** | **The primitives and the refusals.** Four carriers · one edge with seven kinds · one act with five modes · the query category · the amended owner table · the three signatures · determinism · **all seven reserved forks worked** · the seam the three deferred subsystems attach at · **the fourteen refusal rows walked for every new object** · every departure from the prior design with its ground · what is carried open |
| **2** | **`02_THE_SEASON_LOOP.md`** | **How a season executes on those primitives.** Six steps, four barriers, four write classes · one detailed section per step with its pseudocode, reads, writes, invariants and refusals · three seasons walked end to end · the write matrix · order independence · what the loop refuses to do |
| **3** | **`03_COMPENDIUM.md`** | **The cross-referenced register.** Identity · types with every closed set enumerated · the reference map and its inverse index · functions · the Query catalogue · vocabulary · collisions · gaps · five cross-reference indices · what is inherited and not restated · the substrate precedent |

**Read them in that order.** The compendium indexes the other two and comes last.

---

## What this is, in one page

**The design source of truth for everything these documents do not change is
`proposals/2026-08-31-ideal/10_SUPERSEDING.md`.** Where these three are silent, read it.

**The organising question.** An adversarial review of that design found one verdict surviving its own
retractions: **the design can change the STATE of what exists, and cannot change WHICH things exist or
WHO HOLDS THEM.** Measured on Jordan's own long-arc trajectories, five of twelve transitions work, and
the cut is exact — *every transition that works is a state change on an object that already exists;
every transition that fails is a change to what exists, or to who holds it.*

**So: what is the smallest primitive set under which EXISTENCE, TENURE and STATE are the same kind of
change?**

```
Person · Cohort · Rung · Office · Site        -- the carriers
Tenure                                             -- the one edge, seven kinds
Act(touches[]), mode ∈ read|alter|exclude|mint|efface
Query                                            -- never stored, always recomputed

choose  : (Person, View, Sensation) -> Act         -- no World, ever
resolve : (Act[], World)            -> Event[]     -- no Person
witness : (Person, Event)           -> Claim[]     -- a collection is a type error

CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS
```

**Scope.** The seasonal loop, and all of it: worldly state, clocks, pressures, threats, world churn,
character generation, event generation, governance at every scale, advancement and demotion, conflict,
obligation, offices, occupations, roles, petitions, orders, field investigation, parliament and
parliamentary debate, factions, competing beliefs, epistemics, memory, truth.

**Deferred:** mass battle, personal combat, social contest. They attach at **one** seam — `resolve`,
where a contest subdivides the tick — and `01_ARCHITECTURE.md` §8 specifies that seam and nothing else
about them.

---

## The seven forks

Six are answered, each with its cost and the line that would falsify it. **One is Jordan's.**

| fork | disposition | what carries it |
|---|---|---|
| **D-2** the act economy | **ruled: one act per person or cohort, universally** | an office's throughput is its **establishment's** acts |
| **F1** conferral basis | **dissolves** | `Office.conferral` names the basis **per office** |
| **F2** is `stores` the denominator | **dissolves** | `Stores := map[MatterKind → quantity]` |
| **F3** S19, the rootless vacancy | **dissolves** | a conferral rule may name **the office's own judging set** |
| **F4** the Coherence-0 ontology | **not a fork** | de-individuation by another cause |
| **F5** off-board polities | **resolves** | a Rung with an establishment; the one-actor rule keeps **no exception** |
| **F6** is the world dying or misunderstood | **STAYS JORDAN'S** | **the code is identical and only the game differs** — which is the signature of a real fork. The other six each changed the code |

---

## What these documents refuse

- **No apparatus.** No validator, guard, register, checker or process document is proposed, and none of
  the architecture requires one (`11_code_shape.md:243-245`).
- **No claim of a measurement.** Every number is quoted from a cited line or is a design proposal.
  The three worked seasons in `02` were walked by hand.
- **No prose treated as mechanism.** Under `CLAUDE.md` §0.05 these are **reference**. If a table here
  and the code disagree, that is a defect in one of them and the resolution is to change **the code**.

---

## The honest state of the evidence

**The four highest-confidence results behind this work are the four that were rediscovered
independently by audit runners that could not see each other**: the channel store's missing licence;
the loop being four barriers with WITNESS global; `mint` sitting outside the conflict rule; and the
purge limb's missing claim source. Everything else is one reader's argument about text.

**Nothing was executed.** The four structural tests the design rests on — no decision function can see
the world · two witnesses of one event can disagree · a person with no office can act, petition and
receive an opportunity · order independence — **have not been run, and cannot be until something runs
them.**

**Thirty gaps are carried open** (`03_COMPENDIUM.md` §8), and one fork is returned to Jordan.
