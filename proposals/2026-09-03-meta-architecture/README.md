# THE META-ARCHITECTURE — the layer above the plan

## Status: **PROPOSED (2026-09-03). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

| file | what it is |
|---|---|
| **`01_AXIOMS.md`** | **Stage 1 — axioms, idioms, schema.** Start at PART A |

## What this is

Jordan-directed, 2026-09-03: *"a top-down exercise to develop axioms/idioms/schema and consequently
hierarchies, dependencies, nests and scales and therefore discussing verbs, consequences alongside
slices and season loops… We are not building something bottom up that can run as code — we are
performing a meta-architecture exercise from top down to determine the ideal logical shape for
future work."*

**Three stages, in that derivation order. This directory holds the first.**

## Scope — the rule this exercise is under

**The admissible sources are the axioms themselves and the PR chain #337 → #357.** Nothing under
`canon/`, `systems/`, `research/` or `engine/` is authority. **We are designing an idealized system,
so prior work is not a constraint on it** — and "the tree already does it this way" is not an
argument for anything.

⚠ **A first draft of PART E broke this rule and is withdrawn in full.** It was built on a sweep of
the repository, and the reason that is wrong is worth keeping: *evidence that something is already so
is not an argument that it should be so.* An idealized shape argued from the existing tree is the
existing tree with better prose.

## The one-sentence difference from everything upstream

> **`PLAN.md` says what to BUILD. `ARCHITECTURE.md` says what the season loop IS. This asks what the
> THINGS are — and states the small number of commitments everything else is derived from.**

`PLAN.md` is **PAUSED at Jordan's direction, not superseded.** Its critical path
`W18→W20→W21→W22→W23→W26→W27→W30` stands and is not withdrawn.

## What Stage 1 concludes

- **Axioms and theorems are different things, and the chain's five coordinate "laws" mix them.**
  `L5` derives from `AX-1`; `L3`'s clause 1 from `AX-4` and its clause 3 from `AX-6` — ⚠ **not all
  of `L3` from `AX-4`, which the first publication claimed and an adversarial pass broke.** The
  demotion is the point: **break an axiom and you have chosen a different game, deliberately; break
  a theorem and you have introduced a contradiction that surfaces later as a defect nobody can
  localise.**
- **The schema is written as ADMISSION TESTS, not field lists.** A schema that lists fields can only
  grow, which is exactly how the entities *"grew one defect at a time."*
- ⚠ **`H-101`'s first answer was WRONG and is corrected in place.** It said subordination *cannot be
  stored*. An adversarial pass showed the step never established that the edge is
  Proposition→Proposition, and that **`oblige` — already rostered, and named by `H-101` itself** — is
  storable, owned by the person who swore it, and **more `AX-1`-faithful than a Query nobody
  authored.** The faction half is derived; **the office half SPLITS**, by this section's own
  falsifier.
- **And the correction found the better result: FOUR OF SEVEN RELATIONS CAN BE OPENED AND NEVER
  CLOSED.** `oblige`, `succeed`, `tie`, `knot` have no closing verb, so a duty cannot be discharged,
  a bond cannot be broken and a succession cannot be changed. **That is why the first answer looked
  right** — facing an irreversible edge, "make it a Query" is the reachable repair. The reversibility
  was real; the diagnosis was wrong.
- **There are SIX axioms.** `AX-6` — *nothing becomes permanent without an author* — was found
  missing when two separate derivations reached for it and neither could get there from the other
  five: `L3`'s ratchet clause, and the four open-only relations above. **`AX-1` says nothing moves
  without an author; `AX-6` says nothing stops being able to move without one.**
- **Part C gained two idioms because it FAILED its own acceptance test.** The chain's commonest
  instance of the named defect class is *a declared axis that decides nothing* — which `ID-9` misses
  (it needs a write) and `ID-10` is satisfied by. `ID-13` and `ID-14` close it.
- **A `Title` is not an entity**, and the missing conferral path is a **half-landed ruling** (two
  eligibility models, only `revoke` rebuilt on the second) rather than a hole in the ontology.
- ✅ **RULED 2026-09-03, and it dissolved the question rather than answering it.** Jordan:
  *"Regency and puppet rulers must be possible."* · *"Same with delegation."* The document had
  offered two readings of `hold`; **both were wrong**, because the blocker was never the `hold`
  overload — it was that **rank+containment is not conferrable**, so a delegate has no seam to enter
  through. The answer is one sentence: **AUTHORITY IS A PROPERTY OF THE SEAT BEING EXERCISED, NEVER
  OF THE PERSON EXERCISING IT.** A regency, a puppet ruler, a governor, a council and a mayoral
  election are then all **a conferred seat**, with no mechanism written for any of them.

## What it is not

Not ratified · does not run and is not meant to · changes no code, register row, roster or plan ·
proposes no guard, validator or tool · **not a second architecture** — #353's Parts I–VI stand, and
this states what they rest on.
