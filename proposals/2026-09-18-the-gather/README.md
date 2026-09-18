# THE GATHER — every design proposal tree, dispositioned, and the order they imply

## Status: **PROPOSED (2026-09-18). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` (cross-cutting) · **`ED-IN-0252`**
## Grade under `CLAUDE.md` §0.2: **`measured`** for `00` and for every disposition carrying an opened `file:line`; **`paper`** for `05_THE_ORDER.md`. **Nothing in this suite has run.**
## Supersedes: **nothing.** It disposes OF trees; it replaces none of them.
## ⚠ It is NOT a fourth order. `workplans/2026-09-11-reconciled-program.md` §3 is the RATIFIED single owner of the order (`ED-IN-0215`) and `05` is an **amendment** to it, not a rival.

> **Jordan, this session:** *"I want the design proposal trees to be gathered today and orchestrated
> as per previous PRs recently."*

---

## §1 · WHAT `CLAUDE.md` §3 REQUIRES OF THIS DIRECTORY, ANSWERED FIRST

§3 admits nothing new under `proposals/` without answering it:

> **Before starting a new directory here, answer what it changes in `engine/season/`.**

**The gather itself changes nothing in `engine/season/`, and that is the wrong question to stop at.**
What it changes is *which* `engine/season/` work a session finds when it looks — and the answer is
specific, not rhetorical. Every disposition row in `01`–`04` carries an **`engine_season:`** column
holding either a path plus what changes, or the literal `NONE`. The rows that are not `NONE` are the
deliverable. As of writing they are expected to include:

| change | where | why it is not scheduled today |
|---|---|---|
| **phase-6 items 6a/6b/6c** — the affiliation roster, the moral-basis rename, the re-authored thirteen | `references/descriptor_registry.yaml`, `engine/season/rosters.yaml` (`tables.conviction_projection`, `tables.alignment`) | unblocked **hours ago** by `ED-IN-0251` (R1/R2). No order knows they are free |
| **the migration verb** — nobody in Valoria can relocate | a verb + effect; `move` is a `travel_leg` Tenure alter and `residence` is a contested claim predicate **with no writer** | opened by the 2026-09-17 rulings; `01_THE_BUILD_ORDER.md`'s own preamble says *"this order does not schedule"* it |
| **`H-71`'s remit read** — `person_side_eligible` declines every `remit:` alternative unconditionally | `engine/season/`, a ~2-line read of `Tenure.payload`, licensed by `write_matrix.yaml:336-342` | `CAT-6` → ARM 2 decoupled it from item 5, and the order still carries the old dependency |
| **settlements P1–P4** | position 24, `SE-BUILD`, gated on `ED-SE-0051` | part of P1/P2 already landed as items 3a/3b — see `02` |

**If `01`–`04` come back with `NONE` in every row, this directory has failed its own §3 test and should
be deleted rather than kept.** That is the honest condition and it is written before the results.

## §2 · WHY A GATHER AND NOT A FIFTEENTH SUITE

`00_THE_CENSUS.md` measures it: **553 files, 175,079 `.md` lines, 272 `## Status:` lines, of which 3
are `RATIFIED`.** Fourteen trees hold 75% of those lines. Two have no `## Status:` line at all. One,
created yesterday, is referenced by **nothing anywhere** and declares itself *"a queue by
construction"*.

`CLAUDE.md` §3 says this is *"the shape `.audit/` was retired for"*, and the commit that cut Layer 0
by 24% named `proposals/` as needing **a policy call**. This is that call, and its output is
**subtraction**: every row names a successor, a code site, or the word `ORPHAN`. A reader who finishes
`01`–`04` should have FEWER trees to open, not one more.

**The precedent is `proposals/2026-09-17-governance-and-behaviour/` (#413)** and the census shows why:
it is read **20 times by the rest of the repository and once by `proposals/`**. That asymmetry is the
signature of an orchestrating document — it points outward and nothing in the corpus depends on it.
This suite is built to the same shape and should carry the same asymmetry or be deleted.

## §3 · WHAT THIS SUITE DOES NOT DO — stated so an omission is not read as an oversight

1. **It does not ratify anything.** `ED-1094`'s ratify-on-merge does NOT apply; merging this adopts
   nothing, flips no `## Status:` line, moves no `CURRENT.md` row.
2. **It does not delete a tree.** A disposition is a verdict, not an execution. Retirement means
   deletion plus a `FORK:` row in `references/restructure_ledger.md` (`CLAUDE.md` §1), and that is a
   separate commit with Jordan's word on it.
3. **It does not answer `ED-SE-0051`.** Two defensible arms, materially different games; it survived
   all five of §0's tests and it is Jordan's.
4. **It does not flip `CURRENT.md:31`**, which `ED-IN-0251`'s R2 overturns. Held deliberately; the
   ledger row says why and tells a later session to flip it in a commit that says so.
5. **It creates no standing corpus and no `.audit/`-shaped tree.** The record dies when its subject
   dies (§0).
6. ⚠ **It IS a queue, and it does not claim §0's terminal-pass exemption.** `05` creates work for a
   future session. That is what a proposal is; the exemption is for a verdict about something that
   already exists. `proposals/2026-09-18-character-decision-layer/PROPOSAL.md` says the same of itself
   and is right to.

## §4 · METHOD — and its one real limitation

Reading shared once, judgment forked four ways (`CLAUDE.md` §10 pt 1): one batched read-only
measurement lane (Haiku, `valoria-measure`, no write tools) produced `00`, and its table was handed
DOWN to four authors rather than re-measured by each. Four judgment lanes, sized to the subject and
not to the slot (§10) — governance, settlements, decisions, and the long tail, which is 60% of the
corpus by line count and the largest thing no prior pass dispositioned.

⚠ **THE LIMITATION, NAMED: the four authors are producers, and a producer's disposition of its own
lane is not a control.** §10's adversarial pairing buys independence for VERDICTS, and the verdicts
here are the dispositions. Where a row's verdict would license a deletion, treat it as `PLAUSIBLE`
until a structurally independent reader has attacked it — `valoria-critic` has no write tools, so its
independence is structural rather than declared. **No row in this suite is licence to delete a tree.**

## §5 · READING ORDER

⚠ **THE SUITE IS INCOMPLETE AT THIS COMMIT AND THE TABLE SAYS SO PER FILE.** A reading order that
lists files which do not exist is the defect this repository keeps paying for; the state column is
here so nobody opens a promise.

| file | state | what it holds |
|---|---|---|
| `00_THE_CENSUS.md` | **COMPLETE** | the measured numbers, every one with its command |
| `01_GOVERNANCE.md` | **COMPLETE** | the 09-03 corpus rebuild, holdings r1/r2, the seam |
| `02_SETTLEMENTS.md` | **WRITTEN — receipt pending** | the 09-10 set, `ED-SE-0051/0052/0053`, and what of P1/P2 is already built |
| `03_DECISIONS.md` | **WRITTEN — receipt pending** | the conviction layer, the 09-18 orphan, and what `ED-IN-0251` unblocked |
| `04_THE_TAIL.md` | **COMPLETE** | degree-sweep, proceedings, social-contest branches, emergent narrative ×2, greenfield, term-ownership |
| `05_THE_ORDER.md` | **NOT WRITTEN** | the amendment to the ratified order — only the items no order schedules |

**"Receipt pending" means the file is on disk and its author had not yet handed back when this was
written** — so its rows are unreviewed by the orchestrator, not unwritten. Stated rather than smoothed:
§10's relay reconciles in the orchestrator, and that step has not run for those two.
**`04_THE_TAIL.md` is the one that mattered most** — 60% of the corpus by line count, and the largest
thing no prior pass had dispositioned.

Sequential parts in reading order, per `CLAUDE.md` §4's ruling. **Not an `_index` + `_infill` pair**,
which is retired as a default.
