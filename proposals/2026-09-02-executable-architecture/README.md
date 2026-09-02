# The season loop, executable — the successor to PR #353

## Status: **PROPOSED (2026-09-02). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.** Nothing here runs.

| file | what it is |
|---|---|
| **`PLAN.md`** | **the improvement plan — read this first if you are about to do work.** What to build, in what order, what may not be invented while building it, and the one question for Jordan. It also **adjudicates `ARCHITECTURE_V2.md` and corrects it in three places** |
| **`ARCHITECTURE_V2.md`** | **the proposal.** Read Part A before the tables, or they look like bureaucracy |
| `../2026-09-01-season-loop-tests/` | the executed session it rests on — instrument, 143 cases, run output |
| `../2026-09-01-season-loop-tests/session/00_FINDINGS_LEDGER.md` | the 56 findings, transcribed |

## The one-sentence difference

> **#353 specified a season loop that cannot be executed without inventing.** This document closes
> every place where that was true — not by deciding what #353 deliberately left open, but by making
> each opening a **row with an owner, a grade, and — where the shape is ruled and only the value is
> open — a default an instrument may inject without inventing it.**

## How it was found

An instrument implementing #353 was built and attacked four times: three structurally-independent
read-only critics and one anti-fabrication auditor, **56 findings**. Rounds 1 and 2 flattered the
shape; round 3's errors ran **both ways**, which is worse. The measured result of the tested version:

**46 NPCs · 97 arcs · 972 requirement rows · 121 probe executions · ZERO cases that ran end to end.**

## What it inherits, and it is most of the document

**Parts I–VI of #353 are right and are inherited whole** — the one sentence, the nine throughlines,
the five laws, R-1/R-2, the two topologies, the six steps, `Event` without an actor or a target, one
log, the seam, no per-container clock, fixed point, the Godot port, **and all of Part VIII's
refusals**. 43 of 63 probe PASSes were raised by a gate, a type or a law in the shape itself.

**A successor that rewrites Parts I–VI is a worse document.** The failures are not in the
architecture; they are in what the architecture declines to say.

## What it changes

- **Part D** — the write matrix keyed on **`(kind, field)`** rather than on things, 13 rows → 33,
  with a `social:` column that can actually be applied and an `emits:` column so a band crossing has
  an antecedent to cite.
- **Part E** — **the verb table: the resolver's body.** #353 names ~25 verbs across nine sections and
  says what none of them writes. This is why the tested version could only *grade* cases, never
  *run* them.
- **Part F** — `q`'s producer, the NPC decision policy, `budget` resolved **by precedent**, and a
  `standing` formula that needs no cross-holder read.
- **Part G** — **the delegation doctrine.** §42.2.1's *"refuse, don't pick"* survives for
  `absent`-grade holes and is extended to inject-declare-**sweep** for holes whose shape is ruled.
- **Part VII** — **the hole register**, replacing §61–§62's prose: **39 holes, 8 ruled, 13
  assumption-with-a-default, 12 absent.**

## The two things a reader should carry

1. **The set of things an instrument is FORCED to invent is the specification's execution gap,
   located precisely.** It cannot be found by reading. It was found by trying to run.
2. **Twelve refusals a reader can count is worth more than an unknown number an instrument fills.**
   #353 had the same holes and did not enumerate them.

## What it does not do

- **It does not decide the twelve `absent` holes.** Three are genuine escalations (scene=act;
  refraction's side; whether a person carries a banded scalar); nine are authoring work.
- **It does not weaken a refusal.** ~22 core blocks stay refused, named and counted.
- **It does not cite the session's case verdicts.** Two auditors ruled them uncitable in either
  direction; only the probe ledger is cited.
- **Nothing executes.** §I2 lists eight artifacts and marks the seven that cannot be satisfied by
  writing. **Artifact 2 is the bar: one NPC season, end to end. The tested version ran zero.**

---

## What the plan adds, in four lines

- **Eleven of `ARCHITECTURE_V2.md`'s twelve `absent` holes close or downgrade *in chain*** once
  `CLAUDE.md` §0's five tests are actually run over them. **One genuine escalation survives** —
  does a scene equal an act? — **and it blocks nothing.**
- **Nineteen holes have no row at all.** The register could not report this because **it is a
  markdown table nothing reads**, whose own counts do not reproduce from its own rows.
- **The critical path is six items** — `W0 → W1 → W2 → W3 → W5 → W9` — ending at **one NPC season
  running end to end**. Everything else runs beside it.
- **Three of this chain's own rulings are overturned in `PLAN.md` §1.3**, including a "verified
  negative" that was a keyword search.
