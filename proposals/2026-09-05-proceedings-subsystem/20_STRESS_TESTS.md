# 20 · THE STRESS SUITE — thirty-eight attempts to run a proceeding, and the bill they came back with

> ## ⛔ **THIS IS A CLOSED RECORD, NOT A WORK QUEUE. READ `21_RECONCILIATION.md` FIRST.**
>
> **PHASE 0 of `21_RECONCILIATION.md` has been executed** (2026-09-07). What survived of the
> findings below is **fixed in the design files themselves** — `10_LOOPS_AND_GAPS.md`,
> `00_DERIVATION.md`, `03_PARAMETERS.md`, `08_SEAM.md`, `04_VERBS.md`, `12_BUILD_ORDER.md`,
> `19_PLAN.md` — which is what `04_CODE_ARCHITECTURE.md` §G.4.4 requires of an adversarial pass:
> **edits to the thing under review, not a register beside it.**
>
> **Nothing here is a pending item.** A session looking for what to do next wants
> `21_RECONCILIATION.md` PART D, not this file.
>
> ### ⚠ Four results below were WITHDRAWN OR DOWNGRADED after review, two of them headline
>
> | | |
> |---|---|
> | **`F-32`** | ⛔ **withdrawn.** The lane's original diagnosis was right; this suite's correction of it ran the case the rule does not cover. **Executed both ways**: with no payload, 1 claim names the speaker; with a subject named, **0** |
> | **`F-34`** | ⛔ **withdrawn as stated — and the check it called unrunnable now runs and FAILS.** `p_success` was in `sigma_leverage.py` all along. At the 1D floor the deprivation floor hits zero at **Ob 3**, and σ-leverage does not lift it |
> | **`F-14`** | **downgraded** — `19_PLAN.md` step 15 already ruled the declaring act. The row has been corrected |
> | **`F-05`** | **re-cut sharper** — `exists:DocketItem` returns `UNKNOWN`, so `speak` cannot form at all |
>
> **And three *what executes today* claims are corrected in place**: `ST-09` ran the pre-design
> `speak` row, `ST-35` is season determinism rather than a seam draw, `ST-36` permutes deliberation
> order rather than attendance.
>
> ### ⚠ Why this file was not deleted, which its own plan told me to do
>
> `21_RECONCILIATION.md` PHASE 0h says *retire the findings register*. **I narrowed that and am
> saying so rather than doing it quietly.** §G.4.4 governs an adversarial pass that creates a
> document **nobody asked for**; Jordan asked for this one — *"log all instances where you have had
> to create/invent something … log all mechanical decisions as well as gaps and conflicts and
> failures."* Deleting the logs to satisfy a rule about unrequested documents would be obeying the
> letter against the instruction. **What the rule is actually protecting against is a parallel queue
> that accumulates, and that is closed by the banner above rather than by deletion.**

## Status: **PROPOSED (2026-09-07). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Instrument: `stress/stress_proceedings.py` — executes against
## `proposals/2026-09-01-season-loop-tests/tracer/shape.py`, the tracer this directory cites by
## line number throughout. **Reproduce with `python3 stress/stress_proceedings.py`**;
## `--json` for the machine-readable run, `--md` for PARTS A–E of this file.
## Adversarial record: PART F. **Two structurally independent read-only critics attacked this
## suite's output and between them killed two findings outright, overturned a third as stale,
## voided one execution, and corrected four counts. All of it is applied and recorded in place.**

---

# THE OBJECTION THIS FILE MUST ANSWER FIRST, BECAUSE IT IS THE STRONGEST ONE

> **"The design says on every page that nothing here runs. A suite that reports *nothing runs* is
> measuring its own premise."**

**Correct, and a first draft of this file deserved the charge.** The suite does not ask *does it
run* — the answer was published before the first test was written. It asks:

> ## **WHAT MUST BE INVENTED BEFORE A SINGLE PROCEEDING CAN BE TRACED FROM CONVENING TO DISPOSAL — WHERE EXACTLY DOES THE ATTEMPT STOP — AND WHICH OF THE DESIGN'S OWN CLAIMS SURVIVE BEING EXECUTED RATHER THAN READ?**

**A fixture cannot be vague, and that is the whole method.** Prose can say *the bench is a Query
over seats whose remit covers the matter*; a fixture has to name the seat, name the remit act, name
the person holding it, and then call something. Three passes have already attacked this directory's
*arguments* (`13`, `17`, `18`). **None of them tried to instantiate one**, and instantiating is what
surfaces the class of defect that survives every reading pass — not *is this reasoning sound* but
*is there anything to call, and does what comes back fit what the next step needs.*

⚠ **AND THE COUNT OF FINDINGS IS THE WRONG NUMBER TO QUOTE.** This directory's registers are
unusually complete; twenty of the thirty-five findings restate a row it already carries. **Every
finding declares which it is**, in an *already registered?* line, together with what the execution
adds. The fifteen new ones are named at the top of PART C.

| the log | what it answers |
|---|---|
| **PART A · INVENTIONS** | everything created to make a trace possible — characters, seats, a docket, a venue, rosters, magnitudes, whole functions — **each with who owns it.** Eight are harness fixtures; **fifteen are mechanisms the design owes** |
| **PART B · MECHANICAL DECISIONS** | every place the design admits two readings and the trace had to take one, with the alternative and a falsifier |
| **PART C · FINDINGS** | gaps, conflicts and failures, each with an **evidence grade** and an **already-registered line** |
| ⭐ **PART D · THE WORKED TRIAL** | *Vellenmark v. the herdsman*, sixteen steps, each SUPPLIED / RUNS / STOPS / AMBIGUOUS |
| **PART E · THE PER-GAME MATRIX** | what each of the twelve arrangement rows is stopped by — **derived from the other tests' verdicts, not typed** |
| **PART F · THE ADVERSARIAL PASS** | what two independent critics broke in this suite, and what was done about it |

---

# THE HEADLINE

## What executes today — four things, credited in full

| | |
|---|---|
| **`ST-09`** | a `speak` by a person holding **no seat** folds, reaches RESOLVE and emits `speech.made`. Anyone may speak; there is no spectator mode; and the act writes nothing |
| **`ST-19`** | the **appeal depth cap** returns a typed `ContestError` at the cap rather than raising — `AX-6`'s nesting bound, working |
| ⭐ **`ST-35`** | **the same seeded proceeding replays identically** — 21 Events and 18 claims, twice, byte for byte. `06_RESOLUTION.md` C.5's determinism claim, run for the first time |
| ⭐ **`ST-36`** | **permuting who attends does not move the outcome.** `05_PROCEDURE.md`'s PART A grades *who attends* a MAP and its own header says *the criterion is its own falsifier: permute and compare*. Nothing in the directory had permuted anything. It holds |

## The five results that are new and survived attack

1. ⭐ **`F-14` — `disposes:` names a write and has no writer.** Every one of the twelve rows carries
   it; `14_THE_WORLD_IN_THE_ROOM.md` §E makes *what does this game change in the world* the
   governing test; `11_NERS.md`'s diagonal PASS rests on it verbatim (*"`disposes` writes a Tenure
   — a seat, a duty, a severance"*). **No verb in the table writes it.** `determine` grades a
   Tenure and cannot open one, and the draft row that would have opened it was corrected away.
2. ⭐ **`F-38` — the count table that IS the argument is stale in three of five rows.**
   `README.md` puts it at the top as *the count, which is the whole argument*. The fields cell
   still says *1, and it is contested · `Proposition.rung` … admitted with its price*, pointing at
   the section titled **THE ONE FIELD IS WITHDRAWN**, which argues about a *different* field and
   retracts rather than admits. The verbs cell says *4 new* where two other files say ZERO. The
   carriers cell lists `Seat`, which is not a carrier.
3. ⭐ **`F-37` — five gaps are registered by the files that raise them and are in the gap register
   nowhere**, including `P-24`, which `14_THE_WORLD_IN_THE_ROOM.md` calls the sharpest thing its
   hardest question surfaced. Each was written as *Registered `P-nn`* at its own site, which reads
   as done. `10_LOOPS_AND_GAPS.md` PART C quotes the discipline they fail.
4. ⭐ **`F-28` — the ladder rung is a fold over emissions and no emission can name a rung.**
   §B.2 withdrew the design's one new field on five grounds and replaced it with that fold. It is
   the mechanism the descent, the obstacle's third term and `AX-3`'s two-track separation all read.
5. ⭐ **`F-33` — under the fan-out mode in force, there is no such thing as being absent.** The
   subject who never travelled ends the season holding the same three claims as the bench member
   who sat through it. `07_THE_GAME.md` PART E's *a player can be condemned and not know it, and
   that needs no mechanism* is a claim about a sweep arm, and four structural claims rest on it.

## And the one that is a correction rather than a discovery

⭐ **`F-32`** — the design's own headline diagnosis (`18_FINDINGS.md` PART B, `HANDOFF_SC.md`) is
that *no deposit names the actor*. **A deposit does.** After a speech in front of five people, the
bench member's ledger holds `(p_party_a, speech.made, 100, firsthand)`. The defect is the deposit's
**content**, not its absence: the only claim about a speaker is that he spoke — no reading, nothing
that could be wrong, nothing that differs between two hearers — and the tracer's own comment records
that a claim about the actor *"can never raise a listener's question."* `19_PLAN.md` step 2 is aimed
one step to the left of the real hole.

## The shape of the blockage, which matters more than any count

**No arrangement row is blocked on a parameter of its own.** All twelve are stopped by needs shared
across the catalogue — the arrangement loader and the docket in every row, the bench in ten, the
disposal's writer in eleven. ⭐ **That is the closure claim holding in the only direction currently
testable** — the differences between the twelve really are data — **and it is also why the catalogue
has not yet bought anything**: twelve rows over an unbuilt structure differentiate nothing, which is
where `18_FINDINGS.md` PART J arrives from the play side.

**And the worked trial says where the specification ends.** Of sixteen steps in one legal trial,
five are supplied — **and all five are things the tree owned before this design existed**: the
calendar firing, the presence walk, the fold, the degree ladder, the permutation invariance. Ten
stop. One is ambiguous. Every step that stops is one this directory specified. That is a measurement
of how much of the design is specification, not a criticism of it being one.

---

# WHAT THE SUITE IS NOT

- **It is not a NERS pass.** `11_NERS.md` owns that; the method belongs to
  `skills/valoria-resolution-diagnostic`.
- **It did not read the study.** Fidelity to the source is `16_THE_FLATTENING.md`'s.
- **It did not build the subsystem.** No design file was edited by this work, and where a trace hit
  a hole the harness **stopped and logged the hole** rather than stubbing past it. A stand-in bench
  would have made every step below it measure my Query rather than the design.
- ⚠ **It inherits eight swept constants and declares them** (`INV-21`). Every season it runs is one
  undeclared arm of eight, and `F-33` is the finding that arm produces.
- ⚠ **Its own numbers have been wrong.** See PART F.

---
## The run

⚠ **READ THE SECOND LINE, NOT THE FIRST.** Of the 28 findings, **9 are new** and the rest restate a row the design already registers — its gap register, its adversarial record and its playability adjudication are unusually complete, and a stress report that presents their honestly-registered holes as discoveries is padding. Every finding carries an *already registered?* line saying which it is and what the execution adds. **The new ones are `F-02`, `F-05`, `F-11`, `F-14`, `F-25`, `F-28`, `F-31`, `F-33`, `F-34`.**

**38 stress tests** · **BLOCKED** 14 · **FAILED** 13 · **RAN** 11 · **28 findings** · **23 inventions** · **6 mechanical decisions**

| # | stress test | stresses | evidence | verdict |
|---|---|---|---|---|
| `ST-01` | the prize `a matter` routes to a provider | 08_SEAM.md PART B | `construction` | **BLOCKED** |
| `ST-02` | the seam can carry a venue, a matter and an arrangement together | 08_SEAM.md PART A · shape.py:6139 | `construction` | **BLOCKED** |
| `ST-03` | the bench Query answers | 00_DERIVATION.md §A.4 · 04_VERBS.md §B.2 | `construction` | **BLOCKED** |
| `ST-04` | there is an occasion to attach an arrangement to | 08_SEAM.md PART A · 03_PARAMETERS.md PART D | `no-signature` | **BLOCKED** |
| `ST-05` | a fired Date puts the matter on a docket a `speak` can name | 04_VERBS.md §B.1(ii) · 03_PARAMETERS.md §C.1.1 | `construction` | **BLOCKED** |
| `ST-06` | the design's account of when CALENDAR dockets is the code's | 03_PARAMETERS.md §C.1.1 vs shape.py:5363-5381 | `document` | **RAN** |
| `ST-07` | a party with no seat can open the case that names its own terms | 00_DERIVATION.md §A.5 (T-n) · verb_table.yaml | `construction` | **FAILED** |
| `ST-08` | the `scale:` key invariant 10 forbids actually fails the load | 03_PARAMETERS.md §C.1 · 08_SEAM.md D.2 invariant 10 | `construction` | **FAILED** |
| `ST-09` | a `speak` reaches RESOLVE and emits | 04_VERBS.md §B.1 | `construction` | **RAN** |
| `ST-10` | a `speak` that contests a matter reaches a provider | 04_VERBS.md PART C · 08_SEAM.md | `construction` | **BLOCKED** |
| `ST-11` | the four band keys the design writes against are the ladder's | 04_VERBS.md §B.1 · 09_IMPOSSIBILITIES.md row 16 | `construction` | **FAILED** |
| `ST-12` | every `requires_typed` cell names a form the grammar has AND an operand that form admits | 04_VERBS.md · rosters.yaml requires_forms | `construction` | **RAN** |
| `ST-13` | whose stance a `speak` writes | 04_VERBS.md §B.1(v) | `document` | **RAN** |
| `ST-14` | a verdict is a Tenure its determiner OPENED | 00_DERIVATION.md §A.6 | `construction` | **BLOCKED** |
| `ST-15` | an adjudicator can act AS a seat | 10_LOOPS_AND_GAPS.md P-03 | `construction` | **BLOCKED** |
| `ST-16` | two bench members determining is a MAP, not a procedure | 05_PROCEDURE.md PART A · §C | `document` | **FAILED** |
| `ST-17` | a five-party negotiation can settle | 14_THE_WORLD_IN_THE_ROOM.md §A.1 | `document` | **FAILED** |
| `ST-18` | a proceeding nobody advances can END | 05_PROCEDURE.md §B.1 | `construction` | **FAILED** |
| `ST-19` | an appeal chain terminates | 00_DERIVATION.md §A.6 · shape.py contest | `construction` | **RAN** |
| `ST-20` | the world can say WHY the subject is absent | 10_LOOPS_AND_GAPS.md P-33 | `construction` | **FAILED** |
| `ST-21` | a disposal's reach can be computed from anything but presence | 08_SEAM.md §D.3 · 03_PARAMETERS.md §B.7 | `construction` | **FAILED** |
| `ST-22` | a witnessed concession survives long enough to be worth making | 10_LOOPS_AND_GAPS.md P-42 | `probe-model` | **BLOCKED** |
| `ST-23` | the arrangement rows carry the keys the schema declares | 03_PARAMETERS.md PART D · §E.2 | `construction` | **RAN** |
| `ST-24` | the closure falsifier can see the failure it excludes | 03_PARAMETERS.md §F.3 · P-34 | `probe-model` | **FAILED** |
| `ST-25` | `matter` means one thing | CLAUDE.md §4 (idempotent in meaning) | `construction` | **FAILED** |
| `ST-26` | `release` exists, so a duty a proceeding imposes can be discharged | 04_VERBS.md §B.5 · ID-14 | `construction` | **FAILED** |
| `ST-27` | the emission a write produces is the one the design names | 08_SEAM.md §D.1 vs write_matrix.yaml | `document` | **RAN** |
| `ST-28` | the rung fold is computable from the run's own emissions | 00_DERIVATION.md §B.2 · 05_PROCEDURE.md PART C | `probe-model` | **BLOCKED** |
| `ST-29` | each of the twelve arrangement rows can be run, one row at a time | 03_PARAMETERS.md §E.2 · 07_THE_GAME.md PART F | `probe-model` | **BLOCKED** |
| `ST-30` | the thirteenth game is a data edit, as the closure claim promises | 03_PARAMETERS.md §F.1 | `construction` | **BLOCKED** |
| `ST-31` | ONE WORKED TRIAL, step by step, until it stops | the whole directory | `construction` | **BLOCKED** |
| `ST-32` | the room remembers WHO spoke | 15_WHY_IT_IS_A_GAME.md PART C · 18_FINDINGS.md | `construction` | **FAILED** |
| `ST-33` | a person who was not there does not learn what happened | 07_THE_GAME.md PART E | `construction` | **BLOCKED** |
| `ST-34` | the deprivation floor holds: a floored pool against a composed obstacle still has a chance | 06_RESOLUTION.md §B.3a | `probe-model` | **FAILED** |
| `ST-35` | the same season replays byte-identically | 06_RESOLUTION.md PART C.5 · 12_BUILD_ORDER.md | `construction` | **RAN** |
| `ST-36` | permuting who attends does not move the outcome | 05_PROCEDURE.md PART A row 5 | `construction` | **RAN** |
| `ST-37` | every gap the design registers is IN the gap register | 10_LOOPS_AND_GAPS.md PART C · §F.34 | `construction` | **RAN** |
| `ST-38` | the count table that is the design's whole argument is current | 00_DERIVATION.md §B.1 · README.md | `construction` | **RAN** |

---

# PART A · THE INVENTION LOG

**Everything that had to be created for a proceeding to be traceable at all.** The `owner` column is the load-bearing one: a character invented for a fixture is a harness artifact; a Query, a roster or a magnitude invented to get past a hole is **work somebody owes**.


## A.1 · Invented because the subsystem cannot run without it — these are the bill

| id | what was invented | why it had to be | who owns it |
|---|---|---|---|
| **`INV-09`** | a manifest row `{role: contest, provider: proceedings, prize: 'a matter'}` | without it nothing dispatches. The design specifies the row; no file in the tree holds it. | the design (step 8 of 19_PLAN.md) — and a `rosters.yaml` prize edit, which is a data change somebody must make |
| **`INV-03`** | one office `off_justice` with remit_acts [determine, convene, issue], scope_rung S, faction Crown | `bench_basis: determine` reads a remit act off a SEAT. The design specifies the Query that would find such seats and no seat to find. `remit_acts` membership is validated against `rosters.yaml`, so the acts are the roster's; the SEAT is invented. | world-gen / the political layer — but nothing in the tree creates a bench-shaped office either, so until something does, no proceeding has a bench to find even once `judging_set` is written |
| **`INV-06`** | the matter: Proposition(HOLDS, subject=p_absent, predicate='took', value='the cattle') uttered by p_party_a | `14_THE_WORLD_IN_THE_ROOM.md` §A: the matter's MOOD selects the genre. The tracer's `Proposition` carries `mood`, so this is expressible — but no act in the design creates the matter as part of opening a proceeding, and `utter` is a separate act in a separate season. | the design — `open_case` writes Record.exists/stages and never names the matter, so no step of any procedure here puts the matter before the room |
| **`INV-07`** | two `commit` edges making p_party_a and p_party_b parties | `parties` is defined as live `commit` edges to a disposition of the matter. Nothing in the design produces the FIRST commit — `commit` is a live verb, but which Proposition a party commits to at a proceeding, and when, is unspecified. | the design — `03_PARAMETERS.md` §C.2 defines the party role and no step confers it, so `bench ∩ parties`, the column the whole taxonomy rests on, has no producer |
| **`INV-10`** | a three-parameter `judging_set(w, venue, matter)` returning SEATS | no proceeding can identify who may dispose of anything without it. ⚠ This harness does NOT supply a stand-in: a stand-in bench would turn the design's first deliverable into a harness fixture and every downstream trace would then be measuring my Query rather than the design. | the design — its own §A.4 calls this 'this subsystem's first deliverable' |
| **`INV-11`** | `data/arrangements.yaml` with fifteen keys × twelve rows | the parameter space is the subsystem's central claim and has no machine-readable form. | the design (step 11 of 19_PLAN.md) |
| **`INV-12`** | a clerk act — `carry` by a person holding the case Record — between the date firing and the first speech | without it `DocketItem.matter` is None and no `speak` forms. `03_PARAMETERS.md` §C.2 lists 'clerk / recorder' as a role and gives it no step in any procedure. | the design — 05_PROCEDURE.md's nested run has no docketing step |
| **`INV-13`** | the verdict Tenure: a kind, a subject, and an act that opens it | the harness cannot trace a disposal without inventing the edge the finding IS. | the design — this is the disposal, i.e. the thing every game's `disposes:` key names |
| **`INV-14`** | nothing — ⛔ **this invention row is WITHDRAWN.** A draft claimed a proclamation channel had to be invented; `post_remit` and `chronicle` already carry `body` and `<rung kind>`. | recorded rather than deleted, because a withdrawn invention is the shape of an error this log exists to catch: it counted a mechanism as missing without opening the module that has it. | ⛔ WITHDRAWN — no owner |
| **`INV-15`** | a rung carrier: an Event payload field, a per-run local threaded through the provider, or the field §B.2 refused | the ladder is the design's central procedure and its position is stored nowhere and emitted nowhere. | the design |
| **`INV-16`** | six closed rosters — ladder rungs, interposition kinds, genres, registers, proofs, standing routes — plus speech_kinds | the parameter space's vocabulary is prose in a markdown table. | the design (step 7 and step 11 of 19_PLAN.md) |
| **`INV-17`** | two `capability` key names for `brought` and `conduct` | `06_RESOLUTION.md` §B.1 defines the pool as `brought + conduct x latitude` and names neither key, correctly (the attribute roster is IN FLUX and Jordan ruled *ignore their use of attributes*). But a trace cannot roll without them. | content by `ID-12` once the attribute roster settles — a data edit, not a decision |
| **`INV-18`** | the latitude multiplier's shape and `LATITUDE_FLOOR` | ruled 2026-09-06 to be floored near the measured ~0.7 and swept; the number and the curve are both unwritten. | the design (`19_PLAN.md` step 12) — and M-7 is a BLOCKING measurement, so this is not a fixture choice anybody may make quietly |
| **`INV-19`** | magnitudes for the four room terms (aptness · rung · register fit · proofs) | `06_RESOLUTION.md` §C.1 composes the obstacle from four signed terms and supplies no sizes. `ID-6` says inject, declare, sweep — there is nothing to inject into yet. | the design (`19_PLAN.md` step 12), and `P-25` says FOLLOW THE TRIBUNAL rather than re-derive |
| **`INV-20`** | the `reception` composition — which of the bench's claims and which conviction axes, at what weights | `15_WHY_IT_IS_A_GAME.md` makes this the one hidden term that stops the proceeding being a solved flowchart. It is the design's central claim and it is a sentence. | the design (`19_PLAN.md` step 17) — ⚠ and `HANDOFF_SC.md` already records that the set it reads cannot be populated today: no deposit names an actor, every claim is firsthand at confidence 100, `told_by` is never minted |

## A.2 · Invented to have a world at all — harness artifacts, each with what its absence says

| id | what was invented | why it had to be | who owns it |
|---|---|---|---|
| **`INV-21`** | eight swept fixture constants, adopted whole from `DEFAULT_FIXTURES` | `ledger_cap=200` · `scene_budget=5` · `fan_out_mode='total'` · `contest_max_depth=2` · `question_aggregation_rule='first'` · `claim_subject_rule='both'` · `observation_deposit_mode='actor'` · `record_stages_default=3`. **Each carries its own H-row and a declared three-point sweep**, and every season this harness runs is ONE UNDECLARED ARM of eight. `18_FINDINGS.md` states the trap verbatim: *the sweep must run against a setting that is not the current fixture, or it measures the fixture.* Named here because a suite that inherits them silently is doing exactly that. | the harness — DECLARED, not swept. Any verdict below that depends on one says so |
| **`INV-22`** | `world_seed=7`, `SUBSIST` (a subsistence model), `NOCHOOSE` (a chooser that takes nothing), and grain stores of 40 at the settlement and 8 at the hearth | the season loop will not turn without a seed, a subsistence function and a chooser, and the design supplies none of the three. `SUBSIST` is copied from the tracer's own probe harness, which declares it *the instrument's own subsistence model, INJECTED rather than invented inside the shape*. | the harness — and the note is that a PROCEEDING-shaped chooser (one that weighs row 0, the entry decision the design calls its largest lever) does not exist anywhere, so no test here can exercise the decision the design cares most about |
| **`INV-23`** | ⚠ a `manifest` installed directly on the world: `{contest: seam.contest_resolver, order: core.canonical_order}` | copied from the tracer's own fixture so the world boots. **It is worth flagging against `F-01`, which reports that no `manifest.yaml` exists in the repo**: both are true — the tracer's world carries a two-row boot manifest naming a RESOLVER, and the design's PART B row naming a PROVIDER for a prize is a different row in a different file that does not exist. A reader could otherwise take F-01 and this line as contradicting. | the harness (the boot manifest) · the design (the provider row) |
| **`INV-01`** | four venues: realm R, duchy D, settlement S, hearth Hh | `venue_min_rank` is an ordinal over `rung_kinds`, so a proceeding needs a containment ladder to sit on. No fixture, seed world or example venue exists in the design. | harness (the tracer's own `tiny_world` sets the precedent) |
| **`INV-02`** | six persons: p_bench_a, p_bench_b (bench) · p_party_a, p_party_b (parties) · p_floor (audience) · p_absent (the subject who did not travel) | `AX-1` — only a person acts — so every seat, every party and every witness must be a person before anything can be traced. The design names no character anywhere and the tree's `references/npc_registry.yaml` is out of this proposal's declared scope. | harness — BUT see PART D: the design has no worked cast for ANY of its twelve games, so before this walk no row had been instantiated even on paper |
| **`INV-04`** | presence: five of six persons `contain`-ed at S; p_absent left at Hh | `floor` = whoever travelled, and `presence` is a `contain` walk. To have a floor at all somebody must have been put in the room by the fixture, because `move` is the attendee's own act and this harness cannot make six people decide. | harness — and it is the honest form of `07_THE_GAME.md`'s entry decision: the test cannot exercise row 0 without a chooser that weighs it, which does not exist |
| **`INV-05`** | p_bench_b holds NO seat, deliberately | so the bench Query has something to exclude. A bench of one cannot test `&#124;bench&#124; > 1`, which four of the twelve rows require. | harness |
| **`INV-08`** | a Date `d_sitting` due at tick 1 with holder=p_bench_a | a proceeding CONVENES because a Date fires. `convene` writes `Date.due_at`, so a real run would need a prior season in which somebody with a `convene` remit acted; the fixture short-circuits that. | harness (short-circuit) — the verb exists and is `ruled` |

---

# PART B · THE MECHANICAL DECISIONS

**Every place the design admits two readings and the trace had to take one.** Each names the alternative not taken and what would show the choice wrong (`ID-11`: ship the falsifier with the claim).


### `MD-01` — treat the venue/matter channel as a THIRD seam amendment, not a wiring detail

- **because:** `08_SEAM.md` PART C declares two amendments (the caller's ordering; the margin producer) and this is a third of the same kind — a signature the one owner must widen.
- **the alternative not taken:** pass the matter inside `prize` (i.e. prize = the Proposition id), which the roster's prize→module map cannot then key on, since the map is keyed by prize STRING
- **falsifier:** a `contest` signature carrying `matter` and `arrangement`, with the prize still a rostered string

### `MD-02` — read the five investigation rows as UNRULED rather than as broken

- **because:** combat's three-band exemption exists BY RULING because it reads a scene rather than a margin (`rosters.yaml: combat_degree_bands`), and these five plausibly do the same. But no ruling covers them and the design does not ask for one.
- **the alternative not taken:** grade them broken outright, as §B.1 graded the coined `speak` bands
- **falsifier:** a ruling, or a `writes_at` call against one of these rows returning a band

### `MD-04` — check every gap-register row against the newer rulings before citing it

- **because:** the register at `10_LOOPS_AND_GAPS.md` predates the 2026-09-06 rulings recorded in `19_PLAN.md`, `ED-SC-0033..0035` and `HANDOFF_SC.md`, and P-15 and P-29 are both stale there. A suite that cites the register without the ledger reports settled questions.
- **the alternative not taken:** cite the register as the design presents it, which is what a draft of this suite did for P-15 while citing the ledger for the next finding
- **falsifier:** any other P-row a later ruling closed — `P-29` is the second, closed by *pool only it is*, and it is not in the register at all (see F-37)

### `MD-05` — log the collision and do not propose a rename

- **because:** `CLAUDE.md` §4 binds NEW coinage and takes a no-retrofit posture; three of the five senses predate this design.
- **the alternative not taken:** rename the prize to `a disposition` and the disputed Proposition to `the question`, which is what the corpus calls it
- **falsifier:** a session reading `contests: 'a matter'` and resolving it to `matter_kinds`

### `MD-06` — read each row's structural needs off its own YAML block in §E.2

- **because:** a row's needs are what its keys imply — `disposal: bench` needs a bench, `|bench| > 1` needs a quorum, `appeal_basis: determine` needs a fed cap.
- **the alternative not taken:** score every row against every need, which would make the matrix a constant in the other direction and say nothing about the rows
- **falsifier:** a row whose YAML implies a need this reading omits — the parliament's `proofs: []`, for instance, arguably needs nothing of the forensic machinery and is scored here as needing the disposal writer only

### `MD-07` — inject a declared obstacle set rather than refuse the measurement

- **because:** `ID-6` says inject, declare and sweep an `assumption`-grade magnitude rather than escalate it, and `06_RESOLUTION.md` grades the four room terms exactly that. The injected set is: base_Ob = 3 (an opposition score of 6), and the four terms each in [-1, +2], giving a maximum composed Ob of 11 against the 1D floor.
- **the alternative not taken:** refuse, on the grounds that the design supplies no numbers — which is what a draft of this suite did, and it left the design's own BLOCKING check unrun on the grounds that it was blocked
- **falsifier:** a ruled magnitude set that differs from this one, at which point this measurement is re-run rather than argued with

---

# PART C · THE FINDINGS — gaps, conflicts and failures

Ranked by severity, then by id. **`by=` is the evidence grade** and it is the column to read first: `construction` means the tracer, a loader, a roster or a law refused — that is evidence. `no-signature` means there was nothing to call, which *is* the refusal but is weaker, because absence is not a guard. `document` means two surfaces in the tree disagree. `probe-model` means this harness supplied a model the design does not, to reach the question at all — **discount those accordingly.**


## C.1 · BLOCKING (9)


### `F-01` · the proceedings prize is declared in no roster, so the seam cannot reach the subsystem even in principle

> **`by=construction`** · site: `08_SEAM.md PART B`
>
> **already registered?** the design's own `08_SEAM.md` PART B — it specifies the row and says the prize is new rather than claimed. **ADDS: the execution, and that no `manifest.yaml` exists anywhere**

`contest_subsystem('a matter')` returns None. `rosters.yaml: contest_subsystems.prizes` declares ['a field', 'a proposition', 'a standing', 'the body'] and no `manifest.yaml` exists anywhere in the repo. `08_SEAM.md` PART B specifies the row and deliberately does NOT claim the two `social_contest` rows, so today a `speak` that contests `a matter` falls through to the generic `Unspecified('the degree ladder's margin model')`.

### `F-02` · the seam's own dispatch cannot pass a proceeding its venue AND its matter, because both ride on one `payload` field of two incompatible types

> **`by=construction`** · site: `08_SEAM.md PART A`
>
> **already registered?** NEW — no register row covers the seam's inability to carry a matter or an arrangement

`contest(...)` takes ['w', 'rung', 'prize', 'claimants', 'depth', 'max_depth', 'causes', 'extension'] — there is no `matter`, no `arrangement` and no `attendees` parameter. The fold builds the call at shape.py:6137 as `rung=(a.payload if isinstance(a.payload, str) else None) or 'R'`, and the SAME `payload` must be a dict to carry `subject` (the second claimant). So an act that names its opponent CANNOT name its venue: every contested act with a dict payload is dispatched at the REALM. `08_SEAM.md` writes `proceedings.run(proj, place, claimants, depth, max_depth)` and then reads `occasion_at(proj, place).arrangement` and `judging_set(proj, place, matter)` inside it — `matter` is closed over from nowhere. The design's §C.1 amendment (the caller's ordering) is stated; this one is not stated at all.

### `F-03` · the bench does not exist: `Query.judging_set` raises unconditionally, and the design's replacement takes a parameter the live signature has no room for

> **`by=construction`** · site: `shape.py:3161`
>
> **already registered?** `00_DERIVATION.md` §A.4 (*this subsystem's first deliverable*) + `04_VERBS.md` §B.2. **ADDS: the raise as an execution**

live signature ['w', 'rung_id'] — two parameters. The design specifies `judging_set(w, venue, matter)` and argues the third is REQUIRED, not convenient (`04_VERBS.md` §B.2). The tracer raises: [UNSPECIFIED] judging_set_rule  @S61  needs: who decides at a sitting. Everything downstream of the bench — `disposal: bench` in 10 of 12 rows, `genre` (derived from the bench's remit), `bench ∩ parties` (the column the taxonomy rests on) — is unreachable until this function is written.

### `F-05` · the docket item CALENDAR appends carries `matter: None`, so `speak`'s only precondition can never be satisfied by convening alone

> **`by=construction`** · site: `04_VERBS.md §B.1`
>
> **already registered?** NEW — the docket's content was never checked

after two seasons the date has fired (True) and the docket holds [{'date': 'd_sitting', 'matter': None}]. `speak`'s `requires_typed` is `{form: existence, of: subject, kind: DocketItem}`, and CALENDAR (shape.py:5378-5380) writes `{'date': did, 'matter': None}`. The only writer of `DocketItem.matter` in the 32-row verb table is `carry`. ⚠ **AND THE TYPED CELL AND ITS OWN PROSE DO NOT AGREE, WHICH IS THE SHARPER HALF.** The prose `requires` reads *a live occasion at the actor's venue **whose docket names the subject***; the typed form is a bare existence test that binds the act's `subject` and asks whether it exists as a `DocketItem`. **A docket item with `matter: None` satisfies the typed cell and fails the prose.** So `speak` either has a precondition that is unsatisfiable until somebody carries the papers, or one that is satisfied by an empty sitting — and which it is depends on which half of the row a reader takes as the mechanism. Under `CLAUDE.md` §0.05 the typed cell is the mechanism and the prose is reference, so the *empty sitting* reading wins and the design's own account of what `speak` is for does not. ⛔ **A DRAFT OF THIS FINDING CLAIMED THE CELL REQUIRES THE MATTER AND CONCLUDED A CLERK IS MANDATORY. It does not, and the retraction is recorded.** The clerk is still the thing nobody has: `03_PARAMETERS.md` §C.2 lists *clerk / recorder* as a role and no procedure gives it a step, so the docket in practice never names a matter.

### `F-10` · a contested `speak` stops at the seam with no provider and no margin

> **`by=construction`** · site: `08_SEAM.md PART C.2`
>
> **already registered?** `08_SEAM.md` PART C.2, the design's own second declared amendment. **ADDS: the execution**

the fold dispatched and the seam refused: [UNSPECIFIED] the degree ladder's margin model  @S39.4  needs: a margin -- pool, obstacle, and the four band edges read off it. This is the design's own `08_SEAM.md` PART C.2 stated as an execution: the margin-graded branch has a reader (`degree_of` recognises `net`/`ob`) and NO PRODUCER, and this subsystem was to be the first. It is not one yet.

### `F-14` · `determine` can GRADE a Tenure and cannot OPEN one, so the verdict the whole `AX-6` argument rests on has no producer

> **`by=construction`** · site: `00_DERIVATION.md §A.6`
>
> **already registered?** NEW — and it is the strongest finding here

`determine.writes` = ('Tenure.degree',). `00_DERIVATION.md` §A.6 is explicit that a verdict is *'a `Tenure` the determiner opened, closable by `T-o`'*, and that this is what gives the appeal for free. Opening a Tenure is `Tenure.since`, which `determine` does not write — `commit`, `oblige`, `confer`, `succeed` and `tie / knot` do. `04_VERBS.md` §B.2 then adds *'⚠ UNCHANGED from the live row'* and corrects a draft that had proposed `[Tenure.degree, Tenure.since, Tenure.until]` — i.e. the draft that WOULD have opened the verdict was corrected into one that cannot. ⚠ So: WHICH Tenure does a finding grade? The design never says. If it grades the loser's existing `hold`, the finding is a number on somebody else's edge and the non-owner objection of §B.2 applies verbatim. If it grades a new one, nothing opens it. ⭐ AND THE SHARPER FORM IS ABOUT THE KEY, NOT THE VERB: `disposes:` NAMES A WRITE AND HAS NO WRITER. Every one of the twelve rows carries `disposes: <tenure> | Record | oblige | none`; `14_THE_WORLD_IN_THE_ROOM.md` §E makes *what does this game change in the world* the governing test; and NOTHING IN THE DESIGN CONNECTS THE KEY TO ANY ACT'S `writes` COLUMN. That is `ID-13` — find a key a reader or remove it — applied to this design's most load-bearing key. ⚠ And `11_NERS.md`'s diagonal PASS rests on it verbatim: *'`disposes` writes a Tenure — a seat, a duty, a severance — which is a strategic object'*. It does not write one, and no verb in the table does.

### `F-15` · `Act` has no `via`, so the one thing that makes an adjudicator's act a SEAT'S act is unrepresentable — and the design's own `requires` cell for it was already retracted once for naming an operand outside the roster

> **`by=construction`** · site: `04_VERBS.md §B.2`
>
> **already registered?** `P-03` / `H-108` on the `via` half. **ADDS: the tribunal `interposed: [office]` discount and the verdict's authorship as sites that depend on it and are not marked blocked by it**

Act fields = ['id', 'actor', 'verb', 'changes', 'reads', 'contests', 'payload', 'stratum', 'obstacle', 'pool', 'scene']. `requires_operands` = frozenset({'actor', 'from', 'to', 'site', 'amount', 'floor', 'kind', 'subject'}) — no `via`. The design registers this as `P-03` / `H-108` and then relies on it in four places that are not marked as blocked by it: the verdict's authorship (`AX-6`), `T-o`'s revocation gate, the tribunal's `interposed: [office]` discount, and `03_PARAMETERS.md` §C.2's whole adjudicator row (*'holds a seat … and acts **via** it'*). Without `via`, an adjudicator's determination is indistinguishable from a private opinion by the same person, which deletes the difference between the bench and the floor.

### `F-33` · the absent subject learns everything, because the fan-out mode that is the specified behaviour deposits to EVERYONE regardless of presence

> **`by=construction`** · site: `07_THE_GAME.md PART E`
>
> **already registered?** NEW — `19_PLAN.md` step 1 proposes the fix without noting that four structural claims depend on the arm

fan-out mode = 'total' (`H-33`'s control and the tracer's declared default). After the sitting, p_absent — contained at the hearth, never at the venue — holds 3 claims against the attending bench member's 3. `observers_for` returns `list(everyone)` at this mode with no presence predicate. ⭐ So the design's most-quoted *needs no mechanism* claim — *a player can be condemned and not know it* — is **false under the current fixture and true under a different arm of a sweep that has not been run.** `H-33`'s other two arms (`presence_only`, `all_five`) would make it true. ⚠ This is exactly what `19_PLAN.md` step 1 (*take fan-out off `total`*) is for, so the design KNOWS the arm is wrong; what it does not say is that four of its own structural claims — trial in absentia, the closed floor, the covert approach, and *finding out too late is the game* — are claims about a sweep arm rather than about the architecture. Under `total` there is no such thing as being absent.

### `F-34` · ⛔ THE DEPRIVATION FLOOR IS VIOLATED, AND THE σ-CHANNEL REMEDY THE DESIGN NAMES FOR IT DOES NOT REACH THE FLOOR

> **`by=probe-model`** · site: `06_RESOLUTION.md §B.3a`
>
> **already registered?** NEW — `M-7` is registered as a blocking measurement and had never been run. The prediction is the design's own; the number, the crossing point and the refutation of remedy (a) are not

⛔ **RETRACTION FIRST.** A draft of this test reported the check unrunnable because *the ladder module exports no `p_success`*; it searched `dice_engine.py` alone, and `p_success` is in `engine/autoload/sigma_leverage.py` — the resolver `06_RESOLUTION.md` PART C is written against by name. **The design's own BLOCKING check was called unrunnable and was runnable the whole time.** It has now been run. ⭐ **AND IT FAILS.** §B.3a requires that *at the minimum lawful pool against the maximum plausible composed obstacle, `p_success` must not be effectively zero*. At the 1D pool floor: {"Ob 1": 0.2266, "Ob 2": 0.0228, "Ob 3": 0.0006, "Ob 4": 0.0, "Ob 5": 0.0, "Ob 7": 0.0, "Ob 11": 0.0}. **It reaches zero at Ob 3** — not at some exotic maximum, but at a value `base_Ob = opposition_score / 2` alone produces against an opposition score of 6, before a single one of the four room terms is added. ⚠ ⭐ **AND REMEDY (a) IS REFUTED BY MEASUREMENT.** §B.3a offers two: *(a) the σ-channel must be REACHABLE in that room — advantage must be buyable there — or (b) the obstacle takes a ceiling.* Buying σ-leverage at the floor against Ob 7 gives {"net_\u03c3 0": 0.0, "net_\u03c3 1": 0.0, "net_\u03c3 2": 0.0, "net_\u03c3 3": 0.0} — **the uniform channel the design leans on throughout is uniform in Δz and cannot lift a probability that is already zero.** `06_RESOLUTION.md` §B.3a item 3 calls it *the engine's own answer to this exact problem*; at the floor it is not an answer. **So (b) — a ceiling — is the only one of the two remedies that can work**, unless the pool floor rises. ⚠ **What is NOT claimed.** The magnitudes are `MD-07`'s injected set, not a ruling, and the 1D floor is the pathological pool rather than the typical one: with `latitude` floored near the measured 0.7, a real pool is `brought + 0.7 × conduct` and exceeds 1 for anyone with any preparation at all. Against Ob 11 the pool sweep reads {"pool 1": 0.0, "pool 4": 0.0, "pool 9": 0.001, "pool 16": 0.0753}, so the room is survivable with a dossier and not without one — **which is `§B.3a`'s *preparation game* working exactly as it says, and simultaneously the case its own floor forbids.** The design predicted this shape in the same section: *the obstacle is floored at 1 and CEILINGED AT NOTHING … the shape that would break the ruling is a composed obstacle growing without bound against a floored pool.* **This is that shape, measured.**

## C.2 · MATERIAL (18)


### `F-04` · every function `08_SEAM.md`'s own pseudocode calls is absent, and the arrangement file it reads does not exist

> **`by=no-signature`** · site: `03_PARAMETERS.md PART D`
>
> **already registered?** `03_PARAMETERS.md` §F.3 self-grades the closure claim `STATUS: HYPOTHESIS`. **ADDS: the count of absent signatures**

absent from the tracer: ['occasion_at', 'present_at', 'attendees_at', 'arrangements', 'latitude', 'reception', 'genre_of']. `Query.presence(w, rung)` exists and is the only one of the seven with a live analogue. No `arrangements.yaml` anywhere in the repo (0 matches). So the twelve games are twelve YAML blocks inside a markdown file — which under `CLAUDE.md` §0.05 is REFERENCE, not mechanism, and is the exact grade `04_VERBS.md` §B.3 applies to the six investigation acts when it says a prose table means they do not exist. The same test applied to this design's own parameter space returns the same answer.

### `F-07` · `open_case` is `remit:determine`, so in the games with no bench NOBODY CAN OPEN THE CASE — and with it, nobody can declare the term, the stages or the appeal cap

> **`by=construction`** · site: `04_VERBS.md PART A`
>
> **already registered?** `00_DERIVATION.md` §B.2 objection 3 (five games have no `open_case`). **ADDS: that those five therefore have no term, no stages and no depth cap**

`open_case` eligibility = ['remit:determine']. `00_DERIVATION.md` §A.5 and §A.6 hang four mechanisms on the opening act: the declared term that ends a proceeding nobody is advancing (`T-n`), the stages, the named arbiter, and the appeal DEPTH CAP whose absence of a default is a stated invariant (`H-87`). §B.2 objection 3 already notices that FIVE of the twelve games have no `open_case` — negotiation, public debate, audience, interrogation, negotiation-by-envoys — and uses it as an argument against a field. It is a much larger problem than that: those five games have NO TERM, NO STAGES and NO DEPTH CAP, and `05_PROCEDURE.md` §B.1 lists 'the declared term matures' as one of only four things that can end a run. Two of the remaining three (the depth cap, the foot of the ladder) also come from the opening act or from a bench. In a negotiation the ONLY termination condition left is 'nobody acts'.

### `F-08` · the key the design corrects is live, the loader ACCEPTS it, and the ordinal that replaces it has no operand to name the venue

> **`by=construction`** · site: `03_PARAMETERS.md §C.1`
>
> **already registered?** `03_PARAMETERS.md` §C.1 + `08_SEAM.md` D.2 invariant 10 both say the key must go. **ADDS: that the loader does not refuse it, so the invariant is unimplemented; and that the replacement needs a `venue` operand the closed roster lacks**

`convene` carries `scale: 'settlement'` at `verb_table.yaml:138` (present: True), and the tracer's loader parsed it into a live `VerbRow.scale` = 'settlement' without complaint. So `08_SEAM.md` D.2 invariant 10 — *a `scale:` key fails the load* — is a specified invariant with **no implementation**, and Jordan's 2026-09-05 correction is unexecuted rather than already applied. ⚠ **AND THE REPLACEMENT IS NOT EXPRESSIBLE**: `rank(venue.kind) > rank(person)` needs `venue` as an operand and `requires_operands` = frozenset({'actor', 'from', 'to', 'site', 'amount', 'floor', 'kind', 'subject'}) has none; the nearest member is `site`, a different carrier. `rung_kinds` IS ordered, so the comparison exists — it has nothing to compare. **The correction is one roster member away and the design does not say so.**

### `F-11` · `speak` uses the ruled four-band ladder and the five investigation rows use NINE band names of their own, in the same directory that calls a second ladder its weak point

> **`by=construction`** · site: `04_VERBS.md §B.3.2`
>
> **already registered?** NEW — §B.1 retracts the coined bands for `speak` and leaves the five investigation rows

the tree's ladder labels = ['Overwhelming', 'Success', 'Partial', 'Failure'] (speak matches: True). `04_VERBS.md` §B.3.2 keys the five investigation rows on ['Found', 'Glimpsed', 'Misread', 'Nothing', 'Partial', 'Read', 'Seen', 'Sound', 'Wrong'], of which 8 are not the ladder's: ['Found', 'Glimpsed', 'Misread', 'Nothing', 'Read', 'Seen', 'Sound', 'Wrong']. ⚠ `Partial` IS the ladder's third band and appears in two of the five rows, so a draft's *none of them the ladder's* was wrong by two. ⭐ EXECUTED: the row RAISED on the ladder's own band: [UNSPECIFIED] 'examine' has no `writes` branch for degree 'Success'. Declared: ['Found', 'Nothing', 'Partial']. An unlisted degree RAISES rather than defaulting. Three bands per row, none of them the ladder's, in three different vocabularies (Found/Partial/Nothing · Read/Misread/Nothing · Sound/Wrong/Nothing · Seen/Glimpsed/Nothing). §B.1 retracts exactly this defect for `speak` — *'every `speak` would have raised at the first fold'* — and leaves it standing in the five rows on the next page. `writes_at`/`emits_at` raise on any undeclared degree, so if these five ever route through a margin-graded contest they raise identically. ⚠ The narrower reading, which the design does not state: they contest against something (`retention`, `obstinacy`, concealment) and are three-band, so either they are NOT margin-graded — in which case they need combat's kind of ruled exemption and do not have one — or they are, and they are broken.

### `F-16` · the quorum is RULED, not open — what is unbuilt is a ruled thing, and six rows wait on it

> **`by=document`** · site: `10_LOOPS_AND_GAPS.md P-15`
>
> **already registered?** ⛔ `P-15` — **and P-15 IS CLOSED** by `19_PLAN.md` step 15 and `ED-SC-0034`. **ADDS: that the register row is stale, and that the ruled shape needs a declaring act no verb supplies**

⛔ **RETRACTION.** A draft said *`P-15` calls a quorum 'not built' and 'a ruling on whether majorities are wanted'* and regraded it a build blocker. `19_PLAN.md` says **`P-15` closes**, and `ED-SC-0034` (status `ruled`, `needs_jordan: false`) records Jordan's *'of course we accept those shapes'* — the multilateral tally and the debate score land, and conclaves, votes and majority verdicts come into range. The row at `10_LOOPS_AND_GAPS.md` P-15 is the **stale surface**, and it is stale in the register the design points a reader at first. ⭐ **WHAT SURVIVES, AND IT IS NARROWER AND STILL WORTH SAYING**: the ruled shape — a Query over the bench's live determinations, read by a LATER declaring act — means the disposal of a multi-member bench needs *a further person to act*. `05_PROCEDURE.md` §A grades the bench's determinations a MAP on the ground that *two determinations do not read each other*, which stays true; but the finding they produce is then nobody's until somebody declares it, and **no verb in this design declares a tally**. So the ruling is landed and its verb is missing, which is `ID-14` in the same shape as F-14. ⚠ And the stale P-15 row is itself the finding a reader should act on: the gap register is the first thing `README.md` sends you to.

### `F-17` · `disposal: mutual` is defined over two parties and the game's own headline case — a peace conference — has five

> **`by=document`** · site: `03_PARAMETERS.md §E.2`
>
> **already registered?** `P-15` / `19_PLAN.md` step 15 / `ED-SC-0034` / `17_PLAYABILITY.md` PART F row B-6. **ADDS: nothing; it is the ruling restated**

the design says so itself and then leaves the row: *'a multilateral treaty does not work. `disposal: mutual` is defined over TWO parties'*. `19_PLAN.md` step 15 proposes the fix (a Query read by a declaring act) and `ED-SC-0034` records Jordan accepting the multilateral tally. So this is RULED and unbuilt rather than open — but until it is built, the negotiation row is a two-body row and the design's catalogue does not say so.

### `F-18` · `Tenure` has no `term` — but `Record` already carries `ttl`, `stages` and a `term.matured` emission, and the design never considers it

> **`by=construction`** · site: `10_LOOPS_AND_GAPS.md P-04`
>
> **already registered?** `P-04` on the first half. **ADDS: the `Record` carrier the design never considered, and a matrix row for a field the class does not have**

Tenure fields = ['id', 'subject', 'object', 'kind', 'since', 'until', 'degree', 'payload'] (no `term`; `P-04` grades this `absent`, no default). Record fields = ['id', 'rung', 'kind', 'forgery_quality', 'subject_matter', 'ttl', 'stages']. Record matrix rows = [('Record', 'exists', ['RES'], '`record.created` · `record.destroyed`'), ('Record', 'forgery_quality', ['RES'], '`record.forged`'), ('Record', 'matured', ['MAT'], '`term.matured`'), ('Record', 'stages', ['RES'], '`record.staged`'), ('Record', 'ttl', ['MAT'], '`record.expired`')]. `open_case` writes `Record.exists` and `Record.stages` — it is ALREADY the act that opens the case document — and the matrix declares `(Record, matured)` at MATTER emitting `term.matured`, plus `(Record, ttl)` at MATTER emitting `record.expired`. That is `T-n`'s shape — *MATTER matures what an act wound, citing the act that wound it* — sitting on the carrier the opening act already writes. The design instead specifies a NEW `Tenure.term(matures_at, declared_by, closer)` field, which `19_PLAN.md` step 22 calls *'the one new field in the whole plan'*. ⚠ The five-test order in `CLAUDE.md` §0 puts *answered by precedent* fourth and it fires here: the summons's return day may need no new field at all. ⚠⚠ AND `(Record, matured)` IS IN THE MATRIX AND NOT ON THE CLASS — a matrix row for a field that does not exist, which is its own defect and which is why nobody noticed the carrier was available.

### `F-19` · the depth cap WORKS and nothing can supply it, because the act that declares it cannot be taken in five of the twelve games

> **`by=construction`** · site: `00_DERIVATION.md §A.6`
>
> **already registered?** `00_DERIVATION.md` §A.6 (*the mechanism is built; nothing has fed it*). **ADDS: the `ContestError` as an execution**

`contest(depth=2, max_depth=2)` returned ContestError('max_depth reached', depth=2, max_depth=2) — a typed refusal, not a raise, exactly as `00_DERIVATION.md` §A.6 and `H-87` require. Below the cap the call still stops: Unspecified: [UNSPECIFIED] the degree ladder's margin model  @S39.4  needs: a margin -- pool,. The mechanism is built and unfed. And the FEED is the problem: §A.6 rules that the cap *'is declared by the act that opened the case'*, `open_case` is `remit:determine` (F-07), and `appeal_basis: determine` appears in five rows — so the number of appeals a matter admits is set by an act the appellant cannot take and, in the five bench-less games, nobody can take at all. ⚠ **And this harness supplies `max_depth` itself** (INV-21, `contest_max_depth=2` from the tracer's fixtures), which is what let the cap be exercised at all — so *nothing supplies it* means nothing IN THE DESIGN does, not that the parameter is unreachable.

### `F-20` · contumacy and incapacity are the same state, and in canon and common law the first IS the finding

> **`by=construction`** · site: `03_PARAMETERS.md §C.1.1`
>
> **already registered?** `P-33`, which already names `evade / defy` and the return day. **ADDS: that `floor: closed` + `admitted:<basis>` is the third case and is already a key the design carries**

presence at S = ['p_bench_a', 'p_bench_b', 'p_floor', 'p_party_a', 'p_party_b']; the subject is absent = True. The world knows only that a `contain` edge points elsewhere. `P-33` names the four cases — declined · could not · was not admitted · did not know — and grades the collapse *a RULING*. Two of the four are already expressible and the design does not use them: **was not admitted** is `floor: closed` plus `admitted:<basis>`, a key it already carries; **declined** is `evade / defy` against a summons, a live verb (`writes: ()`) that needs a summons with a return day, i.e. F-18. So P-33 is not one ruling — it is one ruling (did-not-know vs could-not) plus two wirings the design already owns and did not connect. ⚠ And the excommunication row's boast — *'there is NO `subject_absent` key, and that is the result'* — is only true for the case where absence is uninformative. Where contumacy is the finding, the absence must be READ, and nothing reads it.

### `F-21` · the two channels that would carry `body` and `<rung kind>` already exist and neither fires — one because no verb emitting a proceeding's disposal has a typed `requires`, the other because nobody holds the matching remit

> **`by=construction`** · site: `08_SEAM.md §D.3`
>
> **already registered?** `P-43`, closed 2026-09-06 by `disposal_reach`. **ADDS: that the two channels which would implement it exist and do not fire, and a RETRACTION of this suite's own draft claim that they do not exist**

⛔ **RETRACTION.** A draft of this finding said the reach *needs a SIXTH channel* and graded it `construction` without opening the five. It is false: `_ch_post_remit` walks a person's live `hold` Tenures for an office whose `remit_acts` intersect the emitting verb's `remit:` eligibility, **with no presence test at all** — which is `08_SEAM.md`'s `body` reach exactly — and `_ch_chronicle`'s own docstring says *when it fires it fires for everyone alive*, which is the `<rung kind>` case at its widest. **The mechanism `disposal_reach` needs is closer to free than either the design or the draft said.** ⭐ **THE CORRECTED FINDING IS ABOUT FIRING, NOT ABOUT EXISTING.** On a `tenure.opened` Event in this fixture the five channels select: {"co_located": ["p_bench_a", "p_bench_b", "p_floor", "p_party_a", "p_party_b"], "post_remit": [], "chronicle": ["p_absent", "p_bench_a", "p_bench_b", "p_floor", "p_party_a", "p_party_b"], "witness_key": ["p_bench_a"], "document_key": []}. `chronicle` is an EVENT-KIND filter over verbs the fold can resolve, and the tracer's own comment records that *the eight `binding_decision` verbs all have prose `requires:` and none is in `REQUIRES_PREDICATES`*, so it matches nobody — and `determine`, the verb that disposes, is one of those eight. `post_remit` needs somebody holding the remit the emitting verb requires. **So the reach has carriers and no traffic**, and closing `P-43` on `disposal_reach` was right about the shape and has not been tested against the channels that must carry it.

### `F-22` · the ledger cap is the only bound on the design's one amplifying loop and nothing has measured it

> **`by=probe-model`** · site: `10_LOOPS_AND_GAPS.md P-42`
>
> **already registered?** `P-42`, which already carries the cap, the eviction key, *nothing has measured it*, and the instrument. **ADDS: nothing. Kept only because ST-22 declined to run an instrument the harness holds**

`ledger_cap` = 200, evicting on `(confidence, recency)`. `L-1` (standing → reception → outcome → standing) is signed `+` and three of its four bounds are properties of the corpus rather than columns. The design's answer to 'does a concession stay paid' is `P-42`, open. This harness cannot settle it — a seeded multi-season run with one recurring bench is the instrument and it does not exist — but it can name why it matters HERE rather than generally: a proceeding is the heaviest depositor in the game (one occasion, many witnesses, many deposits), so a proceedings subsystem is what makes the cap bind. The subsystem that stresses the bound is the one shipping without measuring it.

### `F-24` · the design's own falsifier greps for a literal the provider will never write, while the provider must branch on six enums totalling ~19 values

> **`by=probe-model`** · site: `03_PARAMETERS.md §F.3`
>
> **already registered?** `P-34` (*the closure falsifier cannot see the failure it excludes*) + `P-08`. **ADDS: nothing measured — the branch count is hand-typed, which is the defect the finding faults**

`test_no_branch_on_arrangement.py` is specified as a scan for `arrangement.id == '<literal>'`. The provider never needs one: it needs {'order': 5, 'disposal': 3, 'floor': 3, 'verdict_reasons': 2, 'stakes_grade': 3, 'disposal_reach': 3} = ~19 value-branches on OTHER keys. `P-34` records this ('the closure falsifier cannot see the failure it excludes') and grades it *pending edit*. Restated as an execution claim: the twelve games are twelve rows in the sense that no code says the WORD 'tribunal', and they are not twelve rows in the sense the headline implies, because `order: scripted` and `order: rank` are two different sequencing mechanisms that a provider must implement separately. ⚠ `P-08` already concedes the sharpest instance — `order: rank` needs the fold's canonical sort changed for everybody — and grades it `absent`. A key whose value requires amending a shared mechanism is not a parameter of this subsystem.

### `F-26` · `release` is still absent, so every `oblige` a proceeding imposes is closable only by the person who did not open it

> **`by=construction`** · site: `04_VERBS.md §B.5`
>
> **already registered?** `09_IMPOSSIBILITIES.md` row 8, which already self-grades CONVENTION *only once `release` exists. Today it does not*. **ADDS: nothing**

`release` in the verb table: False. Verbs writing `Tenure.until` = ['confer', 'kill / wound', 'move', 'repudiate', 'revoke'] — `repudiate` (`own`), `revoke` (`remit:revoke`), `confer` (`remit:confer`), `move` (containment). So a penance, a surety or a term of service imposed by a finding can be ended by `repudiate` — which is REPUDIATION, publicly, not discharge — or by a seat-holder revoking. `ID-14` (what an act opens, an act must close) is therefore unmet for the design's own principal output, and `09_IMPOSSIBILITIES.md` row 8 already grades itself CONVENTION for this reason: *'only once `release` exists. Today it does not.'* ⛔ **A DRAFT READ `04_VERBS.md` PART A's '⭐ LANDED' AS A CLAIM THAT THE ROW IS IN THE TREE. IT IS NOT ONE** — the same table cell reads *'⚠ DOES NOT EXIST IN THE TABLE'*, and 'landed' means landed in this proposal, whose complete replacement row is written out at §B.5. The retraction is recorded; the draft read the second word of a two-word cell. ⭐ **What survives is worth keeping and is smaller**: the row is written, it is the cheapest thing in the directory to ship, `ID-14` cannot hold without it, and it is ⛔ **AND A DRAFT ADDED THAT IT IS ABSENT FROM `12_BUILD_ORDER.md`'s buildable-today list. THAT IS FALSE**: `release` is **step 3**, with its dependency column reading *nothing* and its execution artifact written out (*loader invariant 6 is satisfiable for the first time; a person resigns an office*). So the plan has it, costed at zero, and nobody has run the plan — which is a statement about execution and not about the design, and is why this is `material` rather than `blocking`.

### `F-28` · the ladder rung is a fold over `matter.*` emissions and NOTHING IN THE EMISSION SAYS WHICH RUNG

> **`by=probe-model`** · site: `00_DERIVATION.md §B.2`
>
> **already registered?** NEW — §B.2 replaced a retracted field with this fold and nothing checked that the fold has an operand

`00_DERIVATION.md` §B.2 replaces the retracted `Tenure.degree` with `rung(run) := the lowest rung any emitted matter.* Event in THIS run has named`. `speak` emits four kinds — `matter.carried`, `matter.advanced`, `matter.held`, `matter.turned` — and NONE of them names a rung. `Event` carries `(id, kind, subject, changes, causes, emitted_at, degree, observed)`; there is no payload for 'procedural' or 'quality'. So the fold has nothing to fold: either the rung goes in the Event kind (`matter.advanced.at_definition` — which multiplies the declared kind roster by four and breaks invariant 7's derivation), or in `subject` (which is the actor, set by the fold), or a field is added after all — which is the conclusion §B.2 spent five objections avoiding. ⚠ **AND THE TRILEMMA OMITS A FOURTH OPTION THAT COSTS NOTHING, WHICH IS WHY THIS IS GRADED `material` RATHER THAN `blocking`**: the fold already keeps `self.resolved` and `act_of` (Event id → the Act that emitted it), and `Act.payload` is a free dict. A per-run local that reads the run's own acts needs no field, no Event kind and no ruling — and `ED-SC-0034` licenses exactly that (*per-proceeding aggregates that die with the run are FREE*). So the gap is a specification gap rather than an architectural one. What stands is that §B.2's replacement is stated as a fold over EMISSIONS, the emissions cannot carry it, and nothing in the directory noticed. ⚠ This is the load-bearing consequence: the rung is what the descent mechanism, the obstacle's third term, and `AX-3`'s two-track separation all read. `P-32` already grades the `track` column *read by nothing*; this is the same hole one level down, and it means the ISSUE LADDER — the design's central procedure — has no state.

### `F-29` · no arrangement row can be run, and every row is blocked BEFORE it reaches anything that distinguishes it from its neighbours

> **`by=probe-model`** · site: `03_PARAMETERS.md §E.2`
>
> **already registered?** aggregates `P-03`, `P-08`, `P-15`, `P-33`, `P-42` and the findings above. **ADDS: the shape — that the blockers are shared rather than per-row**

runnable rows: none of 12. **Needs shared by ALL twelve rows: ['arrangement', 'docket', 'reach']** — the arrangement loader and the docket, neither of which is about any particular game. Adding the near-universal ones (the bench: 10 of 12; the disposal writer: 11 of 12; the reach: 12 of 12) gives the result: **not one game is blocked on a parameter of its own.** ⭐ That is the closure claim holding in the only direction currently testable — the differences between the twelve really are data — **and it is also why the catalogue has not yet bought anything**: twelve rows over an unbuilt structure differentiate nothing, and the design's own `18_FINDINGS.md` PART J reaches the same place from the play side (*three of the twelve have no distinct play as the code stands*). ⚠ **NOT counted here: `public debate`**, which `14_THE_WORLD_IN_THE_ROOM.md` §E.3 retires as *not a twelfth game but what a proceeding degenerates to when nobody can dispose*. Scoring it as a blocked game would have inflated the denominator with a row the design itself withdrew.

### `F-30` · the design's five closed rosters and its speech-kind roster do not exist, so 'adding a game is a data edit' has no data to edit

> **`by=construction`** · site: `03_PARAMETERS.md §F.1`
>
> **already registered?** `03_PARAMETERS.md` §F.3 self-grades `STATUS: HYPOTHESIS`. **ADDS: that six named rosters do not exist, so the claim cannot be tested by a small step**

absent from `rosters.yaml`: ['proofs', 'registers', 'interposition_kinds', 'speech_kinds', 'ladder_rungs', 'standing_routes', 'genres']. `00_DERIVATION.md` §B.1 counts *'rosters: 5 closed sets, in data — ladder rungs · interposition kinds · genre · register · standing route'*, and §B.1.1 adds a sixth (`speech_kinds`). None is in the data. §F.1's examination — the thirteenth game, offered as the proof that the space is closed — turns on `proofs` gaining a `performance` member and says *'it is a roster edit, not a code change, so the closure claim survives it'*. There is no roster to add the member to. The claim is not wrong; it is untested, and `§F.3` says so itself (`STATUS: HYPOTHESIS`). What this execution adds is that it cannot be tested by a small step: six rosters and a loader come first.

### `F-31` · of sixteen steps in one trial, five are supplied, ten stop on something that does not exist, and one is ambiguous in the spec

> **`by=construction`** · site: `12_BUILD_ORDER.md`
>
> **already registered?** NEW

5 of 16 steps are supplied or run; 10 stop; 1 is ambiguous. ⭐ The distribution is the result: the steps that RUN are the ones the tree already owned before this design existed — the calendar firing, the presence walk, the fold, the degree ladder. **Every step that stops is one this directory specified.** That is not a criticism of the specification; it is the measurement of how much of it is specification. ⭐ **AND THE WALK FINDS ONE THING THE BUILD ORDER DOES NOT HAVE A STEP FOR.** `12_BUILD_ORDER.md` has twelve steps, three of them (`judging_set`, `release`, `convene` corrected) with a dependency column reading *nothing*. **Step 3 of this walk — somebody putting the matter on the docket — is in none of them.** Step 6 is *`speak` with its `requires`* and depends on steps 0 and 2; step 9 is **THE BAR**, *one seeded proceeding runs end to end with zero authored acts, twice, byte-identical*. A proceeding with zero authored acts requires a docket item naming a matter, `DocketItem.matter` is written by `carry` alone, and no step of the build order produces one. **The plan's own bar is unreachable by the plan's own steps**, by one missing act that costs nothing. ⛔ A draft of this finding said the build order's first buildable thing should be the clerk; the correction is that the build order's step 1 is genuinely buildable and the clerk is simply not in it at all.

### `F-32` · ⛔ WITHDRAWN — the lane's original diagnosis was right and this suite's correction of it was an artifact of the case it ran

> **`by=construction`** · site: `18_FINDINGS.md PART B`
>
> **already registered?** ⛔ WITHDRAWN — the row it 'corrected' stands. Kept as a record of the error, not as a finding

**The claim was**: `18_FINDINGS.md` PART B and `HANDOFF_SC.md` say *no deposit names the actor*, and a speech deposits `(speaker, speech.made, 100, firsthand)`, so the defect is the deposit's CONTENT rather than its absence. ⛔ **It is withdrawn.** `claim_subjects` **replaces** the actor with the act's referents when the act names a subject and writes nothing — `speak` writes nothing, so a real `speak` at a proceeding, which presses a matter ABOUT somebody, deposits about the matter's subject and not about the speaker. The draft's probe built its `speak` with no payload, so the act had no referents and the actor survived through the default branch. **EXECUTED, both ways:** with no payload the bench holds 1 claim(s) naming the speaker; with a subject named, 0. ⭐ **So the mechanism the directory named is real, and `19_PLAN.md` step 2 is aimed correctly** — though `R8.1` supersedes its *prepend the actor* mechanism with the `seen` struct, subjected to the changed thing or else the rung. ⚠ **The method lesson is `§0.1` point 1 in reverse**: I checked a claim about a rule by running a case the rule does not cover, and a green result read as a refutation. Two critics missed it; a third caught it by reading the branch instead of the output.

## C.3 · NIT (1)


### `F-25` · `matter` carries five distinct senses across the live tree and this design, one of which is a barrier name

> **`by=construction`** · site: `04_VERBS.md §B.1`
>
> **already registered?** NEW — and MD-05 declines the rename, so it carries no action: it is recorded so a later session meeting `contests: 'a matter'` cold does not resolve it against `matter_kinds`

{"rosters.yaml: matter_kinds": ["coin", "grain", "ore", "salt", "timber"], "Record.subject_matter": "the case papers' subject", "DocketItem.matter": "what is before the sitting", "contests: 'a matter'": "the contest PRIZE this design declares", "Step.MATTER / WriteClass.MATTER": "the second barrier of the season loop"}. `CLAUDE.md` §4's binding test is IDEMPOTENT IN MEANING — *reading the word cold, in a later session, must yield the same meaning* — and the worked failure it records (`evacuate`) cost real work. Here the collision is worse than a coinage because one sense is a STEP of the loop: `MATTER matures what an act wound` and `a matter is pressed before a bench` are the same word two lines apart in `05_PROCEDURE.md`. ⚠ The design cannot simply rename: `DocketItem.matter` is a live matrix row and `matter_kinds` is a live roster, so the free name is the PRIZE and the disputed Proposition — the two this directory introduced.

---

# PART D · THE WORKED TRIAL — sixteen steps, and where each one stands

*Vellenmark v. the herdsman* — a `HOLDS` matter about cattle, before a settlement bench, `floor: open`. **The walk does not stop at the first block**: every step is recorded so the reader sees where the inventions cluster rather than only where the trace dies.

| # | the step | what it needs | state | invented here | note |
|---|---|---|---|---|---|
| 1 | a person with a `convene` remit sets a date at the settlement | `convene` (remit:convene) writing `Date.due_at` + a ConveningCondition | **SUPPLIED** | — | the verb is `ruled` and both matrix rows exist. The fixture short-circuits the act itself (INV-08) because a chooser that decides to convene does not exist |
| 2 | the date fires and a sitting exists | CALENDAR firing a due Date with a holder | **RUNS** | — | executed in ST-05: the date fired and the docket grew by one item |
| 3 | the docket names the matter | `DocketItem.matter` = the Proposition | **STOPS** | `INV-12` | F-05 — CALENDAR writes `matter: None` and only `carry` writes it. Nobody in the design carries the papers |
| 4 | the bench is identified | `judging_set(venue, matter)` -> seats | **STOPS** | `INV-10` | F-03 — raises unconditionally. NOT stubbed by this harness on purpose: a stand-in bench would make every step below measure my Query |
| 5 | the arrangement is read | a row of fifteen keys from `data/arrangements.yaml` | **STOPS** | `INV-11` | F-04, F-23 — the file does not exist and the twelve markdown rows are partial |
| 6 | the genre is derived from the bench's remit | a Query over remit acts -> {forensic, deliberative, epideictic} | **STOPS** | `INV-16` | F-30 — downstream of step 4 and of a roster that is not in the data |
| 7 | the attendees are frozen | `present_at(venue)` at entry | **SUPPLIED** | — | `Query.presence(w, rung)` exists and answers — the design calls it `present_at`, which does not, but the mechanism is there (ST-04) |
| 8 | the attendees are ordered per `arrangement.order: rank` | a sort by rank within the run | **STOPS** | — | P-08, graded `absent` by the design itself: `order: rank` needs the fold's canonical sort changed for everybody, which is not a parameter of this subsystem |
| 9 | a party speaks | `speak` with `contests: 'a matter'` | **RUNS-THEN-STOPS** | — | ST-09 — an uncontested `speak` folds and emits `speech.made`. ST-10 — the contested one reaches the seam and the seam has no provider (F-01, F-10) |
| 10 | the speech draws against an obstacle | pool = brought + conduct x latitude; Ob = score/2 +- four room terms | **STOPS** | `INV-17`, `INV-18`, `INV-19`, `INV-20` | P-06, graded `assumption` — inject, declare, sweep. Nothing to inject INTO: there is no provider, so the four magnitudes have no site |
| 11 | the margin becomes a degree | `degree_from_net(net, ob)` -> one of four bands | **SUPPLIED** | — | the tree owns the ladder and `speak`'s four keys match it exactly (ST-11). This step is the design's cleanest: it borrows rather than re-deciding |
| 12 | the band's writes are applied | `Person.stance` at three bands; `DocketItem.matter` at Partial | **AMBIGUOUS** | `MD-03` | F-13 — the matrix row is `(Person, stance)` with no subject column, so both the speaker-writes and hearers-write readings load |
| 13 | the ladder rung moves | a fold over this run's `matter.*` emissions | **STOPS** | `INV-15` | F-28 — no emission can name a rung. The design's ZERO-NEW-FIELDS count rests on this fold |
| 14 | the bench determines | `determine` via a seat, one finding out of many determinations | **STOPS** | `INV-13` | F-14 (`disposes:` has no writer), F-15 (no `Act.via`), F-16 (no quorum) |
| 15 | the finding reaches the settlement | `disposal_reach: settlement` minting claims for non-attendees | **STOPS** | `INV-14` | F-21 — no witness channel mints a claim for somebody who was not there |
| 16 | the loser discharges the duty imposed | `release` on the `oblige` the finding opened | **STOPS** | — | F-26 — `release` is not in the verb table, and the design says it is LANDED |

---

# PART E · THE PER-GAME MATRIX — what each of the twelve is stopped by

**Read the columns, not the rows.** Every cell is a stress test's verdict, so a row's state moves when that test's does. **No row is blocked by a parameter of its own** — the blockers are shared mechanisms, which is the closure claim holding and the catalogue not yet paying.

| game | met | blocked | what it is waiting on |
|---|---|---|---|
| **negotiation** | 0 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · more than two parties can settle mutually (`ST-17`) · the opening act declares term and stages (`ST-07`) · a declared term can mature (`ST-18`) · the ruling reaches beyond the room (`ST-21`) |
| **negotiation/envoys** | 0 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · more than two parties can settle mutually (`ST-17`) · the opening act declares term and stages (`ST-07`) · a declared term can mature (`ST-18`) · the ruling reaches beyond the room (`ST-21`) |
| **arbitration** | 0 | 7 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · the `disposes:` key has a writer (`ST-14`) · the opening act declares term and stages (`ST-07`) · a declared term can mature (`ST-18`) · the ruling reaches beyond the room (`ST-21`) |
| **legal trial** | 1 | 8 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ladder rung is nameable (`ST-28`) · the ruling reaches beyond the room (`ST-21`) |
| **tribunal** | 0 | 7 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ruling reaches beyond the room (`ST-21`) |
| **interrogation** | 0 | 7 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ladder rung is nameable (`ST-28`) · the ruling reaches beyond the room (`ST-21`) |
| **inquisition** | 0 | 8 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ladder rung is nameable (`ST-28`) · the ruling reaches beyond the room (`ST-21`) |
| **excommunication** | 0 | 8 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · why the subject is absent is readable (`ST-20`) · the ruling reaches beyond the room (`ST-21`) |
| **parliament** | 0 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · the ruling reaches beyond the room (`ST-21`) |
| **council of state** | 0 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · many determinations become one finding (`ST-16`) · the `disposes:` key has a writer (`ST-14`) · the ruling reaches beyond the room (`ST-21`) |
| **audience / embassy** | 0 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ruling reaches beyond the room (`ST-21`) |
| **appeal** | 1 | 6 | the row can be loaded at all (`ST-04`) · the matter is on the docket (`ST-05`) · a bench can be identified (`ST-03`) · the `disposes:` key has a writer (`ST-14`) · an adjudicator can act as a seat (`ST-15`) · the ruling reaches beyond the room (`ST-21`) |

---

# PART F · THE ADVERSARIAL PASS — what two critics broke in this suite

**Method (`CLAUDE.md` §10).** Agonist→antagonist as a **relay, not a dialogue**: the suite was run,
its output written to `stress/results.json`, and two `valoria-critic` agents dispatched with that
JSON and **not with the reasoning behind it**. Independence is structural rather than declared —
`.claude/agents/valoria-critic.md` grants `Read, Grep, Glob` and no write tools, so neither could
edit what it attacked. Disjoint lanes, so neither saw the other's finding:

| lane | brief |
|---|---|
| **A · verification** | attack the FACTS. For each finding: is it true against the tree; is its evidence grade inflated; **and does it duplicate a row the design already registers** |
| **B · coverage and method** | do not re-verify facts. Attack what the suite did not test, whether the invention log is honest, whether the decisions were really only five, and **whether the headline measures its own premise** |

**Between them they attacked every finding and every line of the harness.** What follows is what
they broke. Each correction is applied in place and recorded at its own site as well, so a reader of
one finding does not need this section to know it was retracted.

## F.1 · Two findings were FALSE and are withdrawn

| | what the draft claimed | what the tree says |
|---|---|---|
| ⛔ **`F-08`** | *"the `scale:` key the design corrects is ALREADY GONE from the table this repo carries"* | It is at `verb_table.yaml:138`, in the exact range the design cites. **And the finding contradicted itself in its own output**: it interpolated `scale present = True` into the same paragraph and printed `scale key absent (True)` as its verdict line. The test is rewritten to ask the question that was worth asking — *does the loader refuse it?* — and the answer is no, so invariant 10 is a specified invariant with no implementation |
| ⛔ **`F-21`** | *"`disposal_reach` must mint claims for people who were not there **through no channel** — it needs a SIXTH witness channel"* | **Two channels already do it.** `_ch_post_remit` walks a person's live `hold` Tenures for an office whose `remit_acts` intersect the emitting verb's eligibility, **with no presence test** — which is `body` exactly. `_ch_chronicle`'s own docstring says *when it fires it fires for everyone alive* — which is `<rung kind>` at its widest. The finding was graded `construction` and was an inference from a roster listing, made without opening the module that has the mechanism. Rewritten: the carriers exist and **neither fires**, which is a narrower and better result |

## F.2 · One finding was STALE, and the register it cited is the stale surface

⛔ **`F-16`** treated the quorum as an open question and promoted it to a build blocker, quoting
`10_LOOPS_AND_GAPS.md` `P-15`. **`P-15` is closed** — `19_PLAN.md` step 15 and `ED-SC-0034`
(`status: ruled`, `needs_jordan: false`) record Jordan's *"of course we accept those shapes."*
**This suite had the ruling in hand and cited it in the very next test.** The corrected finding is
that the register row is stale in the file `README.md` sends a reader to first, and that the ruled
shape needs a declaring act no verb supplies. `MD-04` is the general form: **check every gap-register
row against the newer rulings before citing it** — `P-29` is the second stale one, and `F-37` found
that five more rows are not in that register at all.

## F.3 · One execution was VOID and the finding rested on it

⛔ **`F-05`** reported an empty docket after one season as evidence that CALENDAR writes
`matter: None`. It was not evidence of anything: `World.tick` starts at 0 and `season()` increments
at its **end**, so a date `due_at: 1` is never reached in a single season and CALENDAR's guard
skipped the branch. **The empty list measured the fixture's off-by-one.** Re-run over two seasons
the date fires, the docket item appears, and its matter is `None` — so the finding is now supported
by the execution it claimed. And the critic found a second defect the draft had missed and that is
now the sharper half: **`speak`'s prose `requires` and its typed cell do not agree.** The prose says
*whose docket names the subject*; the typed form is a bare existence test that a docket item with
`matter: None` satisfies. Under `CLAUDE.md` §0.05 the typed cell is the mechanism, so the *empty
sitting* reading wins and the design's own account of what `speak` is for does not.

## F.4 · Four counts were wrong

| | was | is |
|---|---|---|
| `F-11` | *"nine non-ladder band names… none of them the ladder's"* | **eight.** `Partial` **is** the ladder's third band and appears in two of the five rows |
| `F-23` | *"9 of 15 §E.2 blocks are partial"* | the block selector matched any ```yaml block in the file containing one of four words, sweeping in PART D's own schema block and PART F's examination. **Scoped to §E.2: 8 of 13** |
| `F-27` | two emission mismatches | **four** — the harness's filter dropped `Record`, and `08_SEAM.md` §D.1 also claims `case.opened` for two rows the matrix gives `record.created`/`record.destroyed` and `record.staged` |
| `F-29` | *"0 of 13 rows runnable"*, from a hand-typed blocker table | ⛔ **the worst defect in the suite: `runnable = []` was an identity.** Every value in the needs map was a non-empty list, so the number could not have come out otherwise — `CLAUDE.md` §0.1 point 2 committed inside a suite that cites §0.1. **Each need now names a stress test and reads that test's real verdict**, so the matrix moves when its blockers do. And `public debate` is no longer counted: `14_THE_WORLD_IN_THE_ROOM.md` §E.3 retires it, so scoring it inflated the denominator with a row the design withdrew |

## F.5 · Four severities and one citation were wrong

`F-04` and `F-26` were `blocking` on things the design self-grades `HYPOTHESIS` and `CONVENTION`;
`F-25` proposes no action and is a `nit`; `F-28` was `blocking` on a trilemma that omitted a fourth
option costing nothing (the fold already keeps `resolved` and `act_of`, and `ED-SC-0034` licenses
per-run aggregates). `F-03` cited `shape.py:3166`, which is `Query.presence`; `judging_set` is at
`:3161` — **the design cites it correctly and this suite did not**, inside a finding about citation
discipline. And `F-26` read the second word of a two-word table cell: *"⭐ LANDED"* means landed in
this proposal, whose replacement row is written out at `04_VERBS.md` §B.5, not landed in the tree.

## F.6 · Six omissions, all of them now tested

Lane B's central charge was that the suite *"audited the plumbing floor of a building whose own prior
pass says the fire is upstairs."* It was right, and five tests exist because of it:

| what was missing | now |
|---|---|
| **the suite never opened a ledger** — it built a fixture with five people in a room and never asked what any of them ended up holding | ⭐ `ST-32`, and it produced the correction at `F-32` |
| **the absent subject was invented and never used for the one thing absence is for** | ⭐ `ST-33`, and it falsifies the design's most-quoted *needs no mechanism* claim under the arm in force |
| **no test touched `06_RESOLUTION.md`** — including the deprivation floor, which the design calls *a blocking check on shipping the composed obstacle, not an advisory one* | `ST-34`, which finds the check is specified against a `p_success` the ladder module does not export |
| **nothing was permuted**, in a directory whose procedure file is titled by the permutation test | ⭐ `ST-36` — and it **passes** |
| **determinism was never checked** | ⭐ `ST-35` — and it **passes** |
| **the gap register was never counted** | `ST-37`, `F-37` |

## F.7 · The invention log was incomplete, and its own completeness claim was false

`proceedings_world()` said *"every line of this function is an INVENTION and is registered as one."*
It was not: the seed, the grain stores, the subsistence model, the chooser and — pointedly — **a
manifest installed directly on the world**, in a suite whose first finding reports that no manifest
exists. All are now logged (`INV-21`, `INV-22`, `INV-23`), including the eight swept fixture
constants inherited whole from `DEFAULT_FIXTURES`. **Three rows were also mis-owned**: `INV-03`,
`INV-06` and `INV-07` were graded `fixture` while their own `owner` strings said the design owes
them, so the split was reported as 8 fixture / 8 mechanism when by the log's own rule it is
**8 / 15**. The `owner` column is the one the log calls load-bearing, and it was the one that was
wrong.

## F.8 · What the critics did NOT do, said so the clean surface is not mistaken for a checked one

- **Neither ran the harness.** Both read `results.json` and the source. A defect that only appears
  when the code executes differently from how it reads would have survived both.
- **Lane A did not attack the four `probe-model` findings on their models**, only on their grades.
- **Lane B did not verify a single factual claim**, by design — so a finding that survived lane A
  and was extended by lane B's coverage work has been checked once, not twice.
- **Neither attacked PART D's walk**, which was written after they were dispatched.
- ⚠ **And one lane-B observation is unresolved and is recorded rather than answered**: `F-29`'s
  closing sentence originally said *`12_BUILD_ORDER.md` lists three steps buildable today and none
  of the six blockers is among them*, while `12_BUILD_ORDER.md` step 1 **is** `Query.judging_set`,
  graded *buildable today — four lines and a walk*. The sentence is removed. Whether the six
  blockers are as expensive as this suite's framing implies is a question `12`, `17` PART I and
  `18` PART L answer three different ways, and **this suite is not the surface that should settle
  it.**

  ⭐ **Checking that observation found two more of this suite's own errors, both now corrected in
  place.** `F-26` claimed `release` is absent from the build order's buildable-today list; it is
  **step 3**, dependency column *nothing*, execution artifact written out. And `F-31` proposed the
  clerk as the first thing to build in preference to step 1; step 1 is genuinely buildable, and
  the correct — and much better — finding is that **the clerk is in none of the twelve steps at
  all**, which makes step 9, the plan's own BAR (*one seeded proceeding runs end to end with zero
  authored acts*), unreachable by the plan's own steps for want of one act that costs nothing.

---

# PART G · WHAT THIS SUITE STILL DOES NOT REACH

**Stated so the clean surface is not mistaken for a checked one** (`§F.34`: a defect in neither
register is invisible to both counts).

| not tested | why, and who should |
|---|---|
| **the composed obstacle's arithmetic end to end** | `ST-34` reached the ladder and found no `p_success` export. The design's `M-7` and `M-8` are **blocking measurements** and need the provider that does not exist; until then they cannot be run, only specified |
| **the σ-channel's uniformity at proceeding pools** | `06_RESOLUTION.md` cites `0.874174` across pools 0.5→25 from the resolution diagnostic. Not re-measured here; taken on the diagnostic's authority |
| **anything across seasons** | `P-42` (does a witnessed concession survive the ledger cap) needs a seeded multi-season run with one recurring bench. The harness drives `SeasonDriver` and could do it; it is a measurement, not a stress test, and it belongs to `19_PLAN.md` step 3 |
| **the player-facing contract** | `07_THE_GAME.md` PART D's owed/forbidden table. `explain()` was not called |
| **the licence veto** | Fig. 26's four conjuncts as a demote-only band extension. `dice_engine.BandExtension` exists; no test drove one |
| **any of the twelve rows as a ROW** | there is no loader and no arrangements file, so no row has been loaded, only read |
| **the study** | out of scope by declaration, not by omission |

---

## Provenance

**Everything in PARTS A–E is generated from the run** (`python3 stress/stress_proceedings.py --md`),
so a finding cannot drift from the execution that produced it. PART F and this section are written.
`stress/results.json` is the machine-readable output. **Nothing in this file edits the design**, and
nothing in it ratifies: the directory remains PROPOSED and HELD BACK IN FULL.
