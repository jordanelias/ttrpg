# THE TWO PATHWAYS FAIL FOR CATEGORICALLY DIFFERENT REASONS

## Status: **RATIFIED 2026-09-05 (ED-IN-0202) — Jordan ruled "adopt in full". This is LAYER 1: the code architecture and shape, which GOVERNS HOW ALL CODING IS CONDUCTED. Under CLAUDE.md §0.05 it is reference for GAME MECHANISM — the code is the formula — and binding as AGENT INSTRUCTION, the same standing as CLAUDE.md itself. The game code it governs is `engine/season/`.**
## Scope: PR #337 → now. Companion to `ARCHITECTURE_V2.md`; computed from the session's probe ledger.

> ### THE FINDING, IN ONE LINE
> **ZERO percent of the NPC set's core blocks are design refusals. THIRTY-THREE percent of the arc
> set's are.** The two pathways were assumed to be two samples of one question. They are not.

> ### ⚠ EVERY NUMBER IN THIS DOCUMENT IS ROUTER-ERA AND IS NOT CURRENTLY REPRODUCIBLE.
> Amended 2026-09-02 by `W10`'s adversarial pass. **The finding is not withdrawn and not
> confirmed.**
>
> The census below counts **probe ids** in `results.json`'s `blockers`, because under the regex
> router a probe was the only thing a case row could reach. `W10` deleted that router: routing is
> now an authored `exercises:` declaration bound to each row by the sha of its own need text, and
> `blockers` names the declared token that failed — a hole id, a verb, or `probe:PID`. The old
> query has no subject, and re-running it returns zero in both columns.
>
> Two consequences, and the second is the one that matters:
>
> 1. **The router's counts were a floor.** A row matching no pattern fell silently to UNMAPPED,
>    so every figure here understated the corpus **in the direction that flattered it**. `PLAN.md`
>    §3.5 already found three cells wrong in exactly that direction before `W10` landed.
> 2. **The ARC lane has 0 of 611 rows declared today** (`cd proposals/2026-09-01-season-loop-tests/tracer
>    && python exercises.py`). So the arc column is **unmeasured**, not measured-as-something —
>    §42.2's polarity rule. The NPC lane has 35 of 292 (32 of 122 core), which is a sample, not a
>    census.
>
> **Do not cite these percentages as current.** They are kept because they are what a
> re-measurement has to beat, and because the qualitative claim — that the two pathways fail for
> categorically different reasons — is a live hypothesis that `W13`'s authoring lane is the test
> of. `CLAUDE.md` §0.1 point 4: a number without a control is not a measurement, in either
> direction.

---

## §1 · The measurement

Core blockers, both pathways, ranked. **REFUSED** marks a probe whose gap is the design declining
something on purpose (L1, L3, L5, §25.1, §29) rather than failing to say something.

| probe | NPC | ARC | | what it is |
|---|---:|---:|---|---|
| `P17` | 4 | 16 | | a quantity accumulates quietly in one person across seasons |
| `P33` | 2 | 5 | | an act costs more when it is bigger |
| `W10` | 0 | **7** | **REFUSED** | a settlement holds a level of discontent |
| `P22` | 2 | 5 | | a held object gates another's act |
| `P26` | 2 | 5 | | accumulated harm changes what a person may do |
| `P10` | **5** | 1 | | a person tracks multi-season work in progress |
| `A3` | 0 | **4** | **REFUSED** | an arc ends at a counter with nobody deciding |
| `W13` | 0 | **4** | **REFUSED** | a background quantity decays on a schedule nobody wound |
| `A15` | 0 | 4 | | a spiral terminates |
| `A27` | 0 | 3 | | every value the game needs has an owner |
| `P38` | 0 | **3** | **REFUSED** | an outcome is judged by a referee |
| `F3` | 0 | **3** | **REFUSED** | a faction acts |
| `A7` | 0 | 2 | | a contest is the season loop nested |
| `P32` | **2** | 0 | | a person's own condition narrows their options |
| `P41` | **2** | 0 | | a precedent is cited to strengthen an argument |
| `P35` | 1 | 0 | | a private track of regard, separate from a public one |
| `F21` | 1 | 0 | | a member's position recorded in a body's collective output |
| `F19` | 1 | 0 | | a place produces a demand with nobody petitioning |
| `F16b` | 0 | 1 | **REFUSED** | a faction-wide **social** quantity is pooled and stored |

| | NPC | ARC |
|---|---|---|
| core blocks | 25 | 66 |
| **of which design REFUSALS** | **0 (0%)** | **22 (33%)** |

> ### ⚠ CORRECTED 2026-09-02 — **`0%` IS WRONG, AND THE `core blocks` ROW DOES NOT REPRODUCE.**
> An independent adjudication of this document (see `PLAN.md` §1 and §3.5) established two things.
>
> **(a) `P33` — *"an act costs more when it is bigger"* — is a RULING, not a hole.** #353 `:927-930`:
> *"**No cost clause is required. A petition consumes budget like any act, and that is the whole of
> the pricing.**"* `F19` — *"a place produces a demand with nobody petitioning"* — is likewise
> substantively an L1/T5 refusal, filed here under §36.1. Reclassifying them:
>
> | | published | `P33` a refusal | `P33` + `F19` |
> |---|---|---|---|
> | NPC blocked cases touching a refusal | **0** | **2** | **3** |
> | NPC blocked **only** by refusals | **0** | **1** (NPC-089) | **2** (NPC-083, NPC-089) |
> | ARC touching a refusal | 22 | **25** | **25** |
> | ARC blocked **only** by refusals | — | **17** | **17** |
>
> **(b) Three different totals are in circulation for one quantity.** Summing `core_blocked` over
> `results.json` gives **26 · 71**; the row above says 25 · 66; the probe table's own rows sum to
> 22 · 63. None shipped with a command. See `PLAN.md` guardrail **G11**.
>
> **The qualitative conclusion survives and is sharper — 21 of 23 blocked NPC cases contain no
> refusal at all — but a claim of exactly zero should have had a control, and §0.1 point 4 says so
> in both directions.** Two further omissions: `P6` and `P20` block NPC cases (NPC-021, NPC-035) and
> appear in neither column.
| verdicts | 23 BLOCKED · 20 NOT-ASSESSED · 2 PLAYABLE · 1 DEGRADED | 53 BLOCKED · 40 NOT-ASSESSED · 3 DEGRADED · 1 PLAYABLE |
| scale mix | person 21 · faction 18 · realm 5 · settlement 1 · world 1 | **realm 43** · faction 29 · person 16 · world 9 |

---

## §2 · What each result means

### §2.1 The NPC pathway is blocked almost entirely by holes

⚠ **This section's heading read *"ENTIRELY"* and its first sentence read *"Not one of the 25 core
blocks is a refusal"*. Both are corrected above: with `P33` and `F19` reclassified, 2–3 of 26 are
refusals. The measured statement that survives is the one that matters — 21 of 23 blocked NPC cases
contain no refusal at all.**

**Almost none of the core blocks is a refusal.** Every one is something `ARCHITECTURE_V2.md`'s
register now carries a row for:

| blocker | the hole | register |
|---|---|---|
| `P10` (5) | multi-season work in progress — a `Record` with act-declared stages, and **no Partition row for any of it** | **H-22** |
| `P17` (4) | L3 clause 1's counter — **permitted by the head**, with no registry and no write row | **H-20** |
| `P22` (2), `P26` (2), `P33` (2) | Record custody · accumulated harm · act cost | H-22 · H-20 · **H-23** |
| `P32` (2), `P35` (1) | a person's banded scalar · a second standing track | **H-38** · **H-29** |
| `P41` (2), `F21` (1), `F19` (1), `F6` (1) | the fault roster · the judging set · a placeless want · refraction's side | **H-37** · **H-32** · §36.1 · **H-36** |

> **THE CONSEQUENCE IS DIRECT: closing the register's holes unblocks the NPC pathway almost
> completely.** Nothing about a named character's season asks the design to be a different design.
> **They are asking it to finish being itself.**

### §2.2 The arc pathway is a third refusals — and those arcs want a design that was replaced

`W10` (7) · `A3` (4) · `W13` (4) · `P38` (3) · `F3` (3) · `F16b` (1) = **22 core blocks the
specification declines on purpose**: a place storing a social level · a counter ending the story with
nobody deciding · a quantity advancing with no author · a referee adjudicating · a faction acting.

**Those are not oversights. They are the five things the architecture exists to refuse**, and the
arcs asking for them were authored against a stat-track model with faction meters, world tracks and
a GM — the model §353 replaced deliberately.

> **THE CONSEQUENCE IS EQUALLY DIRECT AND MUCH LESS COMFORTABLE: no amount of specification work
> unblocks those 22.** They are re-authored against the primitives, or they do not run. Part VIII's
> price — *"8 of 50 surveyed arcs, honestly"* — is real, and at 97 arcs it is 22 core blocks.

### §2.3 Why the split exists — the scale mix explains it

**NPC cases are person-scale (21) and faction-scale (18). Arc cases are realm-scale (43).**

The design's refusals all bite at aggregate scale: L3 refuses a stored social aggregate, L5 refuses
a threshold outcome, L1 refuses an institutional actor. **A person-scale case rarely needs any of
them; a realm-scale case reaches for all of them**, because "the realm grows unstable" is the
natural way to write a realm-scale story and the design has deliberately made it unspellable.

> **This is the design working as intended, and it is expensive.** The refusal is what makes
> obstruction fall out with no verb and makes a stranger able to block an ambition nobody knew about.
> **The same property makes a third of the arc corpus unrunnable as written.**

---

## §3 · The throughline internal to each set

**NPC set — one throughline: THE PERSON HAS NO DURABLE INTERIOR THE ENGINE READS.**
`P10` (work in progress), `P17` (a quiet counter), `P26` (accumulated harm), `P32` (a condition
band), `P35` (a second standing), `P22` (what they hold) are all one shape: **a person accumulates
something across seasons and it changes what they may do.** #353 gives `Person` six interior fields
and **no formula consumes any of them**; the one banded gate it defines has a `Site` as its carrier.
`ARCHITECTURE_V2.md` §F2 is the first formula in the chain that reads `convictions` and `stance`.

**ARC set — one throughline: THE ARCS WANT A NARRATOR AND THE DESIGN HAS DELETED THE ROLE.**
`A3` (a counter ends it), `W13` (a clock nobody wound), `P38` (a referee judges), `F3` (an
institution acts), `W10` (a place has a mood) are one shape: **something that is not a person makes
the story move.** The in-chain survey already measured the honest version of this — **19 of 50 arcs
want a crossing to COMPEL A NAMED PERSON**, which L5 permits exactly, and only 8 want the crossing
to ACT. At 97 arcs the residue is 22.

---

## §4 · What follows for the successor

1. **The register's Tier 0 and Tier 1 holes are aimed at the NPC pathway** and should unblock most
   of it. That is the cheapest large gain available.
2. **The arc pathway needs a second, different piece of work** that no specification change
   delivers: **an authoring pass that re-expresses ~22 arcs against §36.3's petition chain and
   §37's dispensation-as-`tell`**, which is where the "counter compels a person" shape already lives.
3. **The two pathways must not be averaged again.** A single headline number over 143 cases hides
   the fact that one set is blocked by silence and the other by principle. **They are different
   questions and they have different answers.**
4. ⚠ **`P17` is the one blocker large in both sets** (4 NPC, 16 ARC) and it is a hole, not a
   refusal — L3 clause 1 **permits** a per-`(Person, axis)` counter. **H-20 is the single
   highest-value row in the register.**

---

## §5 · Honesty markers

- **The case verdicts are not cited here as playability**, per two independent auditors. **Every
  number in §1 is a count of core rows routed onto a probe whose gap was an execution** — the layer
  both auditors ruled bankable.
- **The REFUSED classification is the orchestrator's**, applied to probe ids by which law each
  cites. It is checkable: each probe names its section.
- **60 of 143 cases are NOT-ASSESSED** and contribute no blockers, so both columns understate.
  There is no reason to expect the understatement to be uneven between them, but it is not measured.
- **The 33%/0% split is robust to the router's known defects** in one direction: every routing fix
  this session made moved cases *out* of refusal blockers and into holes. **If the router still
  errs, the arc set's refusal share is an over-count, and the NPC set's zero cannot move.**
