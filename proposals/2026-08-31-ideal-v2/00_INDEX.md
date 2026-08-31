# THE IDEALIZED SYSTEM, v2 — INDEX

## Status: **PROPOSED (2026-08-31). NOTHING HERE HAS EXECUTED.**
## No simulation was run, no test was written, no number was measured, no season was ticked.
## `CLAUDE.md` §0.2 applies in full: **done means it runs, and none of this runs.**
## Nothing ratifies on merge.

> ## ⚠ THIS SUITE WAS BUILT ON ~12% OF THE CORPUS — READ THIS BEFORE ANY CLAIM IN IT
>
> Of **123 proposal documents over 200 lines, 108 are cited nowhere** in this suite or in the two
> documents it supersedes. **Four mechanisms presented here as new or missing are already designed in
> uncited documents:**
>
> - **the actorless event channel, including Altonian pressure** — `proposals/2026-08-29-greenfield-systems-suite-v2/11_world_events.md` (715 lines), which ships `we.altonian_pressure` and records `external_shock` as *"never defined by anything on disk"*;
> - **`ambition`'s carrier** — `…-v2/09_ambitions_and_arcs.md` + `_part2` (1,065 lines), with derived-at-read `progress`;
> - **the act-economy reconciliation** — `proposals/2026-08-30-fixes/02_the_act_economy.md` (426 lines), which is D-2 already worked out;
> - **slate and salience** — `…-v2/10_the_slate_and_salience.md` + `_part2` (1,152 lines), which is *how anything gets put in front of a decider*.
>
> **EVERY "THERE IS NO X" CLAIM IN THIS SUITE IS SCOPED TO THE DOCUMENTS IT READ, AND THAT SCOPE IS A
> MINORITY OF THE CORPUS.** Two adversarial review rounds, five parallel audit runners and a keys audit
> all missed this, because **every one of them audited derivative documents against each other.**
> **Citation count is not coverage.**

---

## The three documents

| # | file | what it owns |
|---|---|---|
| **1** | **`01_ARCHITECTURE.md`** | **The primitives and the refusals.** Four carriers · one edge with seven kinds · **one state change with three modes and two drivers** · the query category · the amended owner table · the three signatures · determinism · **all seven reserved forks worked** · the seam the three deferred subsystems attach at · **the fourteen refusal rows walked for every new object** · every departure from the prior design with its ground · what is carried open |
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
Person · Rung · Office · Site               -- the carriers. A cohort is a Person at weight > 1
Tenure                                      -- the one edge, seven kinds
StateChange := (subject, mode, driver)      -- mode ∈ mint|alter|efface
                                            -- driver ∈ Act | Event, and the SUBJECT decides which
Query                                       -- never stored, always recomputed

choose  : (Person, View, Sensation) -> Act      -- no World
resolve : (Act[], World)            -> Event[]  -- no Person
witness : (Person, Event)           -> Claim[]  -- per person; never a collection

CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS
```

> **JORDAN'S PARTITION governs everything above.** A state change whose **subject is peninsular human
> society** — polities, institutions, offices, organizations, occupations, religion, settlements,
> marriage — is **driven by a character's choice, always.** A change whose subject is anything else —
> weather, the non-peninsular, tears in the metaphysical substrate — is **an event acting on the
> world.** **Creation and deletion included: events create and destroy too.**
>
> **A plague may kill bodies. It may NOT efface a settlement — the village empties and still legally
> exists until an office strikes it from the roll.** Villages do not cease to exist because everyone
> died.

**Scope.** The seasonal loop, and all of it: worldly state, clocks, pressures, threats, world churn,
character generation, event generation, governance at every scale, advancement and demotion, conflict,
obligation, offices, occupations, roles, petitions, orders, field investigation, parliament and
parliamentary debate, factions, competing beliefs, epistemics, memory, truth.

**Deferred:** mass battle, personal combat, social contest. They attach at **one** seam — `resolve`,
where a contest subdivides the tick — and `01_ARCHITECTURE.md` §8 specifies that seam and nothing else
about them.

---

## The seven forks

**All seven are answered.** Five dissolve under a primitive; **two were ruled by Jordan**, and one of
those reversed an answer this suite had already given.

| fork | disposition | what carries it |
|---|---|---|
| **D-2** the act economy | **ruled: one act per person or cohort, universally** | an office's throughput is its **establishment's** acts |
| **F1** conferral basis | **dissolves** | `Office.conferral` names the basis **per office** |
| **F2** is `stores` the denominator | **dissolves** | `Stores := map[MatterKind → quantity]` |
| **F3** S19, the rootless vacancy | **dissolves** | a conferral rule may name **the office's own judging set** |
| **F4** the Coherence-0 ontology | **not a fork** | de-individuation by another cause |
| **F5** off-board polities | ⚠ **REVERSED — they are an EVENT SOURCE, not a simulated realm** | non-peninsular by definition, so they act through events. **No off-map realm is simulated** — a large deletion — and the one-actor rule is preserved *properly*, since it governs persons and Altonia is not a person |
| **F6** dying or misunderstood | ⚠ **RULED BY JORDAN — NEITHER. THE WORLD IS IN FLUX** | *"If the world is not tended to by anyone, it will die. If it is tended to by everyone, it will thrive."* **A third answer neither branch offered: the direction is an OUTPUT, the sum of what people do about it.** Cost: one constant, `wear`, and zero objects |

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

**Every one of the seven forks is now answered**; F6 and F5 by Jordan's own rulings, and F5's earlier
answer was wrong and is reversed.

⚠ **AND THE MOST IMPORTANT LIMIT IN THIS SUITE IS ABOUT HOW IT WAS AUDITED.**
`proposals/2026-08-29-valoria-from-scratch/03_knowledge_telling_investigation.md` — **980 lines, the
largest document in #342 and the declared owner of the claim, the predicate vocabulary, view assembly,
salience, corroboration, concealment and field investigation — was never read** by two review rounds,
five parallel audit runners, a 982-line identity audit, or the first draft of these documents. **It is
cited three times across 3,840 lines of derivative text, which made it look covered. Citation count is
not coverage.** The cost was two FATAL errors, a reinvented claim source, and an invented `investigate`
verb standing where six shipped acts already were. **Every audit was derivative-facing, and agreement
between derivative documents read as corroboration when it was correlated error with one root** — the
failure this design's own corroboration rule exists to prevent, arriving in the process that produced
the design. `01_ARCHITECTURE.md` §12.8.


---

## THE NAMED NEXT STEP — five documents this suite never read

**Do not treat this suite as complete until these are read.** Line counts are exact; the clause is what
each owns.

| document | lines | what it owns |
|---|---|---|
| `proposals/2026-08-29-greenfield-systems-suite-v2/11_world_events.md` | **715** | the actorless event row, rate bounds, two-way reachability, a registry block, and **`we.altonian_pressure`** — Jordan's own Altonian channel, already mechanised |
| `…-v2/10_the_slate_and_salience.md` + `_part2` | **1,152** | **how anything gets put in front of a decider** — the direct answer to CALENDAR's agenda question and to §14 row 14 |
| `…-v2/09_ambitions_and_arcs.md` + `_part2` | **1,065** | ambition as a first-class object with **derived-at-read `progress`**, bands not numbers, and lapse |
| `proposals/2026-08-30-fixes/02_the_act_economy.md` | **426** | **D-2, already worked out.** This suite's act-economy resolution may be a re-derivation of it |
| the play-space coverage lanes and gap report | **5,270 across 8** | what the design was measured against |

⚠ **AND THE SWEEP STOPPED AT `proposals/`.** Two load-bearing `systems/` documents are also uncited:
**`systems/_architecture/governance_ripple_substrate_v1.md`** (559 lines — **the event deck's own
governing spec**) and **`systems/settlements/governance_play_redesign_v1.md`** (337). **The next gap is
likelier to come from `systems/` than from `proposals/`.**
