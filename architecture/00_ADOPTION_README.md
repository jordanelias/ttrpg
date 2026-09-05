# The season loop, executable — the successor to PR #353

## Status: **RATIFIED 2026-09-05 (ED-IN-0202) — Jordan ruled "adopt in full". This is LAYER 1: the code architecture and shape, which GOVERNS HOW ALL CODING IS CONDUCTED. Under CLAUDE.md §0.05 it is reference for GAME MECHANISM — the code is the formula — and binding as AGENT INSTRUCTION, the same standing as CLAUDE.md itself. The game code it governs is `engine/season/`.**

> ### ⚠ **CONDITIONED BY #358 rev.2 ON 2026-09-03 — what its rewritten loader does to this chain.**
> The meta-architecture was rewritten after an adversarial pass; its loader gained a twelfth
> invariant and corrected four others. **Run against this chain's data, it refuses it in three
> places and supplies the shape for two tier-0 holes.**
>
> | | |
> |---|---|
> | **`scale:` on TEN verb rows** | fails invariant 10 (`scale:` refused by name). **Not deleted** — the keys answer a real Jordan question, and rev.2 supplies the answer as `Act.via.scope` rather than a column. Retired when `Act.via` carries the scope |
> | **`kill / wound`'s `writes`** | **now `Degree`-keyed** (invariant 12). A lost fight used to kill exactly as a won one did, because the seam's degree was discarded on arrival. Bands are `assumption`, swept at `H-98`; the shape is ruled |
> | **invariant 4 widened** | every failable clause needs a refusal kind, not only a `requires`. `kill / wound` gained one. ⚠ **Still open:** eligibility can decline and no row declares a refusal for it, while the fold emits `act.ineligible` / `act.refused` / `contest.resolved` as **body literals** that invariant 7 refuses |
> | **`H-98`, `H-62`** | **shape supplied, bands still open.** The `Degree`-keyed column is where a contest's outcome and a person's interior consequence both become expressible |
> | **`Date.fired`** | **fixed** — `RES` dropped. Its own `by:` cell said *"§24 has no actor"*, so the ACTS class contradicted its provenance on the same line |
> | **`H-90`** | **default superseded** — authority is a property of the seat exercised, not of the actor's own title-holds, which is why a regency was unbuildable rather than unwritten |
>
> **Measured, not asserted:** `write_matrix.yaml`'s header carries the reproducing command for the
> **eleven** RES rows with no producing verb (**nine** after rev.2 deletes `Person.beliefs` and
> replaces `Tenure.payload`). Build step 2's first publication named two.

| file | what it is |
|---|---|
| **`PLAN.md`** | **the improvement plan — read this first if you are about to do work.** What to build, in what order, what may not be invented while building it, and the one question for Jordan. It also **adjudicates `ARCHITECTURE_V2.md` and corrects it in three places** |
| **`ARCHITECTURE_V2.md`** | **the proposal.** Read Part A before the tables, or they look like bureaucracy |
| **`hole_register.yaml`** | **Part VII, as data** (`W0`, landed). 54 rows in §G4's shape. `python ../2026-09-01-season-loop-tests/tracer/register.py --counts` computes what Part VII's prose used to assert; `--check` fails on a row that breaks §42.2/§42.2.1 |
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
- **Part VII** — **the hole register**, replacing §61–§62's prose. ⚠ **Its self-reported counts
  — "39 holes, 8 ruled, 13 assumption, 12 absent" — DO NOT REPRODUCE, and this line no longer
  states any.** `W0` made the register data; the counts are computed:
  `python ../2026-09-01-season-loop-tests/tracer/register.py --counts`.

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
- **Nineteen holes have no row at all.** The register could not report this because **it was a
  markdown table nothing reads**, whose own counts did not reproduce from its own rows. **`W0`
  landed 2026-09-02: it is `hole_register.yaml` now, 54 rows, and `register.py --check` is what
  makes a wrong row fail.** The nineteen became **twenty-two** once §1.4's four §62/§54
  carry-overs were carried as separate rows, which is what the plan told `W0` to do.
- **The critical path is six items** — `W0 → W1 → W2 → W3 → W5 → W9` — ending at **one NPC season
  running end to end**. Everything else runs beside it.
- **Three of this chain's own rulings are overturned in `PLAN.md` §1.3**, including a "verified
  negative" that was a keyword search.
